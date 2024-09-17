#Write a program for Binary to octal conversion
def binary_to_octal(binary):
  decimal=int(binary,2)
  octal=oct(decimal)
  return octal[2:]
binary_input=input("Enter a binary number:")
octal_output=binary_to_octal(binary_input)
print(f"The octal equivalent of binary{binary_input} is {octal_output}")


