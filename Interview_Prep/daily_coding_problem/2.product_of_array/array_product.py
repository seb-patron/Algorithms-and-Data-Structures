import unittest
import sys
from pathlib import Path
import math
from functools import reduce 

def product_of_array_easy(nums: 'List[int]') -> 'List[int]':
    product_list = [reduce((lambda x, y: x * y), nums)] * len(nums) # list of the products

    for i in range(0, len(nums)):
        product_list[i] = product_list[i] / nums[i]

    return product_list

def product_of_array(nums: 'List[int]') -> 'List[int]':
    
    product = 1
    for num in nums:
        product *= num

    product_list = [product] * len(nums) # list of the products


    for i in range(0, len(nums)):
        product_list[i] = product_list[i] / nums[i]

    return product_list
    
def product_of_array_no_division(nums: 'List[int]') -> 'List[int]':

    output = []
    product = 1
    ls_length = len(nums)
    
    # product equals previous array product
    # this makes final product inserted into output the product of the array except itself
    for i in range(0, ls_length):
        output.append(product)
        product = product * nums[i]

    # Our last element in output is correct. Now we just need to go in reverse order and multiply
    # the remaining products in

    product = 1

    for i in range(ls_length-1, -1, -1):
        output[i] = output[i] * product
        product = product * nums[i]

    return output
   


class TestProductOfArray(unittest.TestCase):
    
    def test_one(self):
        self.assertListEqual(product_of_array_easy(nums=[1, 2, 3, 4, 5]), [120, 60, 40, 30, 24])

    def test_two(self):
        self.assertListEqual(product_of_array_easy(nums=[3, 2, 1]), [2, 3, 6])

    def test_three(self):
        self.assertListEqual(product_of_array(nums=[1, 2, 3, 4, 5]), [120, 60, 40, 30, 24])

    def test_four(self):
        self.assertListEqual(product_of_array(nums=[3, 2, 1]), [2, 3, 6])

    def test_five(self):
        self.assertListEqual(product_of_array_no_division(nums=[1, 2, 3, 4, 5]), [120, 60, 40, 30, 24])

    def test_six(self):
        self.assertListEqual(product_of_array_no_division(nums=[3, 2, 1]), [2, 3, 6])



if __name__ == "__main__":
    file = Path(__file__).resolve()
    parent, top = file.parent, file.parents[2]

    sys.path.append(str(top))
    try:
        sys.path.remove(str(parent))
    except ValueError: # Already removed
        pass

    __package__ = 'TestProductOfArray.tests'

    unittest.main()