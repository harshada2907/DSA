#14.Write a Program to Remove spaces from a string
def remove_spaces(input_string):
  return input_string.replace(" ","")
string_with_spaces="Hello World! How are you?"
string_without_spaces=remove_spaces(string_with_spaces)
print("Original String:",string_with_spaces)
print("String without spaces:",string_without_spaces)
