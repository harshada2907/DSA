#18.Write Program to find whether Arrays are disjoint or not
def are_disjoint(arr1, arr2):
    set1 = set(arr1)
    
    for elem in arr2:
        if elem in set1:
            return False
    
    return True

arr1 = [1, 2, 3, 4]
arr2 = [5, 6, 7, 8]

if are_disjoint(arr1, arr2):
    print("The arrays are disjoint.")
else:
    print("The arrays are not disjoint.")

