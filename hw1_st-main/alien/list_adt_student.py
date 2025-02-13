def create_list(size):
    """
    Creates a deque-like data structure with a fixed-size list.

    Parameters:
    - size: The fixed size of the deque.

    Returns:
    A dictionary representing the deque:
    {
        'size': size,    # Fixed size of the deque
        'data': [None] * size,    # List to store elements
        'n': 0,    # Number of elements in the deque
        'i': 0    # Index for circular storage of elements
    }
    """


def is_empty(listADT):
    """
    Checks if the deque is empty.

    Parameters:
    - listADT: The deque data structure.

    Returns:
    True if the deque is empty, False otherwise.
    """


def is_full(listADT):
    """
    Checks if the deque is full.

    Parameters:
    - listADT: The deque data structure.

    Returns:
    True if the deque is full, False otherwise.
    """


def get(i, listADT):
    """
    Gets the element at the specified index in the deque.

    Parameters:
    - i: The index of the element to retrieve.
    - listADT: The deque data structure.

    Returns:
    The element at the specified index.
    """


def set(i, e, listADT):
    """
    Sets the element at the specified index in the deque.

    Parameters:
    - i: The index of the element to set.
    - e: The element to be set.
    - listADT: The deque data structure.
    """


def length(listADT):
    """
    Gets the number of elements in the deque.

    Parameters:
    - listADT: The deque data structure.

    Returns:
    The number of elements in the deque.
    """


def add(i, e, listADT):
    """
    Adds an element at the specified index in the deque.

    Parameters:
    - i: The index at which to add the element.
    - e: The element to be added.
    - listADT: The deque data structure.
    """


def remove(i, listADT):
    """
    Removes the element at the specified index in the deque.

    Parameters:
    - i: The index of the element to remove.
    - listADT: The deque data structure.
    """


def insert_last(e, listADT):
    """
    Inserts an element at the last position in the deque.

    Parameters:
    - e: The element to be inserted.
    - listADT: The deque data structure.
    """


def remove_last(listADT):
    """
    Removes the last element from the deque.

    Parameters:
    - listADT: The deque data structure.
    """


def insert_first(e, listADT):
    """
    Inserts an element at the first position in the deque.

    Parameters:
    - e: The element to be inserted.
    - listADT: The deque data structure.
    """


def remove_first(listADT):
    """
    Removes the first element from the deque.

    Parameters:
    - listADT: The deque data structure.
    """


def get_first(listADT):
    """
    Gets the first element from the deque.

    Parameters:
    - listADT: The deque data structure.

    Returns:
    The first element in the deque.
    """


def get_last(listADT):
    """
    Gets the last element from the deque.

    Parameters:
    - listADT: The deque data structure.

    Returns:
    The last element in the deque.
    """
