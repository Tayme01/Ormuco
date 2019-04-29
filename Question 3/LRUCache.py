import collections


class LRUCache:
    def __init__(self, maximum):
        self.maximum = maximum
        self.cache = collections.OrderedDict()

    def add(self, key, value):
        if len(self.cache) == self.maximum:
            self.cache.popitem(last=True)
            self.cache[key] = value
        else:
            self.cache[key] = value

    def get(self, key):
        if key in self.cache.keys():
            self.cache.move_to_end(key)
            return self.cache[key]
        else:
            return 'Invalid key.'

    def update(self, key, value):
        if key in self.cache.keys():
            self.cache[key] = value
            self.cache.move_to_end(key)
        else:
            print('Invalid key.')