#!/usr/bin/python3
"""LRU Caching"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """LRU Cache class"""
    def __init__(self):
        """Constructor method"""
        super().__init__()

    def put(self, key, item):
        """Add an item in the cache"""
        if key is None or item is None:
            return

        self.cache_data[key] = item

        if len(self.cache_data) > BaseCaching.MAX_ITEMS:
            lru_key = next(iter(self.cache_data))
            del self.cache_data[lru_key]
            print(f"DISCARD: {lru_key}\n")

    def get(self, key):
        """Get an item by key"""
        if key is None or key not in self.cache_data:
            return None

        return self.cache_data[key]
