#!/bin/python3

import os
import sys

#
# Complete the timeConversion function below.
#
def timeConversion(s):
    #
    # Write your code here.
    #
    if s[8:] == "PM":
        hours = int(s[:2])
        if hours != 12:
            hours += 12
        s = str(hours) + s[2:8]
        return s
    elif s[:2] == "12":
        s = "00" + s[2:8]
        return s
    else:
        return s[:8]

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    f.write(result + '\n')

    f.close()
