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
    dequeDict = {"size":size, "data": [None]*size, "n":0, "front":0,"rear":-1}
    return dequeDict


def is_empty(listADT):
    """
    Checks if the deque is empty.

    Parameters:
    - listADT: The deque data structure.

    Returns:
    True if the deque is empty, False otherwise.
    """
    return listADT["n"]==0



def is_full(listADT):
    """
    Checks if the deque is full.

    Parameters:
    - listADT: The deque data structure.

    Returns:
    True if the deque is full, False otherwise.
    """
    return listADT["n"]==listADT["size"]


def get(i, listADT):
    """
    Gets the element at the specified index in the deque.

    Parameters:
    - i: The index of the element to retrieve.
    - listADT: The deque data structure.

    Returns:
    The element at the specified index.
    """
    if i < 0 or i >= listADT["n"]:
        print("Invalid Index")
    else:
        return listADT["data"][(listADT["front"] + i) % listADT["size"]]




def set(i, e, listADT):
    """
    Sets the element at the specified index in the deque.

    Parameters:
    - i: The index of the element to set.
    - e: The element to be set.
    - listADT: The deque data structure.
    """
    if i < 0 or i >= listADT["size"]:
        raise IndexError("Index out of range")
    listADT["data"][ (listADT["front"] + i) % listADT["size"] ] = e


def length(listADT):
    """
    Gets the number of elements in the deque.

    Parameters:
    - listADT: The deque data structure.

    Returns:
    The number of elements in the deque.
    """
    return listADT["n"]
 

def add(i, e, listADT):
    """
    Adds an element at the specified index in the deque.

    Parameters:
    - i: The index at which to add the element.
    - e: The element to be added.
    - listADT: The deque data structure.
    """
    if is_full(listADT):
        raise Exception("Deque is full")
    elif i<0 or i>listADT["size"]:
        raise IndexError("Invalid Index")
    
    for k in range(listADT["n"],i,-1):
        listADT["data"][(listADT["front"] + k) % listADT["size"]] = listADT["data"][(listADT["front"] + (k - 1)) % listADT["size"]]
        
    listADT["data"][(listADT["front"] + i) % listADT["size"]] = e
    listADT["rear"] = (listADT["front"] + listADT["n"] - 1) % listADT["size"]
    listADT["n"] += 1


def remove(i, listADT):
    """
    Removes the element at the specified index in the deque.

    Parameters:
    - i: The index of the element to remove.
    - listADT: The deque data structure.
    """
    if is_empty(listADT):
        raise Exception("Deque is empty")
    if i < 0 or i >= listADT["n"]:
        raise IndexError("Invalid Index")
    removal_index = (listADT["front"]+i)%listADT["size"]
    removed = listADT["data"][removal_index]
    for j in range(i,listADT["n"]-1):
        listADT["data"][(listADT["front"] + j) % listADT["size"]] = listADT["data"][(listADT["front"] + j + 1) % listADT["size"]]
    listADT["data"][(listADT["front"] + listADT["n"] - 1) % listADT["size"]] = None
    listADT["n"] -= 1
    if listADT["n"] == 0:
        listADT["front"] = 0
        listADT["rear"] = -1
    else:
        listADT["rear"] = (listADT["front"] + listADT["n"] - 1) % listADT["size"]
    return removed
    

def insert_last(e, listADT):
    """
    Inserts an element at the last position in the deque.

    Parameters:
    - e: The element to be inserted.
    - listADT: The deque data structure.
    """
    if is_full(listADT):
        raise Exception("Deque is full")
    if is_empty(listADT):
        listADT["front"] = 0
        listADT["rear"] = 0
        listADT["data"][0] = e
        listADT["n"] = 1
    else:
        listADT["rear"] = (listADT["rear"] + 1) % listADT["size"]
        listADT["data"][listADT["rear"]] = e
        listADT["n"] += 1


def remove_last(listADT):
    """
    Removes the last element from the deque.

    Parameters:
    - listADT: The deque data structure.
    """
    if is_empty(listADT):
        raise Exception("Deque is empty")
    removed = listADT["data"][listADT["rear"]]
    listADT["data"][listADT["rear"]] = None
    if listADT["n"] == 1:
        listADT["front"] = 0
        listADT["rear"] = 0
    else:
        listADT["rear"] = (listADT["rear"] - 1) % listADT["size"]
    listADT["n"] -= 1
    return removed


def insert_first(e, listADT):
    """
    Inserts an element at the first position in the deque.

    Parameters:
    - e: The element to be inserted.
    - listADT: The deque data structure.
    """
    if is_full(listADT):
        raise Exception("Deque is full")
    if is_empty(listADT):
        listADT["front"] = 0
        listADT["rear"] = 0
        listADT["data"][0] = e
        listADT["n"] = 1
    else:
        listADT["front"] = (listADT["front"] - 1) % listADT["size"]
        listADT["data"][listADT["front"]] = e
        listADT["n"] += 1


def remove_first(listADT):
    """
    Removes the first element from the deque.

    Parameters:
    - listADT: The deque data structure.
    """
    if is_empty(listADT):
        raise Exception("Deque is empty")
    removed = listADT["data"][listADT["front"]]
    listADT["data"][listADT["front"]] = None
    if listADT["n"] == 1:
        listADT["front"] = 0
        listADT["rear"] = 0
    else:
        listADT["front"] = (listADT["front"] + 1) % listADT["size"]
    listADT["n"] -= 1
    return removed


def get_first(listADT):
    """
    Gets the first element from the deque.

    Parameters:
    - listADT: The deque data structure.

    Returns:
    The first element in the deque.
    """
    if is_empty(listADT):
        raise Exception("Deque is empty")
    return listADT["data"][listADT["front"]]


def get_last(listADT):
    """
    Gets the last element from the deque.

    Parameters:
    - listADT: The deque data structure.

    Returns:
    The last element in the deque.
    """
    if is_empty(listADT):
        raise Exception("Deque is empty")
    return listADT["data"][listADT["rear"]]
