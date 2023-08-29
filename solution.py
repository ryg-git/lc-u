from collections import Counter
from functools import reduce
from typing import List


class Solution:
    def bestClosingTime(self, customers: str) -> int:
        cnt = 0
        
        for c in customers:
            cnt += 1 if c == 'Y' else -1
        
        mcnt = cnt
        ct = len(customers)
        
        for i, c in enumerate(reversed(customers)):
            cnt -= 1 if c == 'Y' else -1
            
            if cnt >= mcnt:
                ct = len(customers) - i - 1
                mcnt = cnt
        
        return ct


def main():
    s = Solution()
    ans = s.bestClosingTime(customers = "YYYY")
    print(ans)


main()
