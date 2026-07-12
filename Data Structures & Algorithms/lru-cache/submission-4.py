class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None
class LRUCache:
# head - > {[1:2],[3:1]} -> tail
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head
    def _insert(self,node):
        node.next = self.head.next
        self.head.next.prev = node
        node.prev = self.head
        self.head.next = node
    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
    def get(self, key: int) -> int:
        if key in self.cache:
            self._remove(self.cache[key])
            self._insert(self.cache[key])
            return self.cache[key].val
        else:
            return -1
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._remove(self.cache[key])
        self.cache[key] = Node(key,value)
        self._insert(self.cache[key])
        if len(self.cache) > self.capacity:
            to_remove = self.tail.prev
            self._remove(to_remove)
            del self.cache[to_remove.key]
            
