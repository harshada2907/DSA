#13.Write a Program to Remove characters in a string except alphabets
def remove_non_alphabets(input_string):
  return ''.join([char for char in input_string if char.isalpha()])
string_with_characters="Hello,World! 123 @#"
string_only_alphabets=remove_non_alphabets(string_with_characters)
print("Original String:",string_with_characters)
print("String with only alphabest:"String_only_alphabets)
