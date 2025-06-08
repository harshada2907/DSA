#Write a program to find Number of digits in an integer
def count_digits(number):
    return len(str(abs(number)))
number=int(input("Enter an integer:"))
digits=count_digits(number)
print(f"The number of digits in {number} is {digits}.")
  
