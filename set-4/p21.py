#21.Write Program to find whether the numbers of an array be made equal?
def can_be_made_equal(arr):
  return len(set(arr))==1
arr=[4,4,4,4]
if can_be_made_equal(arr):
  print("All elements a=can be made equal.")
else:
 print("The elements cannot be made equal.")   
  
