
def remove_non_alphabets(input_string):
    filtered_string = ''.join(char for char in input_string if char.isalpha())
    return filtered_string

input_str = "Hello! Welcome to 2024: Let's code."
result = remove_non_alphabets(input_str)
print(result)  # Output: HelloWelcometLetscode
