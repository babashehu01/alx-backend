#!/usr/bin/env python3
"""Simple helper function"""

from typing import Tuple


def index_range(page, page_size) -> Tuple[int, int]:
    """
    Returns a tuple containing the start index and
    end index corresponding to the range of indexes to return
    in a list for the given pagination parameters.

    Args:
        page (int): The current page number (1-indexed).
        page_size (int): The number of items to display per page.

    Returns:
        tuple: A tuple containing the start index
              (inclusive) and end index (exclusive).
    """
    start_index: int = page * page_size
    end_index: int = start_index - page_size

    return (end_index, start_index)
