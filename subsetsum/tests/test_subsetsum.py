import unittest
import sys
from pathlib import Path




class TestSubsetsum(unittest.TestCase):
    
    def test_one(self):
        from .. import subsetsum
        self.assertListEqual( subsetsum.Subsetsum([1,2,3,4,5]).subsetsum(6), [1, 2, 3] )

    def test_two(self):
        from .. import subsetsum
        self.assertListEqual( subsetsum.Subsetsum([3, 34, 4, 12, 5, 2]).subsetsum(9), [3, 4, 2] )



if __name__ == "__main__":
    file = Path(__file__).resolve()
    parent, top = file.parent, file.parents[2]

    sys.path.append(str(top))
    try:
        sys.path.remove(str(parent))
    except ValueError: # Already removed
        pass

    import subsetsum.tests
    __package__ = 'subsetsum.tests'

    unittest.main()


