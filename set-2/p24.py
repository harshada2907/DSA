#Write a program to print Diamond pattern printing using numbers.
def print_diamond(n):
    for i in range(1, n + 1):
        print(' ' * (n - i), end='')
        print(' '.join(str(i) for _ in range(i)))

    for i in range(n - 1, 0, -1):
        print(' ' * (n - i), end='')
        print(' '.join(str(i) for _ in range(i)))

n = int(input("Enter the number of rows: "))
print_diamond(n)


