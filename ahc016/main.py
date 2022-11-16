from __future__ import annotations

import statistics
import sys
from collections import Counter

import networkx as nx


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

    def to_nx_graph(self) -> nx.Graph:
        g = nx.Graph()
        for i in range(self.n):
            g.add_node(i)
        for i in range(self.n):
            for j in range(i + 1, self.n):
                if self.is_connected(i, j):
                    g.add_edge(i, j)
        return g


# 埋め込み最高！
# graphs[i] := 同型なグラフを含まない、すべてのi頂点グラフのリスト
graphs = [
    [
        Graph.from_01(0, ""),
    ],
    [
        Graph.from_01(1, ""),
    ],
    [
        Graph.from_01(2, "0"),
        Graph.from_01(2, "1"),
    ],
    [
        Graph.from_01(3, "000"),
        Graph.from_01(3, "100"),
        Graph.from_01(3, "110"),
        Graph.from_01(3, "111"),
    ],
    [
        Graph.from_01(4, "000000"),
        Graph.from_01(4, "100000"),
        Graph.from_01(4, "110000"),
        Graph.from_01(4, "100001"),
        Graph.from_01(4, "111000"),
        Graph.from_01(4, "110100"),
        Graph.from_01(4, "110010"),
        Graph.from_01(4, "111100"),
        Graph.from_01(4, "110011"),
        Graph.from_01(4, "111110"),
        Graph.from_01(4, "111111"),
    ],
    [
        Graph.from_01(5, "0000000000"),
        Graph.from_01(5, "1000000000"),
        Graph.from_01(5, "1100000000"),
        Graph.from_01(5, "1000000100"),
        Graph.from_01(5, "1110000000"),
        Graph.from_01(5, "1100100000"),
        Graph.from_01(5, "1100010000"),
        Graph.from_01(5, "1100000001"),
        Graph.from_01(5, "1111000000"),
        Graph.from_01(5, "1110100000"),
        Graph.from_01(5, "1110001000"),
        Graph.from_01(5, "1100100001"),
        Graph.from_01(5, "1100010100"),
        Graph.from_01(5, "1100010010"),
        Graph.from_01(5, "1111100000"),
        Graph.from_01(5, "1110110000"),
        Graph.from_01(5, "1110101000"),
        Graph.from_01(5, "1110100001"),
        Graph.from_01(5, "1110001010"),
        Graph.from_01(5, "1100010011"),
        Graph.from_01(5, "1111110000"),
        Graph.from_01(5, "1111100001"),
        Graph.from_01(5, "1110110100"),
        Graph.from_01(5, "1110110010"),
        Graph.from_01(5, "1110101001"),
        Graph.from_01(5, "1110001011"),
        Graph.from_01(5, "1111111000"),
        Graph.from_01(5, "1111110100"),
        Graph.from_01(5, "1111110010"),
        Graph.from_01(5, "1110110011"),
        Graph.from_01(5, "1111111100"),
        Graph.from_01(5, "1111110011"),
        Graph.from_01(5, "1111111110"),
        Graph.from_01(5, "1111111111"),
    ],
    [
        Graph.from_01(6, "000000000000000"),
        Graph.from_01(6, "100000000000000"),
        Graph.from_01(6, "110000000000000"),
        Graph.from_01(6, "100000000100000"),
        Graph.from_01(6, "111000000000000"),
        Graph.from_01(6, "110001000000000"),
        Graph.from_01(6, "110000100000000"),
        Graph.from_01(6, "110000000000100"),
        Graph.from_01(6, "100000000100001"),
        Graph.from_01(6, "111100000000000"),
        Graph.from_01(6, "111001000000000"),
        Graph.from_01(6, "111000010000000"),
        Graph.from_01(6, "111000000000001"),
        Graph.from_01(6, "110001000000100"),
        Graph.from_01(6, "110000100100000"),
        Graph.from_01(6, "110000100010000"),
        Graph.from_01(6, "110000100000001"),
        Graph.from_01(6, "110000000000110"),
        Graph.from_01(6, "111110000000000"),
        Graph.from_01(6, "111101000000000"),
        Graph.from_01(6, "111100001000000"),
        Graph.from_01(6, "111001100000000"),
        Graph.from_01(6, "111001010000000"),
        Graph.from_01(6, "111001000000100"),
        Graph.from_01(6, "111001000000001"),
        Graph.from_01(6, "111000011000000"),
        Graph.from_01(6, "111000010010000"),
        Graph.from_01(6, "111000010001000"),
        Graph.from_01(6, "111000010000001"),
        Graph.from_01(6, "110001000000110"),
        Graph.from_01(6, "110000100100001"),
        Graph.from_01(6, "110000100010100"),
        Graph.from_01(6, "110000100010010"),
        Graph.from_01(6, "111111000000000"),
        Graph.from_01(6, "111101100000000"),
        Graph.from_01(6, "111101001000000"),
        Graph.from_01(6, "111101000000100"),
        Graph.from_01(6, "111101000000010"),
        Graph.from_01(6, "111100001001000"),
        Graph.from_01(6, "111001100100000"),
        Graph.from_01(6, "111001100010000"),
        Graph.from_01(6, "111001100000001"),
        Graph.from_01(6, "111001010001000"),
        Graph.from_01(6, "111001010000100"),
        Graph.from_01(6, "111001010000010"),
        Graph.from_01(6, "111001000000110"),
        Graph.from_01(6, "111001000000101"),
        Graph.from_01(6, "111000011010000"),
        Graph.from_01(6, "111000010010100"),
        Graph.from_01(6, "111000010010010"),
        Graph.from_01(6, "111000010010001"),
        Graph.from_01(6, "111000010001001"),
        Graph.from_01(6, "110001000000111"),
        Graph.from_01(6, "110000100010011"),
        Graph.from_01(6, "111111100000000"),
        Graph.from_01(6, "111111000000100"),
        Graph.from_01(6, "111101110000000"),
        Graph.from_01(6, "111101101000000"),
        Graph.from_01(6, "111101100100000"),
        Graph.from_01(6, "111101100010000"),
        Graph.from_01(6, "111101100001000"),
        Graph.from_01(6, "111101100000001"),
        Graph.from_01(6, "111101001001000"),
        Graph.from_01(6, "111101001000100"),
        Graph.from_01(6, "111101001000010"),
        Graph.from_01(6, "111101000000011"),
        Graph.from_01(6, "111100001001010"),
        Graph.from_01(6, "111001100100001"),
        Graph.from_01(6, "111001100010100"),
        Graph.from_01(6, "111001100010010"),
        Graph.from_01(6, "111001100010001"),
        Graph.from_01(6, "111001010001100"),
        Graph.from_01(6, "111001010000110"),
        Graph.from_01(6, "111001010000011"),
        Graph.from_01(6, "111001000000111"),
        Graph.from_01(6, "111000011011000"),
        Graph.from_01(6, "111000011010010"),
        Graph.from_01(6, "111000010010011"),
        Graph.from_01(6, "111111110000000"),
        Graph.from_01(6, "111111100100000"),
        Graph.from_01(6, "111111100010000"),
        Graph.from_01(6, "111111100000001"),
        Graph.from_01(6, "111101110100000"),
        Graph.from_01(6, "111101110001000"),
        Graph.from_01(6, "111101101100000"),
        Graph.from_01(6, "111101101010000"),
        Graph.from_01(6, "111101101000001"),
        Graph.from_01(6, "111101100100001"),
        Graph.from_01(6, "111101100010100"),
        Graph.from_01(6, "111101100010010"),
        Graph.from_01(6, "111101100001010"),
        Graph.from_01(6, "111101100001001"),
        Graph.from_01(6, "111101001001100"),
        Graph.from_01(6, "111101001001010"),
        Graph.from_01(6, "111101001000110"),
        Graph.from_01(6, "111101001000011"),
        Graph.from_01(6, "111100001001011"),
        Graph.from_01(6, "111001100010101"),
        Graph.from_01(6, "111001100010011"),
        Graph.from_01(6, "111001010001110"),
        Graph.from_01(6, "111001010000111"),
        Graph.from_01(6, "111000011011100"),
        Graph.from_01(6, "111111111000000"),
        Graph.from_01(6, "111111110100000"),
        Graph.from_01(6, "111111110001000"),
        Graph.from_01(6, "111111100100001"),
        Graph.from_01(6, "111111100010100"),
        Graph.from_01(6, "111111100010010"),
        Graph.from_01(6, "111101110110000"),
        Graph.from_01(6, "111101110101000"),
        Graph.from_01(6, "111101110100001"),
        Graph.from_01(6, "111101110001010"),
        Graph.from_01(6, "111101101100001"),
        Graph.from_01(6, "111101101011000"),
        Graph.from_01(6, "111101101010100"),
        Graph.from_01(6, "111101101010010"),
        Graph.from_01(6, "111101101010001"),
        Graph.from_01(6, "111101100010011"),
        Graph.from_01(6, "111101100001011"),
        Graph.from_01(6, "111101001001110"),
        Graph.from_01(6, "111101001001011"),
        Graph.from_01(6, "111001010001111"),
        Graph.from_01(6, "111000011011110"),
        Graph.from_01(6, "111111111100000"),
        Graph.from_01(6, "111111110110000"),
        Graph.from_01(6, "111111110101000"),
        Graph.from_01(6, "111111110100001"),
        Graph.from_01(6, "111111110001010"),
        Graph.from_01(6, "111111100010011"),
        Graph.from_01(6, "111101110110100"),
        Graph.from_01(6, "111101110110010"),
        Graph.from_01(6, "111101110101010"),
        Graph.from_01(6, "111101110101001"),
        Graph.from_01(6, "111101110001011"),
        Graph.from_01(6, "111101101011100"),
        Graph.from_01(6, "111101101010101"),
        Graph.from_01(6, "111101101010011"),
        Graph.from_01(6, "111101001001111"),
        Graph.from_01(6, "111111111110000"),
        Graph.from_01(6, "111111111100001"),
        Graph.from_01(6, "111111110110100"),
        Graph.from_01(6, "111111110110010"),
        Graph.from_01(6, "111111110101001"),
        Graph.from_01(6, "111111110001011"),
        Graph.from_01(6, "111101110110011"),
        Graph.from_01(6, "111101110101011"),
        Graph.from_01(6, "111101101011110"),
        Graph.from_01(6, "111111111111000"),
        Graph.from_01(6, "111111111110100"),
        Graph.from_01(6, "111111111110010"),
        Graph.from_01(6, "111111110110011"),
        Graph.from_01(6, "111101101011111"),
        Graph.from_01(6, "111111111111100"),
        Graph.from_01(6, "111111111110011"),
        Graph.from_01(6, "111111111111110"),
        Graph.from_01(6, "111111111111111"),
    ],
]


