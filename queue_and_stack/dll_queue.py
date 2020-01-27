
from doubly_linked_list import DoublyLinkedList


class Queue:
    def __init__(self):
        self.size = 0
        # Why is our DLL a good choice to store our elements?
        # self.storage = ?
        self.storage = DoublyLinkedList()

    def enqueue(self, value):
       self.size += 1
       self.storage.add_to_tail(value)
       
    def dequeue(self):
       if self.size is not 0:
            self.size -= 1
            return self.storage.remove_from_head()
       else:
           return
    
    def len(self):
        return self.size

    def peek(self):
        if self.size != 0:
            head_value = self.storage.head.value
            return head_value
        else:
            return 
    def view_queue(self):
        self.storage.get_items()
        

Q = Queue()
Q.enqueue(4)
Q.enqueue(4)
Q.enqueue(4)
print(Q.view_queue())