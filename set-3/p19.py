#18.Write a Program to print Non-repeating characters in a string
def non_repeating_characters(input_string):
    frequency = {}
    
    for char in input_string:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    
    result = [char for char in input_string if frequency[char] == 1]
    
    return ''.join(result)

input_string = "hello world"
result = non_repeating_characters(input_string)
print("Non-repeating characters:", result)
