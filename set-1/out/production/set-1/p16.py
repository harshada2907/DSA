#Write a program to find LCM of two numbers
def find_lcm(x, y):
    # We start with the maximum of x and y
    if x > y:
        greater = x
    else:
        greater = y

    # Loop until we find a number that is divisible by both x and y
    while True:
        if (greater % x == 0) and (greater % y == 0):
            lcm = greater
            break
        greater += 1

    return lcm

# Input two numbers
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Calculate the LCM
result = find_lcm(num1, num2)

# Display the result
print(f"The LCM of {num1} and {num2} is {result}")

