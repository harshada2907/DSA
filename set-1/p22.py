#Write a program to Add two fractions
from fractions import Fraction
frac1 = Fraction(input("Enter first fraction (e.g., 1/2): "))
frac2 = Fraction(input("Enter second fraction (e.g., 1/3): "))

result = frac1 + frac2

print(f"The sum of {frac1} and {frac2} is: {result}")
