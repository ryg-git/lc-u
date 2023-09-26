from collections import Counter, defaultdict, deque, namedtuple
from functools import reduce
import heapq
import string
from typing import List, Optional


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        st = []
        seen = set()

        ls = {c: i for i, c in enumerate(s)}

        for i, c in enumerate(s):
            if c not in seen:
                while st and c < st[-1] and i < ls[st[-1]]:
                    seen.discard(st.pop())
                st.append(c)
                seen.add(c)

        return "".join(st)


def main():
    s = Solution()

    ans = s.removeDuplicateLetters(s="cbacdcbc")

    print(ans)


main()
