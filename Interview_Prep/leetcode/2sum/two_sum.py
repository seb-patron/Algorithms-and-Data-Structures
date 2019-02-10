import unittest
import sys
from pathlib import Path

def twoSum(nums: 'List[int]', target: 'int') -> 'List[int]':
    # iterate through list
    # create a hashmap of each element as key, with index as value
    # for each element, subtract current element from target
    # if result in hashmap, return its index plus current index
    hashmap = {}
    for i in range(0, len(nums)):
        complement = target - nums[i]
        if complement in hashmap:
            return [hashmap[complement], i]
        else:
            hashmap[nums[i]] = i


class TestTwoSum(unittest.TestCase):
    
    def test_one(self):
        self.assertListEqual( twoSum(nums=[2,7,11,15], target=9), [0, 1] )

    def test_two(self):
        self.assertListEqual( twoSum(nums=[3, 2, 4], target=6), [1, 2] )

    def test_three(self):
        self.assertListEqual( twoSum(nums=[3,2,3], target=6), [0, 2] )

    # def test_four(self):
    #     self.assertEqual( add_binary('10101010', '10101010'), '101010100' )

    # def test_five(self):
    #     self.assertEqual( add_binary('111111', '111111'), '1111110' )



if __name__ == "__main__":
    file = Path(__file__).resolve()
    parent, top = file.parent, file.parents[2]

    sys.path.append(str(top))
    try:
        sys.path.remove(str(parent))
    except ValueError: # Already removed
        pass

    __package__ = 'TestTwoSum.tests'

    unittest.main()