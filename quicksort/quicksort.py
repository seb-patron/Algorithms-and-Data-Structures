import unittest
import sys
from pathlib import Path
import unittest
import sys
from pathlib import Path

def quicksort(arr):
    if len(arr) <= 1: return arr

    pivot = choose_pivot(arr)

    arr, pivot = partition(arr, pivot, len(arr))
    length = len(arr)


    left_arr = quicksort( arr[: pivot] )
    right_arr = quicksort( arr[pivot : ] )

    return left_arr + right_arr

def choose_pivot(arr):
    return 0

def partition(arr, left, right):
    pivot = arr[left]

    i = left + 1

    for j in range(left+1, right):

        if arr[j] < pivot:
            arr[j], arr[i] = arr[i], arr[j]
            i+=1

    arr[left], arr[i-1] = arr[i-1], arr[left]

    return arr, i




class TestQuicksort(unittest.TestCase):
    
    def test_one(self):
        self.assertListEqual( quicksort([1,2,3,4,5]), [1,2,3,4,5] )

    def test_two(self):
        self.assertListEqual( quicksort([5,4,3,2,1]), [1,2,3,4,5] )

    def test_three(self):
        self.assertListEqual( quicksort([10, 80, 30, 90, 40, 50, 70]), [10, 30, 40, 50, 70, 80, 90] )

    def test_four(self):
        self.assertListEqual( quicksort([10,0,30,-50,1]), [-50,0,1,10,30] )


if __name__ == "__main__":
    file = Path(__file__).resolve()
    parent, top = file.parent, file.parents[2]

    sys.path.append(str(top))
    try:
        sys.path.remove(str(parent))
    except ValueError: # Already removed
        pass

    __package__ = 'quick.tests'

    unittest.main()


