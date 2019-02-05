import unittest
import sys
from pathlib import Path

def firstNotRepeatingCharacter(s):
    # a=0, b=1,..., etc
    char_list = [0] * 26
    
    char_sequence = []

    # a = 97. To get it to equal 0, we need to subtract 97
    conversion_const = 97
    
    
    
    for i in s:
        char_list[ord(i) - conversion_const] +=1
        
        if char_list[ord(i) - conversion_const] == 1:
            char_sequence.append(i)
            
    for i in char_sequence:
        if char_list[ord(i) - conversion_const] == 1:
            return i
        
    return '_'


class TestFirstNonRepeating(unittest.TestCase):
    
    def test_one(self):
        self.assertEqual( firstNotRepeatingCharacter('abacabad'), 'c' )

    def test_two(self):
        self.assertEqual( firstNotRepeatingCharacter('abacabaabacaba'), '_' )

    def test_three(self):
        self.assertEqual( firstNotRepeatingCharacter('z'), 'z' )

    def test_four(self):
        self.assertEqual( firstNotRepeatingCharacter('bcb'), 'c' )

    def test_five(self):
        self.assertEqual( firstNotRepeatingCharacter('ngrhhqbhnsipkcoqjyviikvxbxyphsnjpdxkhtadltsuxbfbrkof'), 'g' )



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