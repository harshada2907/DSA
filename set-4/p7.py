#7. Write Program for basic array operations (Insert, delete and search an element)
def insert_element(arr, element, position):
    arr.insert(position, element)
    return arr

def delete_element(arr, element):
    if element in arr:
        arr.remove(element)
    else:
        print(f"Element {element} not found in the array.")
    return arr

def search_element(arr, element):
    if element in arr:
        return arr.index(element)
    else:
        return -1

# Example usage
arr = [1, 2, 3, 4, 5]

# Insert element
print("Original array:", arr)
arr = insert_element(arr, 10, 2)  # Insert 10 at position 2
print("Array after insertion:", arr)

# Delete element
arr = delete_element(arr, 4)  # Delete element 4
print("Array after deletion:", arr)

# Search for an element
element_to_search = 5
position = search_element(arr, element_to_search)
if position != -1:
    print(f"Element {element_to_search} found at position {position}")
else:
    print(f"Element {element_to_search} not found in the array.")
