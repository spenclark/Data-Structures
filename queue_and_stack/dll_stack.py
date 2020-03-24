import sys
from doubly_linked_list import DoublyLinkedList
sys.path.append('../doubly_linked_list')


class Stack:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        # self.storage = ?
        self.storage = DoublyLinkedList()

    # add value to head
    def push(self, value):
        self.storage.add_to_head(value)

    # remove value from head
    def pop(self):
        if not self.storage.head:
            return
        return self.storage.remove_from_head()

    # return len
    def len(self):
        return self.storage.length
