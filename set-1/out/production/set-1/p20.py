#Write a program to identify if the number is Perfect number or not
def is_perfect_number(n):
  sum_of_divisors=0
  for i in range(1,n):
     if n % i==0:
       sum_of_divisors+=i
  return sum_of_divisors==n
number=int(input("enter a number:"))
if is_perfect_number(number):
  print("f"{number} is a perfect number.")
else:
  print(f"{number} is not a perfect number.")
  
