
#write a program to check whether two array's are same or not 
def are_arrays_same(arr1, arr2):
    if len(arr1) != len(arr2):
        return False

    for i in range(len(arr1)):
        if arr1[i] != arr2[i]:
            return False

    return True

# Example usage
array1 = [1, 2, 3, 4]
array2 = [1, 2, 3, 4]
array3 = [1, 2, 4, 3]

print("Array1 and Array2 are same:", are_arrays_same(array1, array2))  # Output: True
print("Array1 and Array3 are same:", are_arrays_same(array1, array3))  # Output: False

