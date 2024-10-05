#15.Write a Program to Count the sum of numbers in a string
def sum_of_numbers_in_string(input_string):
    total_sum = 0
    current_number = ''
    
    for char in input_string:
        if char.isdigit():
            current_number += char
        else:
            if current_number != '':
                total_sum += int(current_number)
                current_number = ''
    
    if current_number != '':
        total_sum += int(current_number)
    
    return total_sum

input_string = "The price is 40 dollars and the tax is 5"
result = sum_of_numbers_in_string(input_string)
print("The sum of numbers in the string is:", result)
