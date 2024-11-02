#!/usr/bin/env python3
"""3-lru_cache module """
from base_caching import BaseCaching
from collections import OrderedDict


class LRUCache(BaseCaching):
    """ Inherit from BaseCaching """
    def __init__(self):
        """ Initialize """
        super().__init__()
        self.cache_data = OrderedDict()

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data.move_to_end(key)

        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            # Remove the least recently used item (LRU)
            first_key = self.cache_data.popitem(last=False)[0]
            print("DISCARD: {}".format(first_key))

    def get(self, key):
        """ Get an item by key """
        if key is not None and key in self.cache_data:
            self.cache_data.move_to_end(key)
            return self.cache_data.get(key)
        return None
