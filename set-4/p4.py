#4. Write Program to find Triplets with a given sum
def find_triplets(arr, target_sum):
    arr.sort()  # Sort the array first
    triplets = []

    for i in range(len(arr) - 2):
        left = i + 1
        right = len(arr) - 1

        while left < right:
            current_sum = arr[i] + arr[left] + arr[right]

            if current_sum == target_sum:
                triplets.append((arr[i], arr[left], arr[right]))
                left += 1
                right -= 1
            elif current_sum < target_sum:
                left += 1
            else:
                right -= 1

    return triplets

# Example usage
arr = [1, 4, 6, 2, 3, 7, 9]
target_sum = 12

triplets = find_triplets(arr, target_sum)
print("Triplets with sum", target_sum, ":", triplets)



'''Sorting the array: The array is sorted to apply a two-pointer technique.
Iterating with the first pointer i: For each element arr[i], we use two additional pointers (left and right) to check the possible triplets.
Two-pointer technique: The left pointer starts at the next element (i + 1), and the right pointer starts at the last element of the array. Depending on the sum of the three numbers, either the left pointer is incremented or the right pointer is decremented until we find all triplets that match the target sum.'''
