#Write a program to print Pascal triangle
def print_pascals_triangle(n):
  for i in range(n):
    print("" *(n-i),end="")
    value=1
    for j in range(i+1):
      print(value,end="")
      value=value*(i-j)//(j+1)
    print()
n=int(input("Enter the number of rows:"))
print_pascals_traingle(n)
    
    
    
    
    
    
    
    
    
