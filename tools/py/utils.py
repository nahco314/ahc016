from pathlib import Path


def is_exist(seed: int):
    return Path(f"./score/{seed:04}.txt").is_file()


def rm_score(seed: int):
    Path(f"./score/{seed:04}.txt").unlink()
