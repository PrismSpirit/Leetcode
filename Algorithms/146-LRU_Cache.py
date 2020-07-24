class LRUCache:
    def __init__(self, capacity: int):
        self.db = dict()
        self.capacity = capacity
        self.time = 0

    def get(self, key: int) -> int:
        if key in self.db:
            self.db[key][1] = self.time
            self.time += 1
            return self.db[key][0]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.db:
            self.db[key] = [value, self.time]
        else:
            if len(self.db.keys()) < self.capacity:
                self.db[key] = [value, self.time]
            else:
                # evict LRU
                evict_key = sorted(self.db.items(), key=lambda x: x[1][1])[0][0]
                del self.db[evict_key]
                self.db[key] = [value, self.time]
        self.time += 1

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)