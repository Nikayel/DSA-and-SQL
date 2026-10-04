
class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        #rightSide = MRU
        self.left = Node(0,0)
        self.right = Node(0,0)
        self.left.next = self.right
        self.right.prev = self.left
    def get(self, key: int) -> int:
        #if item not found:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.remove(node)
        self.insert(node)
        return node.value
    #1->2->3
    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
    def insert(self, node):
        #1->2->3->4 -> right
        MRU = self.right.prev 
        self.right.prev = node
        node.next = self.right
        MRU.next = node
        node.prev = MRU

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            self.remove(node)
            del self.cache[key]
        node = Node(key,value)
        self.insert(node)
        self.cache[key] = node
        if len(self.cache) > self.capacity:
            LRU = self.left.next
            self.remove(LRU)
            del self.cache[LRU.key]