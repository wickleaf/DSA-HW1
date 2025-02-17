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
    return queue["n"]==0
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
        raise Exception("Priority queue full")
    
    e = (priority, item)
    if is_empty(priority_queue):
        priority_queue["data"][0] = e
        priority_queue["front"] = 0
        priority_queue["rear"] = 0
        priority_queue["n"] = 1
        return

    # Find insertion position
    pos = None
    for i in range(priority_queue["front"], priority_queue["front"] + priority_queue["n"]):
        index = i % priority_queue["size"]
        if priority < priority_queue["data"][index][0]:
            pos = index
            break

    if pos is None:  # Add at end
        pos = (priority_queue["rear"] + 1) % priority_queue["size"]
    else:  # Shift elements
        for j in range(priority_queue["rear"], pos-1, -1):
            next_idx = (j + 1) % priority_queue["size"]
            current_idx = j % priority_queue["size"]
            priority_queue["data"][next_idx] = priority_queue["data"][current_idx]

    priority_queue["data"][pos] = e
    priority_queue["rear"] = (priority_queue["rear"] + 1) % priority_queue["size"]
    priority_queue["n"] += 1

# Remove and return the element with the minimum priority from the priority queue
def dequeue_priority(priority_queue: dict):
    """
    Description: Removes and returns the element with the minimum priority from the priority queue.
    Parameters: queue - a dictionary representing the priority queue.
    Return: The element with the minimum priority from the priority queue.
    """
    if is_empty(priority_queue):
        raise Exception("Priority queue empty")
    
    item = priority_queue["data"][priority_queue["front"]]
    priority_queue["front"] = (priority_queue["front"] + 1) % priority_queue["size"]
    priority_queue["n"] -= 1
    if priority_queue["n"] == 0:
        priority_queue["front"] = -1
        priority_queue["rear"] = -1
    return item

# Return the element with the minimum priority from the priority queue without removing it
def peek_priority(priority_queue: dict):
    """
    Description: Returns the element with the minimum priority from the priority queue without removing it.
    Parameters: queue - a dictionary representing the priority queue.
    Return: The element with the minimum priority from the priority queue.
    """
    if is_empty(priority_queue):
        raise Exception("Priority queue empty")
    return priority_queue["data"][priority_queue["front"]]

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
    categories = list(call_queues.keys())
    
    while Simulation:
        # provide your implementation here
        processed = False #Processing calls for each category
        for category in categories:
            call_q = call_queues[category]
            agent_q = agent_queues[category]
            
            while not is_empty(call_q) and not is_empty(agent_q):
                try:
                    call_priority, call_data = peek_priority(call_q) #Unpacking tuple
                    agent_priority, agent_name = peek_priority(agent_q)
                except:
                    break
                
                if call_priority > currentTime:
                    break
                
                if agent_priority > currentTime:
                    break
                
                # Dequeue call and agent
                call = dequeue_priority(call_q)
                agent = dequeue_priority(agent_q)
                start_time, duration, caller = call[1]
                
                # Process call
                end_time = currentTime + duration
                waiting_time = currentTime - start_time
                enqueue(call_log, (caller, category, agent[1], currentTime, end_time, waiting_time))
                
                enqueue_priority(agent_q, agent[1], end_time)
                processed = True
                
        # Check if any agent is now available
        for category in categories:
            agent_q = agent_queues[category]
            if not is_empty(agent_q):
                agent_priority, _ = peek_priority(agent_q)
                if agent_priority <= currentTime:
                    agent = dequeue_priority(agent_q)
                    enqueue_priority(agent_q, agent[1], 0)
        
        # Check termination condition
        all_empty = True
        for category in categories:
            if not is_empty(call_queues[category]):
                all_empty = False
                break
        if all_empty:
            break
            
        if not processed:
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
    # Read input file
    with open(filename, 'r') as f:
        lines = [line.strip() for line in f.readlines()]
        #print(lines)

    categories = lines[0].split()
    agent_counts = list(map(int, lines[1].split()))
    

    agent_queues = create_agents_queue(categories, agent_counts)
    current_line = 2
    for index, category in enumerate(categories):
        agent_names = lines[current_line].split()
        current_line += 1
        for name in agent_names:
            enqueue_priority(agent_queues[category], name, 0)
    

    num_calls = int(lines[current_line])
    current_line += 1
    call_queues = create_call_queues(categories, num_calls)
    for _ in range(num_calls):
        callerInfo = lines[current_line].split()
        #print(callerInfo)
        current_line += 1
        start_time = int(callerInfo[0])
        caller = callerInfo[1]
        duration = int(callerInfo[2])
        category = callerInfo[3]
        enqueue_priority(call_queues[category], (start_time, duration, caller), start_time)
    
    # Initialize call log
    call_log = create_queue(num_calls)
    
    handle_calls(call_queues, agent_queues, call_log)

    # Return the call log data as a list
    return call_log["data"]

simulate_call_center("./inputs/KEComplaints01.txt")