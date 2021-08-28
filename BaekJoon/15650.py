# N과 M

from itertools import combinations

N, M = map(int, input().split())
lst = [i for i in range(1, N+1)]
lee = list(combinations(lst, M))

for i in lee:
    print(" ".join(map(str, i)))