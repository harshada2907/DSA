#Write a program to find Fibonacci series up to n
def fibonacci_series(n):
    a, b = 0, 1
    series = []
    for _ in range(n):
        series.append(a)
        a, b = b, a + b
    return series

n = int(input("Enter the number of terms in the Fibonacci series: "))
result = fibonacci_series(n)
print(f"The first {n} terms of the Fibonacci series are: {result}")
