from collections import Counter, defaultdict, deque, namedtuple
from functools import reduce
import heapq
import string
from typing import List, Optional


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        si = 0
        ti = 0
        
        while si < len(s) and ti < len(t):
            if s[si] == t[ti]:
                si += 1
                ti += 1
            else:
                ti += 1
        
        return si == len(s)


def main():
    s = Solution()

    ans = s.isSubsequence(s = "abc", t = "ahbgdc")

    print(ans)


main()


def solve():
    n, m, d = [int(x) for x in input().split()]
    s = list(map(int, input().split()))

    po = 0

    e = 1

    sel = 0

    for i in range(1, n + 1):
        if po < m and s[po] < e:
            e = s[po] + d - 1
            if po < m - 1:
                po += 1
            sel += 1
        if e == i:
            e += d - 1

    return d


def main2():
    # n = int(input())
    n = 1
    for _ in range(n):
        ans = solve()
        print(ans)


# main2()
