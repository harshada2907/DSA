#2. Write Program to find the array type
def find_array_type(arr):
    if len(arr) == 0:
        return "Empty array"
    
    is_ascending = True
    is_descending = True
    is_identical = True

    for i in range(1, len(arr)):
        if arr[i] > arr[i - 1]:
            is_descending = False
        if arr[i] < arr[i - 1]:
            is_ascending = False
        if arr[i] != arr[i - 1]:
            is_identical = False

    if is_identical:
        return "All elements are identical"
    elif is_ascending:
        return "Array is sorted in ascending order"
    elif is_descending:
        return "Array is sorted in descending order"
    else:
        return "Array is unsorted"

# Example usage
arr1 = [1, 2, 3, 4, 5]
arr2 = [5, 4, 3, 2, 1]
arr3 = [3, 3, 3, 3]
arr4 = [3, 1, 4, 2]

print(find_array_type(arr1))  
print(find_array_type(arr2))  
print(find_array_type(arr3))  
print(find_array_type(arr4))  
