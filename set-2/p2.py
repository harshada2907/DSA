#Write a program to print Armstrong numbers between two intervals
#An Armstrong number (or Narcissistic number) is a number that is equal to the sum of its own digits raised to the power of the number of digits.
#153 is na Armstrong number because 1^3+5^3+3^3=153

#39474 is alos an Armstrong number because 9^4+4^4+7^4+4^4=9474

def is_armstrong(num):
  
    num_of_digits = len(str(num))
    
   
    sum_of_digits = sum(int(digit) ** num_of_digits for digit in str(num))
    
  
    return num == sum_of_digits

def print_armstrong_numbers(start, end):
    print(f"Armstrong numbers between {start} and {end} are:")
    for num in range(start, end + 1):
        if is_armstrong(num):
            print(num, end=" ")
    print()


start = int(input("Enter the starting number of the range: "))
end = int(input("Enter the ending number of the range: "))

print_armstrong_numbers(start, end)
