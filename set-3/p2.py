#Write a Program to reverse a string.
def reverse_string(original):
  reversed_string=original[::-1]
  return reversed_string
original_string="Hello,World!"
reversed_string=reverse_string(original_string)
print("Original String:",original_string)
print("Reversed String:"reversed_string)
  
  
