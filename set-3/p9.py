#Write a Program to Remove vowels from a string
def remove_vowels(input_string):
  vowels="aeiouAEIOU"
  result=''.join(char for char in input_string if char not in vowels)
  return result
input_string=input("Enter a string:")
output_string=remove_vowels(input_string)
print("string after removing vowels:",output_string)

