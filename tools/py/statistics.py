from itertools import count
from itertools import pairwise
from pathlib import Path
from textwrap import dedent

import rich.box as box
from rich.box import Box
from rich.console import Console
from rich.pretty import Pretty
from rich.table import Table
from typer import Argument
from typer import Typer

from tools.py.console import console
from tools.py.utils import is_exist

app = Typer()

m_seps = [10, 30, 50, 75, 100]
eps_seps = [0.00, 0.01, 0.1, 0.2, 0.3, 0.4]


def classification_seed(seed: int):
    with open(f"./in/{seed:04}.txt") as f:
        m, eps = f.readline().split()
        m = int(m)
        eps = float(eps)

    res = []

    for i, (s, e) in enumerate(pairwise(m_seps)):
        is_last = i == len(m_seps) - 2
        if s <= m < e or (is_last and m == e):
            res.append(i)
            break
    else:
        raise ValueError(f"m={m} is out of range")

    for i, (s, e) in enumerate(pairwise(eps_seps)):
        is_last = i == len(eps_seps) - 2
        if s <= eps < e or (is_last and eps == e):
            res.append(i)
            break
    else:
        raise ValueError(f"eps={eps} is out of range")

    return res


s_count = [
    [{"score_sum": 0, "count": 0} for _ in range(len(eps_seps))]
    for _ in range(len(m_seps))
]
all_count = {"score_sum": 0, "count": 0}


def load_seed(seed: int):
    with open(f"./score/{seed:04}.txt") as f:
        score = int(f.readline())

    (m, eps) = classification_seed(seed)

    s_count[m][eps]["score_sum"] += score
    s_count[m][eps]["count"] += 1

    all_count["score_sum"] += score
    all_count["count"] += 1


@app.command()
def stat_main(seed_start: int = Argument(0), seed_end: int = Argument(None)):
    it = range(seed_start, seed_end) if seed_end is not None else count(seed_start)

    for seed in it:
        if not is_exist(seed):
            if seed_end is None:
                break
            else:
                raise Exception(f"Seed {seed} does not exist.")
        load_seed(seed)

    table = Table(
        title="Statistics",
        title_justify="left",
        box=box.SQUARE,
        header_style="bright_yellow",
    )
    table.add_column(" ")
    for i, (s, e) in enumerate(pairwise(m_seps)):
        table.add_column(f"[{s},{e})" if i != len(m_seps) - 2 else f"[{s},{e}]")

    for i, (s, e) in enumerate(pairwise(eps_seps)):
        row = []
        for j in range(len(m_seps) - 1):
            c = s_count[j][i]
            if c["count"] == 0:
                row.append("[red]N/A[/]")
            else:
                row.append(f'[cyan]{c["score_sum"] / c["count"]:.2f}')
        table.add_row(
            f"[{s},{e})" if i != len(eps_seps) - 2 else f"[{s},{e}]",
            *row,
            style="bright_yellow",
        )

    foot_table = Table(
        show_header=False,
        show_lines=False,
        show_edge=False,
        show_footer=False,
        box=Box(
            """\
    
  : 
    
  : 
    
    
  : 
    
"""
        ),
    )
    foot_table.add_column("name")
    foot_table.add_column("value")

    foot_table.add_row("[bold]All Count", f'[cyan]{all_count["count"]}')
    foot_table.add_row("[bold]All Score Sum", f'[cyan]{all_count["score_sum"]:.2f}')
    foot_table.add_row(
        "[bold]Average", f'[cyan]{all_count["score_sum"] / all_count["count"]:.2f}'
    )

    console.print(table)
    console.print(foot_table)

    with open("./score/0.txt", "w") as f:
        f_c = Console(file=f)
        f_c.print(table)
        f_c.print(foot_table)


def main():
    app()


if __name__ == "__main__":
    main()
