from itertools import pairwise
from pathlib import Path


def is_exist(seed: int):
    return Path(f"./score/{seed:04}.txt").is_file()


def rm_score(seed: int):
    Path(f"./score/{seed:04}.txt").unlink()


def count_seps(
    seps: list[int], values: list[int]
) -> tuple[list[tuple[int, int, bool]], list[list[int]]]:
    # O(len(value) log len(seps)) に出来るけど、そこまで大きなデータではないので気にしない
    ranges = []
    c_vals = []
    for i, (s, e) in enumerate(pairwise(seps)):
        assert s <= e
        is_last = i == len(seps) - 2
        ranges.append((s, e, is_last))
        c_vals.append([])
        for v in values:
            if s <= v < e or (is_last and v == e):
                c_vals[-1].append(v)

    return ranges, c_vals
