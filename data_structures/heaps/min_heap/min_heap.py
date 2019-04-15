import unittest
import sys
from pathlib import Path

class MinIntHeap:
    def __init__(self):
        self.capacity = 10
        self.size = 0
        # self.items = []
        self.items = [0] * self.capacity

    def get_left_child_index(self, parent_index):
        return (2 * parent_index) + 1

    def get_right_child_index(self, parent_index):
        return (2 * parent_index) + 2

    def get_parent_index(self, child_index):
        return (child_index - 1)//2

    def has_left_child(self, index):
        return self.get_left_child_index(index) < self.size

    def has_right_child(self, index):
        return self.get_right_child_index(index) < self.size

    def has_parent(self, index):
        return self.get_parent_index(index) >= 0

    def left_child(self, index):
        return self.items[self.get_left_child_index(index)]
    
    def right_child(self, index):
        return self.items[self.get_right_child_index(index)]

    def parent(self, index):
        return self.items[self.get_parent_index(index)]

    def swap(self, index_one, index_two):
        self.items[index_one], self.items[index_two] = self.items[index_two], self.items[index_one]

    def peek(self):
        if self.size == 0: raise ValueError('could not peek heap as there are no nodes')

        return self.items[0]

    # extract the minimum element (ie remove it from array, replace it with last inserted)
    def poll(self):
        item = self.items[0]
        self.items[0] = self.items[self.size - 1]
        self.size -= 1
        self.heapify_down()
        return item

    def add(self, item):
        self.items[self.size] = item
        self.size += 1
        self.heapify_up()

    def heapify_down(self):
        index = 0
        while (self.has_left_child(index)): # we only need to check if there's a left child, bc if there isn't there is no right child
            smaller_child_index = self.get_left_child_index(index)
            if (self.has_right_child and self.right_child(index) < self.left_child(index)):
                smaller_child_index = self.get_right_child_index(index)

            if self.items[index] < self.items[smaller_child_index]:
                break
            else:
                self.swap(index, smaller_child_index)
            
            index = smaller_child_index

    def heapify_up(self):
        index = self.size - 1 # start at last element added
        while (self.has_parent(index) and self.parent(index) > self.items[index]): # as long as there are parents and heap is out of order...
            self.swap(self.get_parent_index(index), index)
            index = self.get_parent_index(index)




    


