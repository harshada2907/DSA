#Write a program to identify if the number is Strong number or not
import math

def is_strong_number(num):
    digits = str(num)
    sum_of_factorials = 0
    for digit in digits:
        sum_of_factorials += math.factorial(int(digit))
    return sum_of_factorials == num

number = int(input("Enter a number:"))

if is_strong_number(number):
    print(f"{number} is a strong number.")
else:
    print(f"{number} is not a strong number.")

  
