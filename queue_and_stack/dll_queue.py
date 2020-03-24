from doubly_linked_list import DoublyLinkedList
import sys
sys.path.append('../doubly_linked_list')


class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        # self.storage = ?
        self.storage = DoublyLinkedList()

    # need to set new value to head
    def enqueue(self, value):
        self.storage.add_to_head(value)

    # remove and return an item from the front of the
    def dequeue(self):
        if not self.storage.head:
            return
        return self.storage.remove_from_tail()

    # returns the number of items in the queue.
    def len(self):
        return self.storage.length
