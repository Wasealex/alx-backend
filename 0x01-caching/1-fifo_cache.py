#!/usr/bin/python3
""" a module that contains a class FIFOCache
    that inherits from BaseCaching and is a caching system
    using the FIFO algorithm
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """ a class FIFOCache that inherits from BaseCaching
        and is a caching system using the FIFO algorithm
    """
    def __init__(self):
        """ Initiliaze
        """
        super().__init__()

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is None or item is None:
            return

        if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
            first_key = next(iter(self.cache_data))
            del self.cache_data[first_key]
            print("DISCARD:", first_key)

        self.cache_data[key] = item

    def get(self, key):
        """ Get an item by key
        """
        if key is None or key not in self.cache_data:
            return None

        return self.cache_data[key]
