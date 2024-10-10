#19. Write Program to find whether an array is a subset of another array or not.
def is_subset(arr1, arr2):
    set1 = set(arr1)
    
    for elem in arr2:
        if elem not in set1:
            return False
    
    return True

# Example usage
arr1 = [1, 2, 3, 4, 5]
arr2 = [2, 4]

if is_subset(arr1, arr2):
    print("Array 2 is a subset of Array 1.")
else:
    print("Array 2 is not a subset of Array 1.")

