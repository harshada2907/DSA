#Write a program to print Pyramid pattern using stars
def pyramid_pattern(rows):
  for i in range(1,rows+1):
    print(""*(rows-i),end="")
    print("*" *i)
num_rows=int("Enter the number of rows:"))
pyramid_pattern(num_rows)
    
    
