#24.Write Program to find non-repeating elements of an array
def find_non_repeating_elements(arr):
    element_count = {}
    
    for element in arr:
        if element in element_count:
            element_count[element] += 1
        else:
            element_count[element] = 1
    
    non_repeating = [element for element in arr if element_count[element] == 1]
    
    return non_repeating

arr = [4, 5, 4, 5, 6, 7, 8, 8, 9]
non_repeating_elements = find_non_repeating_elements(arr)
print("Non-repeating elements:", non_repeating_elements)
