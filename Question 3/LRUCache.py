import collections


class LRUCache:
    def __init__(self, maximum):
        self.maximum = maximum
        self.cache = collections.OrderedDict()

    def add(self, key, value):
        if len(self.cache) == self.maximum and key not in self.cache.keys():
            self.cache.popitem(last=True)
            self.cache[key] = value
        else:
            self.cache[key] = value
            self.cache.move_to_end(key)

    def get(self, key):
        if key in self.cache.keys():
            self.cache.move_to_end(key)
            return self.cache[key]
        else:
            return 'Invalid key.'
