#Write a program to Replace all 0’s with 1 in a given integer
def replace_zeros_with_ones(number):
  number_str=str(number)
  replaced_str=number_str.replace('0','1')
  replaced_number=int(replaced_str)
  return replaced_number
input_number=int(input("Enter an integer:"))
output_number=replace_zeros_with_ones(input_number)
print(f"Number after replacing all 0's with 1's :{output_number}")
