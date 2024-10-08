#5. Write Program to find number of even and odd elements in an array
def count_even_odd(arr):
    even_count = 0
    odd_count = 0

    # Iterate through each element in the array
    for num in arr:
        if num % 2 == 0:
            even_count += 1
        else:
            odd_count += 1

    return even_count, odd_count

# Example usage
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_count, odd_count = count_even_odd(arr)
print("Number of even elements:", even_count)
print("Number of odd elements:", odd_count)
