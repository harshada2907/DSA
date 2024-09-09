# Write a program to express a number as a sum of two prime numbers?
def is_prime(n):
  if n<=1:
    return False
  for i in range(2,int(n**0.5)+1):
    if n % i==0:
      return False
  return True
def find_prime_sum(num):
  for i in range(2,num):
    if is_prime(i) and is_prime(num-i):
      return i,num-i
  return None
num=int(input("Enter a number:"))
result=find_prime_sum(num)
if result:
  print(f"{num}" can be expressed as the sum of {result[0]} and {result[1]}.")
else:
print(f"{num} cannot be expressed as the sum of two prime numbers.")
  
