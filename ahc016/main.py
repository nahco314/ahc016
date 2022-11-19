from __future__ import annotations

import statistics
import sys
import time
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

    def disconnect(self, i: int, j: int):
        if i > j:
            i, j = j, i
        self._is_connected[i][j] = False
        self.degrees[i] -= 1
        self.degrees[j] -= 1

    def to_nx_graph(self) -> nx.Graph:
        g = nx.Graph()
        for i in range(self.n):
            g.add_node(i)
        for i in range(self.n):
            for j in range(i + 1, self.n):
                if self.is_connected(i, j):
                    g.add_edge(i, j)
        return g

    def floyd_warshall(self) -> list[list[int]]:
        dist = [[float("inf")] * self.n for _ in range(self.n)]
        for i in range(self.n):
            dist[i][i] = 0
        for i in range(self.n):
            for j in range(i + 1, self.n):
                if self.is_connected(i, j):
                    dist[i][j] = 1
                    dist[j][i] = 1
        for k in range(self.n):
            for i in range(self.n):
                for j in range(self.n):
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])
        return dist

    def adj(self, i: int) -> list[int]:
        return [j for j in range(self.n) if self.is_connected(i, j)]

    def remove(self, i: int) -> Graph:
        g = Graph(self.n - 1)
        for j in range(self.n):
            if j == i:
                continue
            for k in range(j + 1, self.n):
                if k == i:
                    continue
                if self.is_connected(j, k):
                    g.connect(j, k)
        return g

    def is_k_plex(self, k: int, s: list[int]):
        l = len(s)

        s_set = set(s)

        for i in s:
            cnt = 0
            for j in self.adj(i):
                if j in s_set:
                    cnt += 1
            if not l - cnt <= k:
                return False

        return True


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
    def __init__(self, n: int, m: int, eps: float):
        self.n = n
        self.m = m
        self.eps = eps

    def decide_num(self, num: int) -> int:
        return num

    def reconstruction(self, num: int) -> int:
        return num

    def encode(self, num: int) -> Graph:
        raise NotImplementedError

    def decode(self, g: Graph) -> int:
        raise NotImplementedError


class OptimumConverter(ConverterBase):
    def __init__(self, m: int, eps: float):
        n = -1
        for i in range(len(graphs)):
            if len(graphs[i]) >= m:
                n = i
                break
        super().__init__(n, m, eps)

    def encode(self, num: int) -> Graph:
        return graphs[self.n][self.decide_num(num)]

    def decode(self, g: Graph) -> int:
        for i, g2 in enumerate(graphs[self.n]):
            if nx.is_isomorphic(g.to_nx_graph(), g2.to_nx_graph()):
                return min(self.reconstruction(i), self.m - 1)
        assert False, "unreachable"


class Converter(ConverterBase):
    def __init__(self, m: int, eps: float, n_: int = None):
        if eps < 0.2:
            n = m
        else:
            n = 100

        if n_ is not None:
            n = n_

        super().__init__(n, m, eps)

    def decide_num(self, num: int) -> int:
        res = num + (self.n - self.m)
        return res

    def reconstruction(self, num: int) -> int:
        return num - (self.n - self.m)

    def encode(self, num: int) -> Graph:
        g = Graph(self.n)
        ms = self.decide_num(num)

        if ms < self.n // 2:
            for i in range(ms):
                for j in range(i + 1, self.n):
                    g.connect(i, j)
        else:
            for i in range(ms):
                for j in range(i + 1, ms):
                    g.connect(i, j)

        return g

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

            if max(data) < n // 2 and i == 0:
                score = 0

            if score < best_score:
                best_score = score
                best_a = a.copy()
                best_b = b.copy()

            if a:
                b.append(a.pop())

        return best_a, best_b

    def decode(self, g: Graph) -> int:
        print("#", sorted(g.degrees))

        a, b = self.clustering(g.degrees)

        forecast_1 = len(b)

        res = self.reconstruction(forecast_1)
        res = max(min(res, self.m - 1), 0)

        print("#", sorted(self.encode(res).degrees))

        return res


class LowEpsConverter(ConverterBase):
    def __init__(self, m: int, eps: float):
        mn = -1
        for i in range(len(graphs)):
            if len(graphs[i]) >= m:
                mn = i
                break

        self.cnt = 3
        self.mn = mn
        n = self.mn * self.cnt
        super().__init__(n, m, eps)

    def encode(self, num: int) -> Graph:
        res = Graph(self.n)
        for i in range(self.cnt):
            for j in range(self.mn):
                for k in range(j + 1, self.mn):
                    if graphs[self.mn][num].is_connected(j, k):
                        res.connect(i * self.mn + j, i * self.mn + k)
        return res

    def decode(self, g: Graph) -> int:
        return 0


class HighEpsConverter(Converter):
    def __init__(self, m: int, eps: float):
        n = 100
        super().__init__(m, eps, n)

    def decode(self, g: Graph) -> int:
        if max(g.degrees) < self.n // 2:
            return 0

        vs = sorted(range(self.n), key=lambda i: g.degrees[i], reverse=True)
        sss = 0
        ks = vs[:sss]

        k_plex = [0] * self.n

        for i in ks:
            for j in g.adj(i):
                if j < i:
                    continue
                if j in ks:
                    k_plex[i] += 1
                    k_plex[j] += 1

        for it, v in enumerate(vs[sss:]):
            ks.append(v)
            for j in g.adj(v):
                if j in ks:
                    k_plex[v] += 1
                    k_plex[j] += 1

            k = len(ks) // 2 + 2
            is_k_plex = True
            for i in ks:
                if not len(ks) - k_plex[i] <= k:
                    is_k_plex = False
                    break

            if is_k_plex:
                pass
            else:
                ks.pop()

        res = self.reconstruction(len(ks))
        res = max(min(res, self.m - 1), 0)

        return res


def main():
    start_time = time.time()

    m, eps = input().split()
    with open("./raw_input.txt", "w") as f:
        f.write(f"{m} {eps}\n")
    m = int(m)
    eps = float(eps)

    if eps <= 0.02:
        converter = OptimumConverter(m, eps)
    elif eps < 0.1:
        converter = Converter(m, eps)
    elif eps < 0.28:
        converter = Converter(m, eps)
    else:
        converter = HighEpsConverter(m, eps)

    print(converter.n)
    for i in range(converter.m):
        print(converter.encode(i).to_01())

    for i in range(100):
        g_01 = input()
        with open("./raw_input.txt", "a") as f:
            f.write(f"{g_01}\n")
        g = Graph.from_01(converter.n, g_01)
        print(converter.decode(g))

    print(f"elapsed: {time.time() - start_time}", file=sys.stderr)


if __name__ == "__main__":
    main()
