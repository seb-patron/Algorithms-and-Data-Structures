import unittest
import sys
from pathlib import Path
import collections

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """

        # use deque since it is practically the same for purposes
        # appendleft() == add to que
        # pop() is same
        queue = collections.deque()
        queue.appendleft(root)

        string = ""
        
        # BFS using a deque as a queue
        # Add each root to the queue
        # then explore children, adding them to the queue and to the output list
        # once all children were explored, pop next item in queue and use it as current root 
        while queue: # while queue is not empty
            current_node = queue.popleft()

            if not current_node:
                string += "None,"
                continue
            else:
                string +=  str(current_node.val) + ","
                queue.append(current_node.left)
                queue.append(current_node.right)

        return string.rstrip(",")

        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        data = collections.deque(data.split(",")) # convert string to list
        val = data.popleft()
        root = None if val == "None" else TreeNode(int(val))

        queue = collections.deque()
        queue.appendleft(root)

        while queue and len(data) > 0:


            current_node = queue.popleft()

            if current_node:

                left = data.popleft()
                current_node.left = TreeNode(int(left)) if left != "None" else None
                queue.append(current_node.left)

                if len(data) > 0:
                    right = data.popleft()
                    current_node.right = TreeNode(int(right)) if right != "None" else None
                    queue.append(current_node.right)

        return root
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))


class TestSerializeBinaryTree(unittest.TestCase):

    def setup_binary_tree(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)
        root.right.left = TreeNode(4)
        root.right.right = TreeNode(5)
        
        return root

    def setup_binary_tree_2(self):
        root = TreeNode(1)
        root.left = TreeNode(2)
        
        return root
    
    def test_one(self):
        root = self.setup_binary_tree()
        c = Codec()
        self.assertEqual( c.serialize(root), "1,2,3,None,None,4,5,None,None,None,None" )

    def test_two(self):
        root = self.setup_binary_tree()
        c = Codec()
        serialized_tree = c.serialize(root)
        self.assertEqual( c.deserialize(serialized_tree).val, 1 )

    def test_three(self):
        root = self.setup_binary_tree()
        c = Codec()
        serialized_tree = c.serialize(root)
        root = c.deserialize(serialized_tree)
        left = root.left
        self.assertEqual( left.val, 2 )

    def test_four(self):
        root = self.setup_binary_tree()
        c = Codec()
        serialized_tree = c.serialize(root)
        root = c.deserialize(serialized_tree)
        right = root.right
        self.assertEqual( right.val, 3 )

    def test_five(self):
        root = self.setup_binary_tree()
        c = Codec()
        serialized_tree = c.serialize(root)
        root = c.deserialize(serialized_tree)
        right = root.right
        self.assertEqual( right.right.val, 5 )

    def test_six(self):
        root = self.setup_binary_tree()
        c = Codec()
        self.assertEqual( c.deserialize(c.serialize(root)).val, 1 )

    def test_seven(self):
        ls = "1,2"
        c = Codec()
        self.assertEqual( c.deserialize(ls).val, 1 )

    # def test_eight(self):
    #     root = self.setup_binary_tree_2()
    #     c = Codec()
    #     print (c.serialize(root))

if __name__ == "__main__":
    file = Path(__file__).resolve()
    parent, top = file.parent, file.parents[2]

    sys.path.append(str(top))
    try:
        sys.path.remove(str(parent))
    except ValueError: # Already removed
        pass

    __package__ = 'minheap.tests'

    unittest.main()