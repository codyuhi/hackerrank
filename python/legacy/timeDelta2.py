#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the time_delta function below.

def defineMonth(strMonth):
    if strMonth == "Jan":
        return 1
    elif strMonth == "Feb":
        return 2
    elif strMonth == "Mar":
        return 3
    elif strMonth == "Apr":
        return 4
    elif strMonth == "May":
        return 5
    elif strMonth == "Jun":
        return 6
    elif strMonth == "Jul":
        return 7
    elif strMonth == "Aug":
        return 8
    elif strMonth == "Sep":
        return 9
    elif strMonth == "Oct":
        return 10
    elif strMonth == "Nov":
        return 11
    elif strMonth == "Dec":
        return 12
    else:
        return 0

def processHours(current, timeZone):
    currentH = int(current)
    if timeZone[0] == '+':
        currentH -= int(timeZone[1:3])
    elif timeZone[0] == '-':
        currentH += int(timeZone[1:3])
    return currentH

def processMinutes(current, sign, timeZone):
    currentM = int(current)
    if sign == '+':
        currentM -= int(timeZone)
    elif sign == '-':
        currentM += int(timeZone)
    return currentM

def time_delta(t1,t2):
    t1List = t1.split()
    t2List = t2.split()
    totalDays = int(t1List[1]) - int(t2List[1])
    totalDays *= 86400
    totalMonths = int(defineMonth(t1List[2])) - int(defineMonth(t2List[2]))
    totalMonths *= 2628000
    totalYears = int(t1List[3]) - int(t2List[3])
    totalYears *= 31536000
    totalHours = int(processHours(
        t1List[4][0:2], t1List[5][0:3]) - int(processHours(t2List[4][0:2], t2List[5][0:3])))
    totalHours *= 3600
    totalMinutes = int(processMinutes(
        t1List[4][3:5], t1List[5][0], t1List[5][3:5]) - int(processMinutes(t2List[4][3:5], t2List[5][0], t2List[5][3:5])))
    totalMinutes *= 60
    totalSeconds = int(t1List[4][6:8]) - int(t2List[4][6:8])
    total = totalDays + totalMonths + totalYears + totalHours + totalMinutes + totalSeconds
    return str(abs(total))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()
