#Write a program to identify if the number is Armstrong number or not
def is_armstrong(number):
  num_str=str(number)
  num_digits=len(num_str)
  total_sum=sum(int(digit)**num_digits for digit in num_str)
  return total_Sum==number

num=int(input("Enter a number:"))
if is_armstrong(num)
 print(f"{num} is an Armstrong number.")
else:
 print(f"{num} is not as Armstrong number.")


