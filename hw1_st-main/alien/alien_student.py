from typing import Any

import list_adt_student as listadt


def create_alien() -> dict[str, Any]:
    """
    Creates an 'alien' dictionary with a list to store messages.
    You can add other attributes if required

    Returns:
    A dictionary representing an 'alien' with a list to store messages:
    {
        'messages': listadt.create_list(100)    # List to store messages with a maximum capacity of 100
    }
    """
    messages = {"messages": listadt.create_list(100)}

    # provide other required implementation here
    pass


def add(seq: int, msg: str, length: int, alienList: dict):
    """
    Parameters:
    - seq: The sequence number of the message.
    - msg: The message to be added.
    - length: The expected length of the message to be added.
    - alienList: The 'alien' dictionary containing the messages list.
    """

    # provide implementation here
    pass


def delete(seq: int, msg: str, length: int, alienList: dict):
    """

    Parameters:
    - seq: The sequence number of the message to be deleted.
    - msg: The message to be deleted.
    - length: The expected length of the message to be deleted.
    - alienList: The 'alien' dictionary containing the messages list.
    """

    # provide implementation here
    pass


def get_messages(alienList: dict) -> list[str]:
    """

    Parameters:
    - alienList: The 'alien' dictionary containing the messages list.

    Returns:
    A list of all messages in the conversation.
    """

    # provide implementation here
    pass


def main(filename) -> list[str]:
    """
    Reads data from a file, processes it, and returns the conversation as a list.

    Data is provided in the following format:
    There can be multiple lines in the file, each line containing an integer and an optional string separated by a space. The integer represents the sequence number of the message, and the string represents the message itself. If the string is not provided, it is assumed to be an empty string. The sequence number 0 indicates the end of the conversation.

    Process the data as follows:
    - If the sequence number is positive, add the message to the conversation.
    - If the sequence number is 0, delete the message from the conversation.
    - If the sequence number is negative, stop processing the file.

    Parameters:
    - filename: The name of the file to read data from.

    Returns:
    A list representing the conversation obtained from the file.
    """
    messages = create_alien()

    # Provide your implementation here

    output = get_messages(messages)
    return output
