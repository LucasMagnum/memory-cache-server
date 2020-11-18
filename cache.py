class MemoryCache:
    def __init__(self):
        self.cache = {}

    def get(self, key, default=None):
        return self.cache.get(key, default)

    def add(self, key, value):
        self.cache[key] = value

    def delete(self, key):
        del self.cache[key]
