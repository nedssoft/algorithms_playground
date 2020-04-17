def binary_search(arr, target):
    # get the size of the array
    size = len(arr)
    # if the size is zero, it makes no sense to search for the target
    if size == 0:
        return -1
    # Get the lowest index of the array
    low = 0
    # Get the highest index of the array
    high = size-1
    
    # While the end of the array is not reached
    while (low <= high):
        # Get the middle of the array
        mid = (low + high)//2
        # Check if the item in the middle is the target
        if arr[mid] == target:
            # The item is the target, return 1
            return 1
        # Check if the target is greater than the item in the middle
        # This means that the target is at the LHS
        elif target > arr[mid]:
            # set the lowest index to the item after the middle
            low = mid + 1
        # if the target is less than the item in the middle
        # Then the target is at the RHS
        else:
            # set the highest index to the item before the middle
            high = mid -1
    # If at the time the target is not found, then it never existed in the array
    return -1

def binary_search_recursive(arr, target, low, high):
    # Get the middle index of the array
    mid = (low+high) // 2

    # While the end of the array is not reached
    if (low <= high):
        if (len(arr) == 0):
            return -1
        # Check if the item in the middle is the target
        elif (arr[mid] == target):
            # The item is the target, return 1
            return 1
        # Check if the target is greater than the item in the middle
        # This means that the target is at the LHS
        elif target > arr[mid]:
            low = mid + 1
            # if the target is less than the item in the middle
            # Then the target is at the RHS
            return binary_search_recursive(arr, target,low,high)
        else:
            # set the highest index to the item before the middle
            high = mid - 1
            return binary_search_recursive(arr, target,low,high)
    else:
        # If at the time the target is not found, then it never existed in the array
        return -1
    

if __name__ == '__main__':
    arr = [i for i in range(10)]
    print(binary_search_recursive(arr,11, 0, len(arr)-1))
    print(binary_search(arr,11))