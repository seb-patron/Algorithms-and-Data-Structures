#!/bin/python3

import math
import os
import random
import re
import sys
from pathlib import Path
import unittest

class RepeatedString(unittest.TestCase):
# Complete the repeatedString function below.
    def repeated_string(self, string, n):
        str_length = len(string)
        a_count = string.count('a')
        remainder = str_length - n % str_length

        remainder_count = string.count('a', 0, str_length-remainder)

        if a_count == 0: return 0
        
        ans = (n // str_length)
        ans = (a_count*ans) + remainder_count
        return (ans)


class testRepeatedString(unittest.TestCase):
    
    def test_one(self):
        obj = RepeatedString()
        self.assertEqual(obj.repeated_string(string ='gfcaaaecbg', n=547602), 164280)

    def test_two(self):
        obj = RepeatedString()
        self.assertEqual(obj.repeated_string(string ='epsxyyflvrrrxzvnoenvpegvuonodjoxfwdmcvwctmekpsnamchznsoxaklzjgrqruyzavshfbmuhdwwmpbkwcuomqhiyvuztwvq', n=549382313570), 16481469408)

    def test_three(self):
        obj = RepeatedString()
        self.assertEqual(obj.repeated_string(string ='aba', n=10), 7)

    def test_four(self):
        obj = RepeatedString()
        self.assertEqual(obj.repeated_string(string ='a', n=1000000000000), 1000000000000)


if __name__ == "__main__":
    file = Path(__file__).resolve()
    parent, top = file.parent, file.parents[2]

    sys.path.append(str(top))
    try:
        sys.path.remove(str(parent))
    except ValueError: # Already removed
        pass

    import mergesort.tests
    __package__ = 'repeatedstrings.tests'

    unittest.main()
