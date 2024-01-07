class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.hash_map = dict()

    # Time complexity: O(1)
    def get(self, key: int) -> int:
        if key not in self.hash_map:
            return -1

        value = self.hash_map.pop(key)
        self.hash_map[key] = value
        return value

    # Time complexity: O(1)
    def put(self, key: int, value: int) -> None:
        if key in self.hash_map:
            self.hash_map.pop(key)
        else:
            """
            iter(self.hash_map): This creates an iterator for the keys of the dictionary.
            next(iter(self.hash_map)): This retrieves the first key from the iterator. 
                                        In Python 3.7 and later, dictionaries maintain insertion order,
                                        so the first key would be the oldest or least recently used key.
            """

            if len(self.hash_map) == self.capacity:
                del self.hash_map[next(iter(self.hash_map))]
        self.hash_map[key] = value


# Your LRUCache object will be instantiated and called as such:

lRUCache = LRUCache(2)
lRUCache.put(1, 1)
lRUCache.put(2, 2)
lRUCache.get(1)
lRUCache.put(3, 3)
lRUCache.get(2)
lRUCache.put(4, 4)
lRUCache.get(1)
lRUCache.get(3)
lRUCache.get(4)