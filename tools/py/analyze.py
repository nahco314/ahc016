from itertools import count

from rich.panel import Panel
from termplotlib.figure import Figure
from typer import Argument
from typer import Typer

from tools.py.console import console
from tools.py.utils import count_seps
from tools.py.utils import is_exist

app = Typer()


def get_line(f) -> str:
    while (line := f.readline())[0] == "#":
        pass
    return line


def analyze_seed(seed: int):
    corrects = []
    with open(f"./in/{seed:04}.txt") as f:
        m, eps = f.readline().split()
        m = int(m)
        eps = float(eps)

        for _ in range(100):
            corrects.append(int(f.readline()))

    answers = []
    with open(f"./out/{seed:04}.txt") as f:
        n = int(get_line(f))
        graphs = []
        for i in range(m):
            graphs.append(get_line(f))
        for _ in range(100):
            answers.append(int(get_line(f)))

    wrongs = []
    for i in range(100):
        if answers[i] != corrects[i]:
            wrongs.append((i, answers[i], corrects[i]))

    with open(f"./score/{seed:04}.txt") as f:
        score = int(f.readline())

    return m, eps, n, graphs, answers, corrects, wrongs, score


@app.command("a")
def analyze_main(seed: int):
    m, eps, n, graphs, answers, corrects, wrongs, score = analyze_seed(seed)
    console.print(f"m={m}, eps={eps}, n={n}")
    console.print("wrongs nums:")
    nums = []
    for i, a, c in wrongs:
        nums.append(c)
    console.out(sorted(nums))

    fig = Figure()
    ranges, c_vals = count_seps([i for i in range(0, 101, 5)], nums)
    names = []
    for s, e, is_last in ranges:
        if is_last:
            names.append(f"[{s},{e}]")
        else:
            names.append(f"[{s},{e})")
    fig.barh(list(map(len, c_vals)), names)
    console.print(Panel(fig, highlight=True))

    for i in range(100):
        print(i, answers[i], corrects[i], answers[i] - corrects[i])


@app.command("all")
def analyze_all(seed_start: int = Argument(0), seed_end: int = Argument(None)):
    it = range(seed_start, seed_end) if seed_end is not None else count(seed_start)

    for i in it:
        if not is_exist(i):
            break
        m, eps, n, graphs, answers, corrects, wrongs, score = analyze_seed(i)
        if 0.2 <= eps <= 0.3:
            console.print(i, score, m, eps)


def main():
    app()


if __name__ == "__main__":
    main()
