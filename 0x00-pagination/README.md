# ALX Backend Curriculum - Pagination Project

This repository contains the solutions for the Pagination project in the ALX Backend curriculum. The project covers concepts related to pagination, hypermedia metadata, and deletion-resilient pagination. The project is divided into three tasks, and each task involves implementing different functions and classes related to pagination.

## Task 0: Simple Helper Function

This task involves writing a simple helper function called `index_range`. The function takes two integer arguments, `page` and `page_size`, and returns a tuple containing the start index and end index corresponding to the range of indexes to return in a list for those particular pagination parameters.

## Task 1: Simple Pagination

In this task, you need to implement a class named `Server`, which is used to paginate a database of popular baby names. The class contains a method called `get_page`, which takes two integer arguments, `page` and `page_size`, and returns the appropriate page of the dataset based on the provided parameters. The class also includes a helper method called `dataset`, which retrieves the dataset from a CSV file.

## Task 2: Hypermedia Pagination

For this task, you will enhance the `Server` class from Task 1 by adding a method called `get_hyper`. The `get_hyper` method returns a dictionary containing various hypermedia metadata related to the pagination. The metadata includes the page size, current page number, data for the current page, the number of the next page, the number of the previous page, and the total number of pages in the dataset.

## Task 3: Deletion-Resilient Hypermedia Pagination

In the final task, you will further extend the `Server` class to implement deletion-resilient hypermedia pagination. The goal is to ensure that if certain rows are removed from the dataset between two queries, the user does not miss items from the dataset when changing pages. You will implement a new method called `get_hyper_index`, which takes an additional argument `index`. The method returns a dictionary with metadata similar to `get_hyper`, but it handles the case when rows are deleted from the dataset between queries.

## Getting Started

To run and test the code, you need Python 3.7+ and the `pycodestyle` package installed. Clone this repository and navigate to the respective task directories to find the Python files for each task.

```bash
# Clone the repository
git clone https://github.com/babashehu01/alx-backend.git
cd alx-backend/0x00-pagination

# Run the tests for Task 0
python 0-main.py

# Run the tests for Task 1
python 1-main.py

# Run the tests for Task 2
python 2-main.py

# Run the tests for Task 3
python 3-main.py
