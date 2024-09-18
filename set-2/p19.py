#Write a program to find number of times digit 3 occurs in each and every number from 0 to n
def count_digit_3(n):
  def count_3_in_number(num):
    return str(num).count('3)
  counts=[count_3_in_number(i) for i in range(n+1)]
  return counts
n=100
counts=count_digit_3(n)
for i,count in enumerate(counts):
 print(f"Number {i} contains the digit 3 {count} times")
