'''input

'''
import sys
import math
import bisect
from sys import stdin, stdout
from math import gcd, floor, sqrt, log
from collections import defaultdict as dd
from bisect import bisect_left as bl, bisect_right as br

sys.setrecursionlimit(100000000)


def inp(): return int(input())
def strng(): return input().strip()


def jn(x, l): return x.join(map(str, l))
def strl(): return list(input().strip())


def mul(): return map(int, input().strip().split())
def mulf(): return map(float, input().strip().split())
def seq(): return list(map(int, input().strip().split()))


def ceil(x): return int(x) if (x == int(x)) else int(x)+1
def ceildiv(x, d): return x//d if (x % d == 0) else x//d+1


def flush(): return stdout.flush()
def stdstr(): return stdin.readline()
def stdint(): return int(stdin.readline())


def stdpr(x): return stdout.write(str(x))


mod = 1000000007


# main code


class TreeNode:
    def __init__(self, data):
        self.left = None
        self.right = None
        self.val = data

    def PrintTree(self):
        print(self.val)


def poTravel(tn: TreeNode):
    st, po = [], []

    current = tn

    lv = None

    while st or current:
        if current:
            st.append(current)
            current = current.left
        else:
            if st[-1].right and lv != st[-1].right:
                current = st[-1].right
            else:
                nd = st.pop()

                po.append(nd.val)

                lv = nd

    return po


def main():
    r = TreeNode(7)
    r.left = TreeNode(3)
    r.right = TreeNode(6)
    r.left.left = TreeNode(1)
    r.left.right = TreeNode(2)
    r.right.left = TreeNode(4)
    r.right.right = TreeNode(5)

    poTravel(r)


main()
