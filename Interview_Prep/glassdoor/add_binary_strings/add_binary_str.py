import unittest
import sys
from pathlib import Path

# Given two binary strings, write a function that adds them . 
# You are not allowed to use any built in string to int 
# conversions or parsing tools. E.g. Given "100" and "111" 
# you should return "1011". What is the time and space 
# complexity of your algorithm?


# We transverse each element in the longest string
# Runtime O(n) = n

# Both strings are set to the length of the longest string, so n + n
# End string is length n
# Space Complexity O(n) = 3n = n

def add_binary(str1, str2):
    str1, str2 = normalize_binary_str_length(str1, str2)
    result = ''
    carry = 0

    # work backwards
    for i in range(len(str1)-1, -1, -1):
        if str1[i] == '1':
            carry += 1
        if str2[i] == '1':
            carry += 1

        # if carry = 0 or 2, result is a 0
        if carry % 2 == 0:
            result = '0' + result
        # else carry = 1 or 3 (ie previously we added two 1's and carried over the result), result is 1
        else:
            result = '1' + result

        # adjust the carry for the operation we did
        # if carry is 0 or 1, we have nothing to carry to the next iteration, so reset carry to 0
        # else if we have a carry > 2, we have a digit to carry, so carry is set to 1 to account for this
        carry = 0 if carry < 2 else 1

    if carry !=0 : result = '1' + result 
    return result


# make strings equal length for easier transversing
def normalize_binary_str_length(str1, str2):
    if len(str1) == len(str2): return str1, str2
    elif len(str1) > len(str2):
        str2 = ('0' * (len(str1)-len(str2))) + str2
    else:
        str1 = ('0' * (len(str2)-len(str1))) + str1
    return str1, str2


# print (add_binary('100', '111'))


class TestBinaryStringAdd(unittest.TestCase):
    
    def test_one(self):
        self.assertEqual( add_binary('100', '111'), '1011' )

    def test_two(self):
        self.assertEqual( add_binary('1', '11001100'), '11001101' )

    def test_three(self):
        self.assertEqual( add_binary('10101010', '11001100'), '101110110' )

    def test_four(self):
        self.assertEqual( add_binary('10101010', '10101010'), '101010100' )

    def test_five(self):
        self.assertEqual( add_binary('111111', '111111'), '1111110' )



if __name__ == "__main__":
    file = Path(__file__).resolve()
    parent, top = file.parent, file.parents[2]

    sys.path.append(str(top))
    try:
        sys.path.remove(str(parent))
    except ValueError: # Already removed
        pass

    __package__ = 'firstnonrepatingtests.tests'

    unittest.main()