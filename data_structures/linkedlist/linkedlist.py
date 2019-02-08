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

    def search(self, data):
        current_node = self.head

        # while there are still nodes and we have not found our node...
        while current_node is not None:
            if current_node.get_data() == data:
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


linked_list = LinkedList()
linked_list.insert(1)
linked_list.insert(2)
linked_list.insert(3)

print (linked_list.search(1).get_data())
linked_list.print_list()
print (linked_list.size)
linked_list.delete(2)
linked_list.print_list()
print (linked_list.size)