#!/usr/bin/env python3
"""4-mru_cache module """
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """ Inherit from BaseCaching """
    def __init__(self):
        """ Initialize """
        super().__init__()
        self.stack = []

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.stack.remove(key)
        elif len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            # Remove the most recently used item (LRU)
            recent_key = self.stack.pop()
            del self.cache_data[recent_key]
            print("DISCARD: {}".format(recent_key))

        self.cache_data[key] = item
        self.stack.append(key)

    def get(self, key):
        """ Get an item by key """
        if key is not None and key in self.cache_data:
            self.stack.remove(key)
            self.stack.append(key)
            return self.cache_data.get(key)
        return None