class TestMinIntHeap(unittest.TestCase):

    def setup_heap(self):
        heap = MinIntHeap()
        heap.items[0] = 2
        heap.items[1] = 4
        heap.items[2] = 8
        heap.items[3] = 9
        heap.items[4] = 7
        heap.items[5] = 10
        heap.items[6] = 9
        heap.size = 7
        return heap
    
    def test_get_left_child_index_one(self):
        heap = self.setup_heap()
        self.assertEqual(heap.get_left_child_index(0), 1 )

    def test_get_left_child_index_two(self):
        heap = self.setup_heap()
        self.assertEqual(heap.get_left_child_index(2), 5 )

    def test_get_right_child_index_one(self):
        heap = self.setup_heap()
        self.assertEqual(heap.get_right_child_index(0), 2 )

    def test_get_right_child_index_two(self):
        heap = self.setup_heap()
        self.assertEqual(heap.get_right_child_index(2), 6 )

    def test_get_parent_index_one(self):
        heap = self.setup_heap()
        self.assertEqual(heap.get_parent_index(1), 0 )

    def test_get_parent_index_two(self):
        heap = self.setup_heap()
        self.assertEqual(heap.get_parent_index(6), 2 )

    def test_get_parent_index_three(self):
        heap = self.setup_heap()
        self.assertEqual(heap.get_parent_index(7), 3 )

    def test_get_parent_index_three(self):
        heap = self.setup_heap()
        self.assertEqual(heap.get_parent_index(7), 3 )

    def test_left_child_one(self):
        heap = self.setup_heap()
        self.assertEqual(heap.left_child(0), 4 )

    def test_left_child_two(self):
        heap = self.setup_heap()
        self.assertEqual(heap.left_child(2), 10 )

    def test_right_child_one(self):
        heap = self.setup_heap()
        self.assertEqual(heap.right_child(0), 8 )

    def test_right_child_two(self):
        heap = self.setup_heap()
        self.assertEqual(heap.right_child(1), 7 )

    
    def test_parent_one(self):
        heap = self.setup_heap()
        self.assertEqual(heap.parent(1), 2 )

    def test_parent_two(self):
        heap = self.setup_heap()
        self.assertEqual(heap.parent(3), 4 )

    def test_parent_three(self):
        heap = self.setup_heap()
        self.assertEqual(heap.parent(6), 8 )

    def test_swap_one(self):
        heap = self.setup_heap()
        former_item_at_six = heap.items[6]
        heap.swap(6, 2)
        self.assertEqual(heap.items[2], former_item_at_six)

    def test_swap_two(self):
        heap = self.setup_heap()
        former_item_at_two = heap.items[2]
        heap.swap(6, 2)
        self.assertEqual(heap.items[6], former_item_at_two)

    def test_has_parent_one(self):
        heap = self.setup_heap()
        self.assertEqual(heap.has_parent(1), True )

    def test_has_parent_two(self):
        heap = self.setup_heap()
        self.assertEqual(heap.has_parent(6), True )

    def test_has_parent_three(self):
        heap = self.setup_heap()
        self.assertEqual(heap.has_parent(0), False )

    def test_has_left_child_one(self):
        heap = self.setup_heap()
        self.assertEqual(heap.has_left_child(0), True )

    def test_has_left_child_two(self):
        heap = self.setup_heap()
        self.assertEqual(heap.has_left_child(2), True )

    def test_has_left_child_three(self):
        heap = self.setup_heap()
        self.assertEqual(heap.has_left_child(3), False )

    def test_has_left_child_four(self):
        heap = self.setup_heap()
        self.assertEqual(heap.has_left_child(6), False )

    def test_has_right_child_one(self):
        heap = self.setup_heap()
        self.assertEqual(heap.has_right_child(0), True )

    def test_has_right_child_two(self):
        heap = self.setup_heap()
        self.assertEqual(heap.has_right_child(2), True )

    def test_has_right_child_three(self):
        heap = self.setup_heap()
        self.assertEqual(heap.has_right_child(3), False )

    def test_has_right_child_four(self):
        heap = self.setup_heap()
        self.assertEqual(heap.has_right_child(6), False )

    def test_heapify_up_one(self):
        heap = self.setup_heap()
        heap.add(8)
        self.assertEqual(heap.items[7], 9 )

    def test_heapify_up_two(self):
        heap = self.setup_heap()
        heap.add(8)
        self.assertEqual(heap.items[3], 8 )

    def test_heapify_up_three(self):
        heap = self.setup_heap()
        heap.add(8)
        self.assertEqual(heap.items[4], 7 )

    def test_heapify_up_four(self):
        heap = self.setup_heap()
        heap.add(1)
        self.assertEqual(heap.items[0], 1 )

    def test_heapify_up_five(self):
        heap = self.setup_heap()
        heap.add(1)
        self.assertEqual(heap.items[1], 2)

    def test_heapify_up_six(self):
        heap = self.setup_heap()
        heap.add(1)
        self.assertEqual(heap.items[7], 9)

    def test_heapify_down_one(self):
        heap = self.setup_heap()
        heap.add(25)
        heap.poll()
        self.assertEqual(heap.items[0], 4 )

    def test_heapify_down_two(self):
        heap = self.setup_heap()
        heap.add(25)
        heap.poll()
        self.assertEqual(heap.items[4], 25 )

    def test_heapify_down_three(self):
        heap = self.setup_heap()
        heap.add(25)
        heap.poll()
        self.assertEqual(heap.items[1], 7 )

    def test_heapify_down_four(self):
        heap = self.setup_heap()
        heap.add(25)
        heap.poll()
        self.assertEqual(heap.items[2], 8)



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