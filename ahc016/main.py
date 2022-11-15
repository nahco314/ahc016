from __future__ import annotations

import sys
from collections import Counter


class Graph:
    def __init__(self, n: int):
        self.n = n
        self._is_connected = [[False] * n for _ in range(n)]
        self.degrees = [0] * n

    def is_connected(self, i: int, j: int) -> bool:
        if i > j:
            i, j = j, i
        return self._is_connected[i][j]

    def to_01(self) -> str:
        res_lst = []
        for i in range(self.n):
            for j in range(i + 1, self.n):
                if self.is_connected(i, j):
                    c = "1"
                else:
                    c = "0"
                res_lst.append(c)
        return "".join(res_lst)

    @classmethod
    def from_01(self, n: int, str_01: str) -> Graph:
        g = Graph(n)
        ind = 0
        for i in range(n):
            for j in range(i + 1, n):
                if str_01[ind] == "1":
                    g.connect(i, j)
                ind += 1
        return g

    def connect(self, i: int, j: int):
        if i > j:
            i, j = j, i
        self._is_connected[i][j] = True
        self.degrees[i] += 1
        self.degrees[j] += 1


def encode(n: int, m: int, eps: float, num: int) -> Graph:
    return Graph.from_01(n, "1" * num + "0" * (190 - num))


def decode(n: int, m: int, eps: float, g: Graph) -> int:
    return min(sum(g._is_connected, []).count(True), m - 1)


def main():
    m, eps = input().split()
    m = int(m)
    eps = float(eps)

    n = 20
    for n in range(4, 100):
        if n * (n - 1) // 2 >= m:
            break

    print(n)
    for i in range(m):
        print(encode(n, m, eps, i).to_01())

    for i in range(100):
        g_01 = input()
        g = Graph.from_01(n, g_01)
        print(decode(n, m, eps, g))


if __name__ == "__main__":
    main()
