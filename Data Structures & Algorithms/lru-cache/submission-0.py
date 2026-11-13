class Node:

    def __init__(self, key:int, val:int):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None



class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.hash = {}

        self.old = Node(0,0)
        self.new = Node(0,0)

        self.old.next = self.new
        self.new.prev = self.old

    def remove(self, node):
        prev_node = node.prev
        next_node = node.next

        prev_node.next = next_node
        next_node.prev = prev_node
    
    def insert(self, node):
        new_node = self.new.prev
        self.new.prev = node
        node.next = self.new
        node.prev = new_node
        new_node.next = node



    def get(self, key: int) -> int:
        if key not in self.hash:
            return -1

        curr = self.hash[key]
        self.remove(curr)
        self.insert(curr)
        
        return curr.val
        

    def put(self, key: int, value: int) -> None:
        if key in self.hash:
            self.remove(self.hash[key])

        self.hash[key] = Node(key,value)
        self.insert(self.hash[key])

        if len(self.hash) > self.cap:
            old = self.old.next
            self.remove(old)
            del self.hash[old.key]
