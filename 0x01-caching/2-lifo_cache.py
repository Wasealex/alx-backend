#!/usr/bin/python3
""" LIFO Caching """
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """ LIFO Cache class """
    def __init__(self):
        """ Initiliaze
        """
        super().__init__()

    def put(self, key, item):
        """ Add an item in the cache
        """
        if key is None or item is None:
            return
        self.cache_data[key] = item
        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            discarded_key = next(reversed(self.cache_data))
            del self.cache_data[discarded_key]
            print(f"DISCARD: {discarded_key}\n")

    def get(self, key):
        """ Get an item by key
        """
        if key is None or key not in self.cache_data:
            return None
        return self.cache_data[key]
