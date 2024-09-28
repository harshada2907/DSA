#Write a Program to Toggle each character in a string
def toggle_string(s):
   toggled=""
   for char in s:
     if char.isupper():
       toggled+=char.lower()
     elif char.islower():
       toggled+=char.upper()
     else:
       toggled+=char
    return toggled
input_string="Hello World!"
toggled_string=toggle_string(input_string)
print("Original String:",input_string)
print("Toggled String:",toggled_string)

