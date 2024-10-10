#14.Write Program to find second smallest element in an array
def find_second_smallest(arr):
    if len(arr) < 2:
        return None

    # Initialize first and second smallest to infinity
    first_smallest = second_smallest = float('inf')

    # Traverse the array
    for num in arr:
        if num < first_smallest:
            second_smallest = first_smallest
            first_smallest = num
        elif first_smallest < num < second_smallest:
            second_smallest = num

    return second_smallest if second_smallest != float('inf') else None

# Example usage:
arr = [10, 5, 8, 12, 7]
result = find_second_smallest(arr)
print("Second smallest element is:", result)
