#Write a program to identify if the number is Palindrome or not
def is_palindrome(num):
  return str(num)==str(num)[::-1]
number=int(input("Enter a number."))
if is_palindrome(number):
  print(f"{number} is a palindrome.")
else:
  print(f"{number} is not a palindrome.")
