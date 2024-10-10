#15.Write Program to for sorting the elements of an array
# Function to sort an array
def sort_array(arr):
    arr.sort()
    return arr

# Example array
my_array = [34, 12, 5, 67, 1, 89, 23]

# Sorting the array
sorted_array = sort_array(my_array)

# Display the sorted array
print("Sorted Array:", sorted_array)
