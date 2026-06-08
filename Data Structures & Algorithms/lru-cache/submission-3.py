class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None
class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.cap = capacity

        self.left = Node(0,0)   #LRU least Rec Used
        self.right = Node(0,0) #MRU Most Rec Used

        self.left.next = self.right
        self.right.prev = self.left # left -> right
    def insert(self, node:Node):
        node.next = self.right
        node.prev = self.right.prev
        self.right.prev.next = node
        self.right.prev = node
    def remove(self, node:Node):   #left -> 1 : 5 -> 3 :  9 -> right
        node.prev.next = node.next
        node.next.prev = node.prev

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.remove(self.cache[key])
        self.insert(self.cache[key])
        return self.cache[key].val
    
    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key,value)
        self.insert(self.cache[key])
        if len(self.cache) > self.cap:
            LRU = self.left.next
            self.remove(LRU)
            del self.cache[LRU.key]
            
        #Note -> Make sure no Capacity OverFlow even temporrilly
