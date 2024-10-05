#17.Write a Program to calculate the Frequency of characters in a string
def character_frequency(input_string):
    frequency = {}
    
    for char in input_string:
        if char in frequency:
            frequency[char] += 1
        else:
            frequency[char] = 1
    
    return frequency

input_string = "hello world"
result = character_frequency(input_string)
print("Character frequency:", result)
