#Write a program to find number of integers which has exactly 9 divisors
import math

def count_numbers_with_nine_divisors(limit):
    count = 0
    for i in range(1, limit + 1):
        divisors = 0
        for j in range(1, int(math.sqrt(i)) + 1):
            if i % j == 0:
                if j * j == i:
                    divisors += 1
                else:
                    divisors += 2
        if divisors == 9:
            count += 1
    return count

limit = 100000
result = count_numbers_with_nine_divisors(limit)
print(result)

