import unittest
import sys
from pathlib import Path

class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_next_node(self, next_node=None):
        self.next_node = next_node

class LinkedList:
    def __init__(self, head=None):
        self.head = None
        self.size = 1 if head is not None else 0

    def insert(self, data):
        new_node = Node(data)
        new_node.set_next_node(self.head)
        self.head = new_node
        self.size += 1

    # searches for specific value in the linkedlist
    def search(self, data):
        current_node = self.head

        # while there are still nodes and we have not found our node...
        while current_node is not None:
            if current_node.get_data() == data:
                return current_node
            else:
                current_node = current_node.get_next()

        return None #we didnt find our value

    def value_at(self, n):
        current_node = self.head

        # while there are still nodes and we have not found our node...
        for i in range(0, n):
            if i == n-1:
                return current_node
            else:
                current_node = current_node.get_next()

        return None #we didnt find our value


    # The delete method traverses the list in the same way that 
    # search does, but in addition to keeping track of the current 
    # node, the delete method also remembers the last node it visited. 
    # When delete finally arrives at the node it wants to delete, 
    # it simply removes that node from the chain by “leap frogging” it.
    def delete(self, data):
        current_node = self.head
        previous_node = None

        # while there are still nodes and we have not found our node...
        while current_node is not None:
            if current_node.get_data() == data:
                previous_node.set_next_node(current_node.get_next())
                del current_node
                self.size -=1
                return 
            elif current_node.get_next() is not None:
                previous_node = current_node
                current_node = current_node.get_next()
                continue
            else:
                return None #we didnt find out value

    def print_list(self):
        current_node = self.head

        # while there are still nodes and we have not found our node...
        while current_node is not None:
            print(current_node, current_node.get_data())
            current_node = current_node.get_next()


class TestBinaryStringAdd(unittest.TestCase):

    def setup_list(self):
        linked_list = LinkedList()
        linked_list.insert('1')
        linked_list.insert('2')
        linked_list.insert('3')
        return linked_list
    
    def test_one(self):
        linked_list = self.setup_list()
        self.assertEqual(linked_list.value_at(1).get_data(), '3' )

    def test_two(self):
        linked_list = self.setup_list()
        self.assertEqual(linked_list.value_at(2).get_data(), '2' )

    def test_three(self):
        linked_list = self.setup_list()
        self.assertEqual(linked_list.value_at(3).get_data(), '1' )
    
    def test_four(self):
        linked_list = self.setup_list()
        self.assertEqual(linked_list.size, 3 )

    def test_five(self):
        linked_list = self.setup_list()
        linked_list.delete(2)
        self.assertEqual(linked_list.value_at(1).get_data(), '3' )

    def test_six(self):
        linked_list = self.setup_list()
        linked_list.delete('2')
        self.assertEqual(linked_list.value_at(2).get_data(), '1' )

    def test_seven(self):
        linked_list = self.setup_list()
        linked_list.delete('2')
        self.assertEqual(linked_list.size, 2 )



if __name__ == "__main__":
    file = Path(__file__).resolve()
    parent, top = file.parent, file.parents[2]

    sys.path.append(str(top))
    try:
        sys.path.remove(str(parent))
    except ValueError: # Already removed
        pass

    __package__ = 'linkedlist.tests'

    unittest.main()