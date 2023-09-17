from collections import Counter, defaultdict, deque, namedtuple
from functools import reduce
import string
from typing import List, Optional


class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:

        n = len(graph)

        vis = set()

        msk = (1 << n) - 1

        Node = namedtuple('Node', ('node', 'mask', 'cost'))

        q = deque()

        ans = float('inf')

        for i in range(n):
            no = Node(i, (1 << i), 1)
            q.append(no)

            vis.add((i, (1 << i)))

        while q:
            nn = q.popleft()

            if msk == nn.mask:
                return nn.cost - 1

            else:
                for adj in graph[nn.node]:
                    nm = nn.mask | 1 << adj

                    if (adj, nm) not in vis:
                        q.append(Node(adj, nm, nn.cost + 1))
                        vis.add((adj, nm))

        return ans


def main():
    s = Solution()

    ans = s.shortestPathLength(graph=[[1, 2, 3], [0], [0], [0]])

    print(ans)


main()


def solve():

    mod = 1_000_000_007

    n = int(input())
    arr = list(map(int, input().strip().split()))[:n]

    dp = [(0, 0) for _ in range(n + 1)]

    ma = -100001

    for i in range(n + 1):
        dp[i] = (100001, 0)

    for i in range(1, n + 1):
        na, nb = dp[i - 1]
        for j in range(i, n + 1):
            a = min(na, arr[j - 1])
            b = nb + arr[j - 1]
            c = ((-1 * a * b) % mod) * -1 if (a > 0) ^ (b > 0) else a * b % mod

            ma = max(ma,  c)
            na, nb = dp[j]
            dp[j] = (a, b)

    return ma


def main2():
    n = int(input())
    for _ in range(n):
        ans = solve()
        print(ans)


# main2()
