#Write a Program to print Length of the string without using strlen() function
def string_length(s):
  length=0
  for char in s:
    length+=1
  return length
user_string=input("Enter a string:")
length=string_length(user_string)
print(f"Length of the string:{length}")
