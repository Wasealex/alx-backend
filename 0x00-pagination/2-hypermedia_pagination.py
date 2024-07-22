#!/usr/bin/env python3
"""
a module that contains a class Server that will paginate a database
of popular baby names using the dataset Popular_Baby_Names.csv
"""
import csv
import math
from typing import List, Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Return a tuple of size two containing a start index
    and an end index
    """
    start_index = (page - 1) * page_size
    end_index = page * page_size
    return (start_index, end_index)


class Server:
    """
    Server class to paginate a database of popular baby names
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """
        Returns the dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE, 'r') as f:
                reader = csv.reader(f)
                self.__dataset = [row for row in reader]
        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Finds the correct indexes to paginate the dataset correctly
        and return the appropriate page of the dataset
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        indexes = index_range(page, page_size)
        start_index = indexes[0]
        end_index = indexes[1]
        return self.dataset()[start_index:end_index]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Finds the correct indexes to paginate the dataset correctly
        and return the appropriate page of the dataset
        """
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        indexes = index_range(page, page_size)
        start_index = indexes[0]
        end_index = indexes[1]
        total_pages = math.ceil(len(self.dataset()) / page_size)
        data = self.dataset()[start_index:end_index]
        return {
            'page_size': len(data),
            'page': page,
            'data': data,
            'next_page': page + 1 if page + 1 < total_pages else None,
            'prev_page': page - 1 if page > 1 else None,
            'total_pages': total_pages
        }
