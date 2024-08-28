#Write a program to identify if the character is an alphabet or not

char=input("please enter a character")
if char.isalpha():
  print(f"'{char}' is an alphabet")
else:
  print(f"'{char}' is not alphabet")