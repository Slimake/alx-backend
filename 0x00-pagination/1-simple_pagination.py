#!/usr/bin/env python3
"""0-simple_helper_function"""
import csv
import math
from typing import Tuple, List


class Server:
    """Server class to paginate a database of popular baby names.
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]
        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        assert type(page) is int
        assert type(page_size) is int
        assert page > 0
        assert page_size > 0
        self.dataset()
        if page >= len(self.__dataset) or page_size >= len(self.__dataset):
            return []
        start_idx, end_idx = index_range(page, page_size)
        return self.__dataset[start_idx:end_idx]


def index_range(page: int, page_size: int) -> Tuple:
    """
    return a tuple of size two containing a start index
    and an end index corresponding to the range of indexes
    to return in a list for those particular pagination parameters.
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)