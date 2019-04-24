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

        output = []
        output.append(root.val)
        
        # BFS using a deque as a queue
        # Add each root to the queue
        # then explore children, adding them to the queue and to the output list
        # once all children were explored, pop next item in queue and use it as current root 

        
        while queue: # while queue is not empty
            current_node = queue.pop()
            
            if current_node.left != None:
                queue.appendleft(current_node.left)
                output.append(current_node.left.val)
            else:
                output.append(None)
                output.append(None)
                continue

            if current_node.right != None:
                queue.appendleft(current_node.right)
                output.append(current_node.right.val)


        # trim remaining Nones from output since we know that they are right children
        # and we don't need to explicitly state that
        for i in range (len(output)-1, -1, -1):
            if output[i] == None:
                del output[-1]
            else: 
                return "[" + ",".join(str(x) for x in output) + "]"

        return "[" + ",".join(str(x) for x in output) + "]"
        
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        ls = data[1:-1].split(",") # convert string to list
        queue = collections.deque()
        current_node = TreeNode(int(ls.pop(0)))
        root = current_node
        queue.appendleft(current_node)

        while queue and len(ls) > 0:

            left = (ls.pop(0))
            if left is None:
                left = int(left)
                current_node.left = TreeNode(left)
                queue.appendleft(current_node.left)
            if len(ls) > 0:
                right = ls.pop(0)
                if right is None:
                    right = int(right)
                    current_node.right = TreeNode(right)
                    queue.appendleft(current_node.right)

            current_node = queue.pop()

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
        self.assertEqual( c.serialize(root), "[1,2,3,None,None,4,5]" )

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
        print (root.val, type(root))
        print (root.right.left)
        self.assertEqual( root.left.val, 2 )

    def test_six(self):
        root = self.setup_binary_tree()
        c = Codec()
        self.assertEqual( c.deserialize(c.serialize(root)).val, 1 )

    def test_seven(self):
        ls = "[1,2]"
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