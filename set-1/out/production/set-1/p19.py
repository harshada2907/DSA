#Write a program to find the Factors of a number
def find_factors(n):
  factors=[]
  for i in range(1,math.isqrt(n)+1):
    if n % i==0:
      factors.append(i)
      if i!=n//i:
        factors.append(n//i)
  return sorted(factors)
number=int(input("Enter a number:"))
factors=find_factors(number)
print(f"The factors of{number} are:{factors}")
