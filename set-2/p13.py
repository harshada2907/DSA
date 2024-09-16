# Write a program for Binary to decimal conversion
def binary_to_decimal(binary):
  decimal=0
  binary=str(binary)
  for digit in binary:
    decimal=decimal*2+int(digit)
  return decimal
binary_number=input("Enter a binary number:")
decimal_number=binary_to_decimal(binary_number)
print(f"The decimal equivalent of binary(binary_number} is {decimal_number}")
