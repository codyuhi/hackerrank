#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    k = int(input())

    sortedKValues = sorted(list(i[k] for i in arr))
    # print(sortedKValues)
    sortArr = []
    for i in sortedKValues:
        for j in range(len(arr)):
            # print(j)
            if i == arr[j][k]:
                sortArr.append(arr[j])
                del arr[j]
                break
    for i in sortArr:
        out = ""
        for j in range(m):
            if j > 0:
                out += " "
            out += str(i[j])
        print(out)