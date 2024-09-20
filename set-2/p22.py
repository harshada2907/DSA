#Write a program to print Solid and hollow rectangle star pattern
def solid_rectangle(rows,cols):
  for i in range(rows):
    print("*" *cols)
rows=int(input("Enter the number of rows:"))
cols=int(input("Enter the number of columns:"))
print("Solid Rectangle:")
solid_rectnagle(rows,cols)

