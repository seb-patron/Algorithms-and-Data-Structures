import unittest
import sys
from pathlib import Path




class TestMergesort(unittest.TestCase):
    
    def test_one(self):
        from .. import mergesort
        self.assertListEqual( mergesort.Merge([1,2,3,4,5]).sort(), [1,2,3,4,5] )

    def test_two(self):
        from .. import mergesort
        self.assertListEqual( mergesort.Merge([5,4,3,2,1]).sort(), [1,2,3,4,5] )

    def test_three(self):
        from .. import mergesort
        self.assertListEqual( mergesort.Merge([1,2,3,4,5]).sort(), [1,2,3,4,5] )

    def test_four(self):
        from .. import mergesort
        self.assertListEqual( mergesort.Merge([10,0,30,-50,1]).sort(), [-50,0,1,10,30] )


if __name__ == "__main__":
    file = Path(__file__).resolve()
    parent, top = file.parent, file.parents[2]

    sys.path.append(str(top))
    try:
        sys.path.remove(str(parent))
    except ValueError: # Already removed
        pass

    import mergesort.tests
    __package__ = 'mergesort.tests'

    unittest.main()


