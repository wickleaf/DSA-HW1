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
    for i,j in enumerate(arr,1):
        if (i%chunk_size)==0:
            x[k][col]=j
            k+=1
            col=0
        else:
            x[k][col]=j
            col+=1
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
    # while high_pointer > low_pointer:
    #     if arr1[low_pointer] > arr2[high_pointer]:
    #         low_pointer+=1
    #     else:
    #         arr1[low_pointer],arr2[high_pointer]=arr2[high_pointer],arr1[low_pointer]
    #         high_pointer-=1

    tempArr = [None]*(l1+l2)
    for i in range(l1+l2):
        if arr1[arr1_pointer] > arr2[arr2_pointer] and arr1_pointer<=l1-1:
            tempArr[i] = arr1[arr1_pointer]
        elif arr1[arr1_pointer] < arr2[arr2_pointer] and arr2[arr2_pointer]<=l2-1:
            tempArr[i] = arr2[arr2_pointer]



    # for i in range(l1):
    #     tempArr[i]=arr1[i]
    # for i in range(l1,l1+l2):
    #     tempArr[i]=arr2[i]
        
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
    chonk = round((l**(1/2)))
    broken = divide_chunks(arr,chonk)
    for i in range(chonk):
        selection_sort(broken[i])
    lenBroken = length(broken)
    f = 0
    #print(length(broken))
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
    int_list= [int(x) if i != "None" else 0 for i in x]

    return fusion_sort(int_list)
    pass


if __name__ == "__main__":
    main("./Inputs/sorting03.txt")
