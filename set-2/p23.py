#Write a program to print Diamond pattern printing using stars
def print_diamond(n):
    for i in range(n):
        print(' ' * (n - i - 1), end='')
        print('*' * (2 * i + 1))

    for i in range(n - 2, -1, -1):
        print(' ' * (n - i - 1), end='')
        print('*' * (2 * i + 1))

n = int(input("Enter the number of rows: "))
print_diamond(n)
