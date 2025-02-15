import math
def initialize_matrix(n: int) -> list[list[int]]:
    """
    A  function that takes an integer n as an argument and returns a 2D array of size n x n with each cell containing None values.
    """
    return [[None for _ in range(n)] for _ in range(n)]
    pass


def length(arr: list[int]) -> int:
    """
    A function that takes a single-dimensional array, arr, as an argument and returns the count of valid data items in it, i.e., the non-None values.
    """
    count=0
    for i in arr:
        if i != None:
            count+=1
    return count
            

    pass


def divide_chunks(arr: list[int], chunk_size: int) -> list[list[int]]:
    """
    A fruitful function that takes an array and chunk size as arguments and divides the array into chunks of size k.
    """
    l = length(arr)
    x = initialize_matrix(chunk_size)
    k=0
    col= 0
    for i,j in enumerate(arr,1): #Initially used enumerate for a different approach I had in mind but switched to a different one, hence the redunant i
        x[k][col]=j
        col+=1
        if col == chunk_size:
            k+=1
            col=0
    return x
    # return [arr[i:i+chunk_size] for i in range(0,l,chunk_size)] #Slice Method




    pass


def selection_sort(arr: list[int]) -> None:
    """
    A void function that takes an array and sorts it in descending order using the selection sort algorithm.
    This is an in-place function, meaning the original array that was passed as a reference will be updated with the
    sorted values.

    The function should not return anything.
    """
    l = length(arr)
    for i in range(l):
        max_index = i
        for j in range(i+1,l):
            if arr[j] > arr[max_index]:
                max_index = j
        arr[i],arr[max_index]=arr[max_index],arr[i]
    pass


def consolidate(arr1: list[int], arr2: list[int]) -> list[int]:
    """
    A fruitful function that combines two sorted arrays into one sorted array using a two-pointer approach,
    in a descending order.

    The function returns the updated, sorted array
    """
    l1 = length(arr1)
    l2 = length(arr2)

    arr1_pointer = 0
    arr2_pointer = 0
    k=0
    
    tempArr = [None]*(l1+l2)
    while arr1_pointer <l1 and arr2_pointer<l2:
        if arr1[arr1_pointer]>arr2[arr2_pointer]:
            tempArr[k]=arr1[arr1_pointer]
            arr1_pointer+=1
            k+=1
        else:
            tempArr[k]=arr2[arr2_pointer]
            arr2_pointer+=1
            k+=1
    while arr1_pointer<l1: #To push remaining elements onto tempArr, if any.
        tempArr[k]=arr1[arr1_pointer]
        arr1_pointer+=1
        k+=1
    while arr2_pointer<l2:
        tempArr[k]=arr2[arr2_pointer]
        arr2_pointer+=1
        k+=1
    
    return tempArr
        
    pass


def fusion_sort(arr: list[int]) -> list[int]:
    """
    A fruitful function that implements the “Fusion Sort” algorithm described above to sort the valid data items
    in a descending order, while preserving the positions of invalid items.

    The function returns the updated, sorted array
    """

    l = length(arr)

    if l<=0:
        return arr
    chonk = math.ceil((l**(1/2)))
    broken = divide_chunks(arr,chonk)
    for i in range(chonk):
        selection_sort(broken[i])
    lenBroken = length(broken)
    f = 0

    for i in range(1,lenBroken):
        broken[f] = consolidate(broken[f],broken[i])

    return broken[f]

    pass


def main(filename) -> list[int]:
    """
    - Take input from the given filename one line at a time
    - Apply fusion sorting algorithm to get the sorted arrays and returns the output, sorted array.
    """
    file = open(filename,"r")
    x = file.readline().strip()
    x= x.strip("[]").split(", ")
    int_list= [int(i) if i != "None" else None for i in x] #In case entire array is None values
    if length(int_list)==0:
        return int_list
    else:
        int_list = [int(i) if i != "None" else -1 for i in x] #Replacing None with -1 to distribute into chunks properly
        r = fusion_sort(int_list)
        for i,j in enumerate(r):
            if j == -1:
                r[i]=None #Replacing -1 back with None
        return r
 
    pass


if __name__ == "__main__":
    main("./Inputs/sorting02.txt")
