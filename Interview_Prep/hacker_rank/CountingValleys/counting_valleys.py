#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
# less efficent solution
# def countingValleys(n, string):
#     count = 1
#     valley_count = 0
#     level = 0
#     for i in range(0, len(string)):
#         if (i+1 < len(string)) and string[i] == string[i+1]:
#             count = count + 1
#         else:
#             temp = level
#             if string[i] == 'U': 
#                 level = level + count
#             elif string[i] == 'D': 
#                 level = level - count
#             if temp >= 0 and level < 0:
#                 valley_count = valley_count + 1
#             count = 1
#     return valley_count

def countingValleys(n, string):
    level= valley = 0
    for i in range(n):
        if string[i] == 'U':
            level+=1
            if level == 0:
                valley +=1
        else:
            level-=1

    return valley

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    s = input()

    result = countingValleys(n, s)

    fptr.write(str(result) + '\n')

    fptr.close()
