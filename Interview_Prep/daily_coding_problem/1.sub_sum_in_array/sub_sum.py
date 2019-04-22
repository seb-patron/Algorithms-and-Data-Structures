import unittest
import sys
from pathlib import Path

def sub_sum_in_list(nums: 'List[int]', target: 'int') -> 'List[int]':
    hashmap = {}

    for num in nums:
        match = target - num
        if match in hashmap:
            return True

        else:
            hashmap[num] = True

    return False
   


class TestTwoSum(unittest.TestCase):
    
    def test_one(self):
        self.assertEqual(sub_sum_in_list(nums=[2,7,11,15], target=9), True)

    def test_two(self):
        self.assertEqual(sub_sum_in_list(nums=[3, 2, 4], target=6), True)

    def test_three(self):
        self.assertEqual(sub_sum_in_list(nums=[3,2,3], target=6), True)

    def test_four(self):
        self.assertEqual(sub_sum_in_list(nums=[3,2,3], target=8), False)

    def test_five(self):
        self.assertEqual(sub_sum_in_list(nums=[7,11,15], target=6), False)

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