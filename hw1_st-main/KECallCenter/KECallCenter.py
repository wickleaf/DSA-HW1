# DO NOT CHANGE THIS FUNCTION
# Create a basic queue
def create_queue(size: int) -> dict:
    """
    Description: Creates and initializes a basic queue with a specified size.
    Parameters: size - an integer representing the size of the queue.
    Return: A dictionary representing the initialized queue.
    """
    return {
        "data": [None] * size,  # list of elements
        "front": -1,  # index of the first element in the queue
        "rear": -1,  # index of the last element in the queue
        "n": 0,  # number of elements in the queue
        "size": size,  # size of the queue
    }


# DO NOT CHANGE THIS FUNCTION
# Create Agent Priority Queues
def create_agents_queue(categories: list, sizes: list) -> dict:
    """Description: Creates and initializes a dictionary containing keys as call category
                 and value as a priority queue with a specified size.
                 Each element in the queue is a tuple consisting of data and priority.
    Parameters: categories - list of strings containing call categories ,sizes - list of integers containing the respective size of the priority queue.
    Return: A dictionary representing the initialized priority queue.
    """
    return {category: create_queue(size) for category, size in zip(categories, sizes)}


# Create Call Priority Queues
def create_call_queues(categories, size):
    """Description: Creates and initializes a dictionary containing keys as call categories
                 and value as a priority queue with a specified size.
                 Each element in the queue is a tuple consisting of data and priority.
    Parameters: categories - list of strings containing call categories ,size - integer containing the respective size of the priority queue.
    Return: A dictionary representing the initialized priority queue.
    """
    return {category: create_queue(size) for category in categories}


# Check if the queue is full
def is_full(queue: dict) -> bool:
    """
    Description: Checks if the given queue is full (reached its maximum capacity).
    Parameters: queue - a dictionary representing the queue.
    Return: True if the queue is full, False otherwise.
    """
    return queue["size"]==queue["n"]
    pass


# Check if the queue is empty
def is_empty(queue: dict) -> bool:
    """
    Description: Checks if the given queue is empty (contains no elements).
    Parameters: queue - a dictionary representing the queue.
    Return: True if the queue is empty, False otherwise.
    """
    return queue["n"]
    pass


# Add an element to the rear of the queue
def enqueue(queue: dict, item):
    """
    Description: Adds an element with the value 'val' to the rear of the queue.
    Parameters: queue - a dictionary representing the queue, val - the value to be added to the queue.
    """
    if is_full(queue):
        raise Exception("Queue is full")
    if queue["n"] == 0:
        queue["front"] = 0
    queue["rear"] = (queue["rear"] + 1) % queue["size"]
    queue["data"][queue["rear"]] = item
    queue["n"] += 1
    
    pass


# Remove and return the element from the front of the queue
def dequeue(queue: dict):
    """
    Description: Removes and returns the element from the front of the queue.
    Parameters: queue - a dictionary representing the queue.
    Return: The element from the front of the queue.
    """
    if is_empty(queue):
        raise Exception("Queue is empty")
    item = queue["data"][queue["front"]]
    if queue["n"] == 1:
        queue["front"] = -1
        queue["rear"] = -1
    else:
        queue["front"] = (queue["front"] + 1) % queue["size"]
    queue["n"] -= 1
    return item
    pass


# Return the element at the front of the queue without removing it
def peek(queue: dict):
    """
    Description: Returns the element at the front of the queue without removing it.
    Parameters: queue - a dictionary representing the queue.
    Return: The element at the front of the queue.
    """
    if is_empty(queue):
        raise Exception("Queue is full")
    return queue["data"][queue["front"]]
    pass


# Add an element with priority to the priority queue
def enqueue_priority(priority_queue: dict, item, priority: int):
    """
    Description: Adds an element with the value 'val' and the specified priority to the priority queue.
    Parameters: queue - a dictionary representing the priority queue, val - the value to be added to the queue,
                priority - the priority of the element.
    """
    if is_full(priority_queue):
        raise Exception("Queue is full")
    e = (item, priority)
    if is_empty(priority_queue):
        priority_queue["n"] == 0
        priority_queue["front"] = 0
        priority_queue["rear"] = 0
        priority_queue["data"][0] = e
    else:
        for i,j in enumerate(priority_queue["data"]):
            if j[1]> priority:
                index = i
        for k in range(priority_queue["n"],index,-1):
            priority_queue["data"][(priority_queue["front"] + k) % priority_queue["size"]] = priority_queue["data"][(priority_queue["front"] + (k - 1)) %priority_queue["size"]]
        
        priority_queue["data"][(priority_queue["front"] + i) % priority_queue["size"]] = e
        priority_queue["rear"] = (priority_queue["front"] + priority_queue["n"] - 1) % priority_queue["size"]
        priority_queue["n"] += 1



    
        
        
    
    pass


# Remove and return the element with the minimum priority from the priority queue
def dequeue_priority(priority_queue: dict):
    """
    Description: Removes and returns the element with the minimum priority from the priority queue.
    Parameters: queue - a dictionary representing the priority queue.
    Return: The element with the minimum priority from the priority queue.
    """
    if is_empty(priority_queue):
        raise Exception("Queue is empty")
    
    removed = priority_queue["data"]["front"]
    for j in range(priority_queue["front"],priority_queue["n"]-1):
        priority_queue["data"][(priority_queue["front"] + j) % priority_queue["size"]] = priority_queue["data"][(priority_queue["front"] + j + 1) % priority_queue["size"]]
    priority_queue["data"][(priority_queue["front"] + priority_queue["n"] - 1) % priority_queue["size"]] = None
    priority_queue["n"] -= 1
    if priority_queue["n"] == 0:
        priority_queue["front"] = 0
        priority_queue["rear"] = -1
    else:
        priority_queue["rear"] = (priority_queue["front"] + priority_queue["n"] - 1) % priority_queue["size"]
    return removed[0]
    pass


# Return the element with the minimum priority from the priority queue without removing it
def peek_priority(priority_queue: dict):
    """
    Description: Returns the element with the minimum priority from the priority queue without removing it.
    Parameters: queue - a dictionary representing the priority queue.
    Return: The element with the minimum priority from the priority queue.
    """
    return priority_queue["data"]["front"][0]
    pass


def handle_calls(call_queues, agent_queues, call_log):
    """
    Description: Simulates a call center scenario where calls are processed by agents based on their availability and call type.
    Type: Function
    Parameters: call_queues - a dictionary representing the call queue one for each call category,
                agent_queues - a dictionary representing the agent priority queues one for each call category.
                call_log - a dictionary representing the call logs as they are processed.
    Return: None , Modifies the call_log in place
    """
    # Simulation parameters
    Simulation = True
    currentTime = 0

    while Simulation:
        # provide your implementation here

        # Increment the current time for the next iteration
        currentTime += 1


# Main simulation function
def simulate_call_center(filename):
    """Description: Main Simulation function to read input data from a file, initialize agent and call queues, simulate call processing using CallSimulator, and return the call log data.
    Parameters: filename - the name of the file containing input data.
    Return: A list representing the call log data.
    """

    # Read input data from the file
    # First line contains the list of agents separated by spaces
    # Second line contains the number of calls to be processed
    # Populate the call queue with call details from the remaining lines contain the call details (start time, caller name, call duration) separated by spaces

    # provide your implementation here

    call_log = create_queue(num_calls)
    # Simulate call processing using CallSimulator

    handle_calls(call_queues, agent_queues, call_log)

    # Return the call log data as a list
    return call_log["data"]


simulate_call_center("KEComplaints.txt")
