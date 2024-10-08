#8. Write Program to find smallest and largest element in an array
def find_smallest_largest(arr):
    if len(arr) == 0:
        return None, None  # Return None if the array is empty

    smallest = min(arr)  # Use the built-in min function to find the smallest element
    largest = max(arr)   # Use the built-in max function to find the largest element

    return smallest, largest

# Example usage
arr = [10, 20, 4, 45, 99, -5, 0]

smallest, largest = find_smallest_largest(arr)
print("Smallest element:", smallest)
print("Largest element:", largest)
