# Design an LRU (Least Recently Used) cache with O(1) time complexity for both read and write operations.

# Start by defining a Node class to represent a node in the doubly linked list. Each node will contain a key-value pair and references to the previous and next nodes in the list.

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

# Next, define the LRUCache class, which will implement the cache functionality.


class LRUCache:
    # Initialize the cache with the specified capacity and create the head and tail sentinel nodes for the doubly linked list.
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.head = Node(None, None)
        self.tail = Node(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head

    # Checks if the key exists in the cache. If it does, we retrieve the node, move it to the head of the list (since it's now the most recently used), and return its value. Otherwise, we return -1 to indicate that the key doesn't exist.
    def get(self, key):
        if key in self.cache:
            node = self.cache[key]
            self._move_to_head(node)
            return node.value
        else:
            return -1

    def put(self, key, value):  # First checks if the key already exists in the cache. If it does, we update the value, move the corresponding node to the head (as it's now the most recently used item), and update the cache accordingly. If the key doesn't exist, we check if the cache is full. If it is, we remove the least recently used item (the tail) from both the linked list and the cache. Then, we create a new node with the key and value, add it to the head of the list, and update the cache.
        if key in self.cache:
            node = self.cache[key]
            node.value = value
            self._move_to_head(node)
        else:
            if len(self.cache) == self.capacity:
                self._remove_tail()
            new_node = Node(key, value)
            self.cache[key] = new_node
            self._add_to_head(new_node)

    # Removes a node from its current position in the list and adds it to the head (as the most recently used item).
    def _move_to_head(self, node):
        self._remove_node(node)
        self._add_to_head(node)

    # Removes the tail node (the least recently used item) from both the list and the cache.
    def _remove_tail(self):
        tail_node = self.tail.prev
        self._remove_node(tail_node)
        del self.cache[tail_node.key]

    def _remove_node(self, node):  # Removes a given node from the list.
        node.prev.next = node.next
        node.next.prev = node.prev

    def _add_to_head(self, node):  # Adds a node to the head of the list.
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node