class ConverterBase:
    def encode(self, n: int, m: int, eps: float, num: int) -> Graph:
        raise NotImplementedError

    def decode(self, n: int, m: int, eps: float, g: Graph) -> int:
        raise NotImplementedError


class Converter(ConverterBase):
    def encode(self, n: int, m: int, eps: float, num: int) -> Graph:
        return graphs[n][num]

    def decode(self, n: int, m: int, eps: float, g: Graph) -> int:
        for i, g2 in enumerate(graphs[n]):
            if nx.is_isomorphic(g.to_nx_graph(), g2.to_nx_graph()):
                return min(i, m - 1)
        assert False, "unreachable"


class WeakConverter(ConverterBase):
    def encode(self, n: int, m: int, eps: float, num: int) -> Graph:
        g = Graph(n)
        ms = num + (n - m)
        for i in range(ms):
            for j in range(i + 1, ms):
                g.connect(i, j)

        if ms < n // 2:
            missing = n // 2 - ms
            p = 0
            for i in range(ms):
                for j in range(missing):
                    g.connect(i, ms + p)
                    p += 1
                    p %= n - ms

        return g

    def calc_diff(self, n: int, m: int, eps: float, num: int, d_c: Counter[int]):
        zero_cnt = n
        p_cnt = 0
        if num != 0:
            zero_cnt -= num + 1
            p_cnt += num + 1

        e_lst = [0] * zero_cnt + [num + 1] * p_cnt

        lst = []
        for i in range(n):
            lst.extend([i] * d_c[i])

        res = 0
        for i, j in zip(lst, e_lst):
            res += abs(i - j) ** 3

        return res

    def clustering(self, data: list[int]) -> tuple[list[int], list[int]]:
        data = sorted(data)
        n = len(data)
        a = data.copy()
        b = []

        best_score = 10**10
        best_a = []
        best_b = []

        for i in range(n + 1):
            score = 0
            a_center = statistics.mean(a) if a else 0
            for j in range(n - i):
                score += abs(a[j] - a_center) ** 2
            b_center = statistics.mean(b) if b else 0
            for j in range(i):
                score += abs(b[j - i] - b_center) ** 2
            if score < best_score:
                best_score = score
                best_a = a.copy()
                best_b = b.copy()
            if a:
                b.append(a.pop())

        return best_a, best_b

    def decode(self, n: int, m: int, eps: float, g: Graph) -> int:
        a, b = self.clustering(g.degrees)
        return max(min(len(b) - (n - m), m - 1), 0)


def main():
    m, eps = input().split()
    with open("./raw_input.txt", "w") as f:
        f.write(f"{m} {eps}\n")
    m = int(m)
    eps = float(eps)

    if eps <= 0.05:
        n = -1
        for i in range(len(graphs)):
            if len(graphs[i]) >= m:
                n = i
                break

        converter = Converter()
    else:
        if eps < 0.2:
            n = min(round(m * 2), 100)
        else:
            n = 100

        converter = WeakConverter()

    print(n)
    for i in range(m):
        print(converter.encode(n, m, eps, i).to_01())

    for i in range(100):
        g_01 = input()
        with open("./raw_input.txt", "a") as f:
            f.write(f"{g_01}\n")
        g = Graph.from_01(n, g_01)
        print(converter.decode(n, m, eps, g))


if __name__ == "__main__":
    main()
