#12. Write a program to find Permutations in which n people can occupy r seats in a classroom.
import math

def find_permutations(n, r):
    if r > n:
        return "Number of seats can't be more than the number of people."
    
    permutations = math.factorial(n) // math.factorial(n - r)
    return permutations

n = int(input("Enter the number of people (n): "))
r = int(input("Enter the number of seats (r): "))

result = find_permutations(n, r)
print(f"The number of ways {n} people can occupy {r} seats is: {result}")
