#Write a program to print Floyd’s triangle
def floyd_triangle(rows):
  num=1
  for i in range(1,rows+1):
    for j in range(1,i+1):
      print(num,end="")
      num+=1
     print()
n=int(input("Enter the number of rows:"))
floyd_triangle(n)
