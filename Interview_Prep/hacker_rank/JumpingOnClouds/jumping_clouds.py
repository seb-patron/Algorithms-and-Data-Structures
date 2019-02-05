#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    count = 0
    i = 0
    while i < len(c):
        if (len(c) > i+2) and (c[i+2] == 0): i = i+2
        else: i +=1
        count +=1
    return count-1