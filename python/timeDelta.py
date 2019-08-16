#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the time_delta function below.
negHours = [int(0)]
negMins = [int(0)]

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
    #fptr.write("current is initially " + str(current) + "\n")
    #fptr.write("timeZone is initially " + str(timeZone) + "\n")
    currentH = int(current)
    if timeZone[0] == '+':
        currentH -= int(timeZone[1:3])
        if currentH < 0:
            negHours[0] = currentH
            currentH = 0
    elif timeZone[0] == '-':
        currentH += int(timeZone[1:3])
    #fptr.write("currentH is " + str(currentH) + "\n")
    return currentH

def processMinutes(current, sign, timeZone):
    #print(current)
    currentM = int(current)
    if sign == '+':
        negMins[0] = int("-"+timeZone)
    elif sign == '-':
        currentM += int(timeZone)
    return currentM

def time_delta(t1, t2):
    t1List = t1.split()
    t2List = t2.split()
    totalDays = abs(int(t1List[1]) - int(t2List[1]))
    totalMonths = abs(int(defineMonth(t1List[2])) - int(defineMonth(t2List[2])))
    totalYears = abs(int(t1List[3]) - int(t2List[3]))
    totalHours = abs(int(processHours(t1List[4][0:2], t1List[5][0:3]) - int(processHours(t2List[4][0:2], t2List[5][0:3]))))
    #fptr.write("totalHours is " + str(totalHours) + "\n")
    #fptr.write(t1List[5][3:5] + "\n")
    totalMinutes = abs(int(processMinutes(
        t1List[4][3:5], t1List[5][0], t1List[5][3:5]) - int(processMinutes(t2List[4][3:5], t2List[5][0], t2List[5][3:5]))))
    totalMinutes += negMins[0]
    totalSeconds = 0
    #fptr.write(str(t1List))
    # fptr.write("totalDays is " + str(totalDays) + "\n")
    # fptr.write("totalMonths is " + str(totalMonths) + "\n")
    # fptr.write("totalYears is " + str(totalYears) + "\n")
    # fptr.write("totalHours is " + str(totalHours) + "\n")
    #fptr.write("totalMinutes is " + str(totalMinutes) + "\n")
    #fptr.write("negMins is " + str(negMins[0]) + "\n")
    # fptr.write("totalSeconds is " + str(totalSeconds) + "\n")
    return str((totalDays * 86400) + (totalMonths * 2628000) + (totalYears * 31536000) + (totalHours * 3600) + (totalMinutes * 60) + totalSeconds)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()
    
# failed:
# in:
# 100
# Fri 11 Feb 2078 00: 05: 21 + 0400
# Mon 29 Dec 2064 03: 33: 48 - 1100
# Wed 12 May 2269 23: 22: 15 - 0500
# Tue 05 Oct 2269 02: 12: 07 - 0200
# Sat 14 Sep 2126 00: 36: 44 + 1400
# Wed 22 Jun 2050 23: 18: 57 - 0100
# Sat 17 Sep 2107 18: 52: 42 + 0530
# Wed 24 Apr 2199 15: 00: 11 - 0900
# Sat 24 Aug 2080 00: 35: 31 + 1030
# Mon 12 Jan 1998 01: 22: 02 - 0700
# Thu 16 Jul 2026 06: 28: 56 - 0930
# Sun 20 Apr 2149 00: 02: 39 - 0400
# Sat 09 Jun 1979 12: 33: 03 + 0200
# Sat 28 Dec 2120 16: 55: 13 + 0500
# Thu 19 Sep 2199 10: 47: 49 + 0330
# Sun 15 May 2016 02: 21: 14 + 0630
# Sun 23 Nov 2110 22: 33: 19 - 1100
# Sun 22 Oct 2141 05: 14: 53 + 1100
# Tue 03 Mar 2065 08: 11: 36 - 0700

# out:
# 413962293
# 12527392
# 2405413067
# 2890723049
# 2607054209
# 3873960223
# 4467057730
# 5785903595
# 975400894
# 3088568718
# 4984873852
# 4910960543
# 6255495019
# 1155677269
# 1948516117
# 6085008512
# 7347800726
# 1284474337
# 3877627387
# 402560892
