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
    alienList = {"messages": listadt.create_list(100)}

    # provide other required implementation here
    alienList["sequence_Map"]= {"minSeq":0,"maxSeq":0,"order":{},"count":0}
    return alienList
    


def add(seq: int, msg: str, length: int, alienList: dict):
    """
    Parameters:
    - seq: The sequence number of the message.
    - msg: The message to be added.
    - length: The expected length of the message to be added.
    - alienList: The 'alien' dictionary containing the messages list.
    """
    
    # provide implementation here
    if len(msg)!=length:
        return "Discarded"
    m=alienList["messages"]
    s = alienList["sequence_Map"]
    if listadt.is_empty(m):
        listadt.insert_first(msg,m)
        currentR = s["count"]
        s["maxSeq"] = seq 
        s["minSeq"] = seq
        s["order"][currentR]=(m["rear"],seq)
    else:
        currentR=s["count"]
        if seq < s["minSeq"]:
            currentR+=1
            listadt.insert_last(msg,m)
            s["order"][currentR] = (m["rear"],seq)
            s["count"] = currentR
            s["minSeq"]=seq
        elif seq>s["maxSeq"]:
            currentR-=1
            listadt.insert_last(msg,m)
            s["order"][currentR] = (m["rear"],seq)
            s["count"] = currentR
            s["maxSeq"]=seq


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
    
    m = alienList["messages"]
    s = alienList["sequence_Map"]
    if listadt.is_empty(m):
        return
    else:
        listadt.remove_last(m)
        s["order"].popitem()
        s["count"]+=1
        

        

    pass


def get_messages(alienList: dict) -> list[str]:
    """

    Parameters:
    - alienList: The 'alien' dictionary containing the messages list.

    Returns:
    A list of all messages in the conversation.
    """
    m = alienList["messages"]
    s = alienList["sequence_Map"]
    msgLst = [None]*m["n"]
    ordering = s["order"]
    count=0
    for i in ordering.values():
        msgLst[count] = m["data"][i[0]]
        count+=1
    return msgLst
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
    alienList = create_alien()

    with open(filename, 'r') as file:
        for line in file:
            extracted_Line = line.strip().split()
            seq = int(extracted_Line[0])  
            if seq < 0:
                break  
            elif seq == 0:
                delete(seq, "", 0, alienList) 
            else:
                msg = ""
                msgLen = 0
                if len(extracted_Line) > 2:
                    msg = " ".join(extracted_Line[1:-1])  
                    msgLen = int(extracted_Line[-1])  
                elif len(extracted_Line) == 2:
                    msg = extracted_Line[1]  
                    msgLen = len(msg)  
                add(seq, msg, msgLen, alienList) 
    
    s = alienList["sequence_Map"]
    orderingDict = s["order"]
    dictKeys = list(orderingDict.keys())
    dictKeys.sort(reverse=True)
    sortedOrderingDict = {i:orderingDict[i] for i in dictKeys}
    s["order"]=sortedOrderingDict

    output = get_messages(alienList)
    final = " ".join(output)
    return final
if __name__ == "__main__":
    main("./inputs/alien01.txt")