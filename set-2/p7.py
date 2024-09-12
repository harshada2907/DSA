#Write a program to print Palindromic pyramid pattern printing..
def print_palindromic_pyramid(n):
  for i in range(1,n+1):
    print(''*(n-i),end='')
  for j in range(1,i+1):
    print(j,end='')
  for j in range(i-1,0,-1):
    print(j,end='')
rows=5
print_palindromic_pyramid(rows)
    
