#3. Write Program to find missing elements of a range
def find_missing_elements(arr,start,end):
    full_range=set(range(start,end+1))
    arr_set=set(arr)
    missing_elements=aorted(list(full_range-arr_Set))
    return missing_elements
arr = [1, 2, 4, 5, 7, 9]
start = 1
end = 10

missing = find_missing_elements(arr, start, end)
print("Missing elements:", missing)  
  
  
  
