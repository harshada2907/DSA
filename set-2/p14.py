#Write a program for Decimal to binary conversion
def decimal_to_binary(decimal):
  if decimal==0:
    return "0"
  binary=""
  while deciaml>0:
    remainder=decimal%2
    binary=str(remainder)+binary
    decimal=decimal//2
  return binary
decimal_number=int(input("Enter a decimal number:"))
binary_number=decimal_to_binary(decimal_number)
