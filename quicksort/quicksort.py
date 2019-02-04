import unittest
import sys
from pathlib import Path
import unittest
import sys
from pathlib import Path


def sort(arr):
    return quicksort(arr, 0, len(arr)-1)

def quicksort(arr, left, right):

    if left < right: 

        pivot = partition(arr, left, right)

        left_arr = quicksort( arr, left, pivot-1 )
        right_arr = quicksort( arr, pivot+1, right)

    return arr

def choose_pivot(arr):
    return len(arr)

def partition(arr, left, right):
    pivot = arr[right]

    i = left - 1

    for j in range(left, right):

        if arr[j] <= pivot:
            i+=1
            arr[j], arr[i] = arr[i], arr[j]
            # i+=1

    arr[right], arr[i+1] = arr[i+1], arr[right]

    return i+1




class TestQuicksort(unittest.TestCase):
    
    def test_one(self):
        self.assertListEqual( sort([1,2,3,4,5]), [1,2,3,4,5] )

    def test_two(self):
        self.assertListEqual( sort([5,4,3,2,1]), [1,2,3,4,5] )

    def test_three(self):
        self.assertListEqual( sort([10, 80, 30, 90, 40, 50, 70]), [10, 30, 40, 50, 70, 80, 90] )

    def test_four(self):
        self.assertListEqual( sort([10,0,30,-50,1]), [-50,0,1,10,30] )


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


