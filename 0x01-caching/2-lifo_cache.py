#!/usr/bin/env python3
""" 2-lifo_cache module """
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ Inherit from BaseCaching """
    def __init__(self):
        """ Initialize """
        super().__init__()
        self.keys_order = []

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            # Remove the last added item (LIFO)
            last_key = self.keys_order.pop()  # Get the last key
            del self.cache_data[last_key]  # Remove from cache
            print("DISCARD: {}".format(last_key))

        self.keys_order.append(key)

    def get(self, key):
        """ Get an item by key """
        if key is not None and key in self.cache_data:
            return self.cache_data.get(key)
        return None
