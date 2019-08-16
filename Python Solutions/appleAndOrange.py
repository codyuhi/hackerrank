#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    acount = 0
    bcount = 0
    for i in range(len(apples)):
        apples[i] += a
        if apples[i] >= s and apples[i] <= t:
            acount += 1
    for i in range(len(oranges)):
        oranges[i] += b
        if oranges[i] >= s and oranges[i] <= t:
            bcount += 1
    print(acount)
    print(bcount)

if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
