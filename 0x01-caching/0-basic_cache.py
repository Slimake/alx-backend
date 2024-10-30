#!/usr/bin/env python3
""" 0-basic_cache module """
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """ Inherit from BaseCaching """
    def __init__(self):
        """ Initialize """
        super().__init__()

    def put(self, key, item):
        """ Add an item in the cache """
        if key is not None:
            self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key """
        value = self.cache_data.get(key)
        if key is not None and value is not None:
            return value
        return None
