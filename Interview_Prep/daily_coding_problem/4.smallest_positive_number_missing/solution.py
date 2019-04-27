import unittest
import sys
from pathlib import Path
import collections
from random import randrange

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class SolutionSorting:
    """
        sorts the array, then iterates through until a missing number is found
        uses quicksort to sort

        runtime: quicksort -> O(n log(n))
                 iterating through sorted array -> O(n)
                 total: O(n log(n) + n) == O(n log(n))

        space complexity: O(1) -> in place sort
    """

    def find_smallest_positive_int(self, nums):
        """Finds the first missing positive integer in list.
        
        :type nums: list
        :rtype: int
        """
        nums = self.quicksort(nums)

        smallest_positive = 1

        for num in nums:
            if num < 1:
                continue
            
            elif smallest_positive  == num:
                smallest_positive += 1
            else:
                return smallest_positive

        return smallest_positive


    def quicksort(self, arr, left=None, right=None):
        if left is None: left = 0
        if right is None: right = len(arr)-1

        if left < right: 

            pivot = self.partition(arr, left, right)

            left_arr = self.quicksort( arr, left, pivot-1 )
            right_arr = self.quicksort( arr, pivot+1, right)

        return arr

    def choose_pivot(self, arr):
        return len(arr)

    def partition(self, arr, left, right):
        pivot = arr[right]

        i = left - 1

        for j in range(left, right):

            if arr[j] <= pivot:
                i+=1
                arr[j], arr[i] = arr[i], arr[j]

        arr[right], arr[i+1] = arr[i+1], arr[right]

        return i+1



class SolutionHashing:
    """
    iterates through array and adds each value into a hashtable
    then iterates through the hashtable, from 1 to the largest number in the array
    until a value not in the array is found. returns that value
    if loop finishes, the largest value + 1 is returned

    # runtime analysis: O(n + n) == O(n)
    # space complexity: O(n) -> creating a hashtable of the same size as the array
    """
    
    def find_smallest_positive_int(self, nums):
        hashtable = {}
        largest_num = 1
        for num in nums:
            if num not in hashtable:
                hashtable[num] = True

            if num > largest_num:
                largest_num = num

        for i in range(1, largest_num):
            if i not in hashtable:
                return i

        return largest_num + 1


class SolutionOptimal:

    def find_smallest_positive_int(self, nums):
        print ("\n\n\ninput nums", nums)
        shift, nums = self.segregate(nums)


        print ("shift", shift, "nums", nums)
        nums = nums[shift:]

        print (nums)

        if len(nums) == 0: return 1
        if len(nums) == 1:
            if nums[0] == 1: return 2
            else: return 1

        largest_num = nums[0]
        for num in nums:
            if num > largest_num:
                largest_num = num


        indexes = [-1] * len(nums)

        for num in nums:
            if num < len(nums) and num > 0:
                indexes[num] = 1

        for index in range(1, len(indexes)):
            if indexes[index] < 1:
                print ("indexes at return", indexes, len(indexes))
                return index

        return len(indexes)


    # puts all non-positive  
    # (0 and negative) numbers on left side of nums 
    # return count of such numbers, new array, and largest number fount
    def segregate(self, nums):
        i = 0
        neg_count = 0
        for j in range (1, len(nums)):
            if nums[j] < 0:
                nums[j], nums[i] = nums[i], nums[j]
                i +=1
                neg_count +=1
        if nums[-2] < 1: neg_count +=1
        return neg_count, nums



class TestFindMissingSmallestPositive(unittest.TestCase):

    # sorting solution tests
    def test_sorting_solution_one(self):
        solution = SolutionSorting()
        self.assertEqual( solution.find_smallest_positive_int([2, 3, 7, 6, 8, -1, -10, 15]), 1 )

    def test_sorting_solution_two(self):
        solution = SolutionSorting()
        self.assertEqual( solution.find_smallest_positive_int([ 2, 3, -7, 6, 8, 1, -10, 15]), 4 )

    def test_sorting_solution_three(self):
        solution = SolutionSorting()
        self.assertEqual( solution.find_smallest_positive_int([3, 4, -1, 1]), 2 )

    def test_sorting_solution_four(self):
        solution = SolutionSorting()
        self.assertEqual( solution.find_smallest_positive_int([1, 2, 0]), 3 )

    # hashing solution tests
    def test_hashing_solution_one(self):
        solution = SolutionHashing()
        self.assertEqual( solution.find_smallest_positive_int([2, 3, 7, 6, 8, -1, -10, 15]), 1 )

    def test_hashing_solution_two(self):
        solution = SolutionHashing()
        self.assertEqual( solution.find_smallest_positive_int([ 2, 3, -7, 6, 8, 1, -10, 15]), 4 )

    def test_hashing_solution_three(self):
        solution = SolutionHashing()
        self.assertEqual( solution.find_smallest_positive_int([3, 4, -1, 1]), 2 )

    def test_hashing_solution_four(self):
        solution = SolutionHashing()
        self.assertEqual( solution.find_smallest_positive_int([1, 2, 0]), 3 )

    def test_optimal_solution_one(self):
        solution = SolutionOptimal()
        self.assertEqual( solution.find_smallest_positive_int([2, 3, 7, 6, 8, -1, -10, 15]), 1 )

    def test_optimal_solution_two(self):
        solution = SolutionOptimal()
        self.assertEqual( solution.find_smallest_positive_int([ 2, 3, -7, 6, 8, 1, -10, 15]), 4 )

    def test_optimal_solution_three(self):
        solution = SolutionOptimal()
        self.assertEqual( solution.find_smallest_positive_int([3, 4, -1, 1]), 2 )

    def test_optimal_solution_four(self):
        solution = SolutionOptimal()
        self.assertEqual( solution.find_smallest_positive_int([1, 2, 0]), 3 )
         
    def test_optimal_solution_five(self):
        solution = SolutionOptimal()
        self.assertEqual( solution.find_smallest_positive_int([-10,-3,-100,-1000,-239,1]), 2)

    def test_optimal_solution_six(self):
        solution = SolutionOptimal()
        self.assertEqual( solution.find_smallest_positive_int([-4,-5,0,-2,-6,-3,-6,8,4,-4]), 1)

    def test_optimal_solution_seven(self):
        solution = SolutionOptimal()
        self.assertEqual( solution.find_smallest_positive_int([1, 0]), 2)

    def test_optimal_solution_eight(self):
        solution = SolutionOptimal()
        self.assertEqual( solution.find_smallest_positive_int([1,1000]), 2)

    def test_optimal_solution_nine(self):
        solution = SolutionOptimal()
        self.assertEqual( solution.find_smallest_positive_int([2, 1]), 3)
        

   

if __name__ == "__main__":
    file = Path(__file__).resolve()
    parent, top = file.parent, file.parents[2]

    sys.path.append(str(top))
    try:
        sys.path.remove(str(parent))
    except ValueError: # Already removed
        pass

    __package__ = 'TestFindMissingSmallestPositive.tests'

    unittest.main()