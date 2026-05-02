class Node:
    def __init__(self, key, val):
        self.key,self.val = key, val
        self.prev = self.next = None
    
class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}

        self.head,self.tail = Node(0,0),Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head
    
    #head - > 1 -> 2 -> 3 -> 4 -> tail
    def _remove(self, node: Node):
        node_prev, node_next = node.prev, node.next
        #removing / snapping
        node_prev.next = node_next
        node_next.prev = node_prev

    def _insert(self, node: Node):
        temp_next = self.head.next
        self.head.next = node
        node.next = temp_next
        node.prev = self.head
        node.next.prev = node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self._remove(self.cache[key])
        self._insert(self.cache[key])
        return self.cache[key].val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._remove(self.cache[key])
        self.cache[key] = Node(key, value)
        self._insert(self.cache[key])
        if len(self.cache) > self.cap:
            LRU = self.tail.prev
            self._remove(LRU)
            del self.cache[LRU.key]



        
