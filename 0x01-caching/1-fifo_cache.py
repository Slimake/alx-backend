#!/usr/bin/env python3
""" 1-fifo_cache module """
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ Inherit from BaseCaching """
    def __init__(self):
        """ Initialize """
        super().__init__()

    def put(self, key, item):
        """ Add an item in the cache """
        if key is not None and item is not None:
            self.cache_data[key] = item
            if len(self.cache_data) > BaseCaching.MAX_ITEMS:
                first_key = next(iter(self.cache_data))
                print(f"DISCARD: {first_key}")
                self.cache_data.pop(first_key)

    def get(self, key):
        """ Get an item by key """
        if key is not None and key in self.cache_data:
            return self.cache_data.get(key)
        return None