#Min Heap

A Min Heap is a special tree structure in which each parent node is less than or equal to its child node. 

![image of min heap](https://github.com/seb-patron/Algorithms-and-Data-Structures/blob/master/data_structures/heaps/min_heap/Screen%20Shot%202019-04-14%20at%209.42.29%20PM.png)

### Associated Functions:

- heapify : This function converts a regular list to a heap. In the resulting heap the smallest element gets pushed to the index position 0. But rest of the data elements are not necessarily sorted. There are two versions: heapify_up and heapify_down. Each one is used depending on whether the minimum element is removed, or a new element is added.

- poll : Removes the smallest element from the heap, and replaces it with the last added element. Triggers a heapify_down call.

- add : Adds a new element at the last node. Triggers a heapify_up call.