#16.Write a Program to Capitalize the first and last letter of each word of a string
def capitalize_first_last_letters(input_string):
    words = input_string.split()
    result = []
    
    for word in words:
        if len(word) > 1:
            word = word[0].upper() + word[1:-1] + word[-1].upper()
        else:
            word = word.upper()
        result.append(word)
    
    return ' '.join(result)

input_string = "hello world python is fun"
result = capitalize_first_last_letters(input_string)
print("Result:", result)
