from typer import Typer

import tools.py.run as run_
from tools.py.console import console

app = Typer()


@app.command()
def run(seed: int, verbose: bool = False):
    score = run_.run(seed, verbose)
    console.print(f"score: {score}")


@app.command()
def mrun(seed_start: int, seed_end: int, multi_process: bool = True):
    score_sum, score_avg = run_.multi_run(range(seed_start, seed_end), multi_process)
    console.print(f"score_sum: {score_sum}, score_avg: {score_avg}")


def main():
    app()


if __name__ == "__main__":
    main()
