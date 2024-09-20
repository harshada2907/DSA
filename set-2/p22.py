#Write a program to print Solid and hollow rectangle star pattern
#solid_rectangle
def solid_rectangle(rows,cols):
  for i in range(rows):
    print("*" *cols)
rows=int(input("Enter the number of rows:"))
cols=int(input("Enter the number of columns:"))
print("Solid Rectangle:")
solid_rectnagle(rows,cols)

#hollow_rectangle
def hollow_rectangle(rows, cols):
    for i in range(rows):
        if i == 0 or i == rows - 1:
            print("* " * cols)
        else:
            print("* " + "  " * (cols - 2) + "*")

rows = int(input("Enter the number of rows: "))
cols = int(input("Enter the number of columns: "))

print("Hollow Rectangle:")
hollow_rectangle(rows, cols)
