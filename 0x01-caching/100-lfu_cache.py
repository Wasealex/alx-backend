#!/usr/bin/python3
"""LFU Caching"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """LFU Cache class"""
    def __init__(self):
        """
        LFU Cache init
        """
        super().__init__()

    def put(self, key, item):
        """
        Add an item in the cache
        """
        if key is None or item is None:
            return

        if key in self.cache_data:
            self.cache_data[key] = item
            self.update_frequency(key)
        else:
            if len(self.cache_data) >= BaseCaching.MAX_ITEMS:
                self.remove_least_frequent()
            self.cache_data[key] = item

    def get(self, key):
        """
        Get an item by key
        """
        if key is None or key not in self.cache_data:
            return None

        self.update_frequency(key)
        return self.cache_data[key]

    def update_frequency(self, key):
        """
        Update the frequency of a key
        """
        frequency, value = self.cache_data[key]
        self.cache_data[key] = (frequency + 1, value)

    def remove_least_frequent(self):
        """
        Remove the least frequent item
        """
        least_frequent_key = min(
            self.cache_data, key=lambda k: self.cache_data[k][0])
        least_frequent_value = self.cache_data.pop(least_frequent_key)
        print("DISCARD:", least_frequent_key)
