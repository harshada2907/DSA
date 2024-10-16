#25.Write Program to find repeating elements in an array
def find_repeating_elements(arr):
    element_count = {}
    
    for element in arr:
        if element in element_count:
            element_count[element] += 1
        else:
            element_count[element] = 1
    
    repeating = [element for element in arr if element_count[element] > 1]
    
    return list(set(repeating))

arr = [4, 5, 4, 5, 6, 7, 8, 8, 9]
repeating_elements = find_repeating_elements(arr)
print("Repeating elements:", repeating_elements)


