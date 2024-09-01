#Write a program to reverse a given number
def reverse_number(number):
    reversed_num = 0
    while number > 0:
        digit = number % 10
        reversed_num = reversed_num * 10 + digit
        number = number // 10
    return reversed_num

num = int(input("Enter a number: "))
reversed_num = reverse_number(num)

print("Reversed number is:", reversed_num)



