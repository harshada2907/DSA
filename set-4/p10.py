#10. Write Program to find longest palindrome in an array
def is_palindrome(num):
    # Convert the number to a string and check if it reads the same forwards and backwards
    return str(num) == str(num)[::-1]

def find_longest_palindrome(arr):
    longest_palindrome = None

    for num in arr:
        if is_palindrome(num):
            if longest_palindrome is None or num > longest_palindrome:
                longest_palindrome = num

    return longest_palindrome

# Example usage
arr = [121, 131, 12321, 34543, 567, 123, 45654]

longest_palindrome = find_longest_palindrome(arr)
if longest_palindrome:
    print("Longest palindrome:", longest_palindrome)
else:
    print("No palindrome found in the array.")
