#!/usr/bin/env python3
"""2-hypermedia_pagination"""
import csv
import math
from typing import Tuple, List, Dict


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
        """
        Return the appropriate page of the dataset
        (i.e. the correct list of rows).
        """
        # Validate input
        assert isinstance(page, int) and page > 0
        assert isinstance(page_size, int) and page_size > 0

        # Retrieve the dataset
        dataset = self.dataset()

        # Calculate the indices for pagination
        start_idx, end_idx = index_range(page, page_size)

        # Check if the indices are out of range
        if start_idx >= len(dataset):
            return []

        # Return the page of the dataset
        return dataset[start_idx:end_idx]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """
        Returns a dictionary containing the following key-value pairs
        """
        # Get the current page data
        page_data = self.get_page(page, page_size)

        # Calculate total number of pages
        total_items = len(self.__dataset)
        total_pages = math.ceil(total_items / page_size)

        # Calculate previous and next pages
        previous_page = page - 1 if page > 1 else None
        next_page = page + 1 if page < total_pages else None

        return {
            'page_size': len(page_data),
            'page': page,
            'data': page_data,
            'next_page': next_page,
            'prev_page': previous_page,
            'total_pages': total_pages
        }


def index_range(page: int, page_size: int) -> Tuple:
    """
    Return a tuple of size two containing a start index
    and an end index corresponding to the range of indexes
    to return in a list for those particular pagination parameters.
    """
    start_index = (page - 1) * page_size
    end_index = start_index + page_size
    return (start_index, end_index)
