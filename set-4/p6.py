#6. Write Program to find Frequency of each element of an array
from collections import Counter

def find_frequency(arr):
    # Use Counter to find frequency of each element
    frequency = Counter(arr)
    
    # Convert to a dictionary and return
    return dict(frequency)

# Example usage
arr = [1, 2, 3, 2, 1, 5, 6, 1, 6, 5, 2]

frequency = find_frequency(arr)
print("Element frequencies:", frequency)
