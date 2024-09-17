#Write a program for Octal to binary conversion
def octal_to_binary(octal):
  decimal=int(octal,8)
  binary=bin(decimal)
  return binary[2:]
octal_input=input("Enter an octal number:")
binary_output=octal_to_binary(octal_input)
print(f"The binary equivalent of octal {octal_input} is {binary_output}")
