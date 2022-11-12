import re
import subprocess
import sys
from functools import partial
from multiprocessing import Pool
from multiprocessing import cpu_count
from time import perf_counter

from rich.progress import Progress
from rich.progress import Task
from rich.progress import track

from tools.py.console import console


def run(seed: int, verbose: bool = False) -> int:
    if verbose:
        print("run", seed)

    start = perf_counter()
    res = subprocess.run(
        f"cargo run --release --bin tester python ../ahc016/main.py < ./in/{seed:04}.txt > ./out/{seed:04}.txt",
        shell=True,
        capture_output=True,
    )
    time = perf_counter() - start
    try:
        score = int(
            re.match(
                "Score = (\d+)", res.stderr.decode("utf-8").splitlines()[-1]
            ).group(1)
        )
    except Exception:
        print(res.stderr.decode("utf-8"))

    with open(f"./score/{seed:04}.txt", "w") as f:
        f.write(f"{score}")

    if verbose:
        print("end", seed, time)

        print(res.stderr.decode("utf-8"), file=sys.stderr)
    return score


def multi_run(
    seed_range: range, multi_process=True, verbose: bool = False
) -> tuple[int, float]:
    score_sum = 0

    if multi_process:
        with Progress() as progress:
            task = progress.add_task("Running...", total=len(seed_range))
            with Pool(cpu_count()) as p:
                start = perf_counter()
                results = []

                args = []
                for i in seed_range:
                    args.append(i)

                for result in p.imap(
                    partial(run, verbose=verbose),
                    args,
                ):
                    results.append(result)
                    progress.advance(task)

                score_sum = sum(results)
                time = perf_counter() - start

    else:
        start = perf_counter()
        for seed in track(seed_range):
            score_sum += run(seed, verbose=verbose)
        time = perf_counter() - start

    score_avg = score_sum / len(seed_range)

    return score_sum, score_avg
