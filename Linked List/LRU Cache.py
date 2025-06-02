class Node:
    def __init__(self):
        self.next = None
        self.previous = None
        self.value = -1
        self.key = -1
        
class LRUCache:
    def __init__(self, capacity: int):
        self.maxCapacity = capacity
        self.recent = None
        self.old = None
        self.cache = {}

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        self.update(key)

        return self.cache[key].value

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key].value = value
            self.cache[key].key = key
            self.update(key)
            return None
        
        if len(self.cache) == self.maxCapacity:
            self.cache.pop(self.old.key)

            if self.maxCapacity > 1:
                self.old.next.previous = None
                self.old = self.old.next

        node = Node()
        node.value = value
        node.key = key

        if len(self.cache) == 0:
            self.old = node
            self.recent = node
            self.cache[key] = node

            return None

        node.previous = self.recent
        self.recent.next = node
        self.recent = node
        self.cache[key] = node

    def update(self, key):
        node = self.cache[key]

        if node == self.recent:
            return

        if node == self.old:
            self.old = node.next
        else:
            node.previous.next = node.next
        node.next.previous = node.previous

        node.previous = self.recent
        node.next = None
        self.recent.next = node
        self.recent = node
