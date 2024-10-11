#23.Write Program to count distinct elements of an array
def count_distinct_elements(arr):
  distinct_elements=set(arr)
  return len(distinct_elements)
array=[1,2,2,3,4,4,5]
distinct_count=count_distinct_elements(array)
print("Number of distinct elements:",distinct_count)
