"""
This class implements a very simple Least Recently Used (LRU) cache.

The cache stores key-value pairs in a list.
The most recently used item is kept at the end of the list.
When the cache is full, the least recently used item is removed.
"""

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = []   

    def get(self, key):
        for i in range(len(self.cache)):
            if self.cache[i][0] == key:
                value = self.cache[i][1]
                self.cache.pop(i)        
                self.cache.append((key, value))  
                return value
        return -1

    def put(self, key, value):
        for i in range(len(self.cache)):
            if self.cache[i][0] == key:
                self.cache.pop(i)        
                break

        if len(self.cache) == self.capacity:
            self.cache.pop(0)            

        self.cache.append((key, value)) 
