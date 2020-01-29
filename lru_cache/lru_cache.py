from doubly_linked_list import DoublyLinkedList


class Node:
    def __init__(self, key, val):
        # keep track of key for later use;
        # given only a Node, we are able to
        # delete it from a node_map (see LRUCache)
        self.key = key
        self.val = val
        self.next = None
        self.prev = None
class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    def __init__(self, limit=10):
        self.storage = {}
        self.limit = limit
        self.size = 0
        self.order = DoublyLinkedList()
        self.head = None
        self.tail = None

       
    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        if key in self.storage:
            self.use_node(self.storage[key])
            return self.storage[key].val
        else:
            return None

        

    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """
    def set(self, key, value):
        if key in self.storage:
            self.use_node(self.storage[key])
            self.storage[key].val = value
        else:
            # insert new node
            node = Node(key, value)
            self.storage[key] = node

            # first node is special case: its the head and the tail
            if self.size == 0:
                self.head = node
                self.tail = node

            if self.size < self.limit:
                self.size += 1

            # size at max capacity; must remove tail (least recent) node
            elif self.size == self.limit:
                k = self.tail.key # preserve current tail key

                if self.size == 1:
                    # special case; replace only node left,
                    # so it becomes the head and the tail
                    self.head = node
                    self.tail = node
                else:
                    # normal case, just adjust the tail position
                    self.tail = self.tail.prev
                    self.tail.next = None

                # delete old tail
                del self.storage[k]

            self.use_node(node)

    def use_node(self, node):
        """
        put a Node in the head (most recent) position;
        can be a new node, or node that is already stored
        """

        # head Node is already in most recent position,
        # so no work to do when we use it
        if node is self.head: return

        # connect nodes neighbors (one could be None);
        # if node is new, there are no neighbors to connect
        if node.next: node.next.prev = node.prev
        if node.prev: node.prev.next = node.next

        # when using the tail, we must set a new tail
        if node is self.tail:
            # node still points to original tail, so we
            # are fine overwriting the tail pointer.
            # new tail's next is be set to None in the above
            # condition, since the original tail's next was None
            self.tail = self.tail.prev

        # update head Node connections
        self.head.prev = node
        node.next = self.head
        node.prev = None
        self.head = node

        
        
        
 

        

 
        