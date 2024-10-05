#19.Write a Program to check if two strings are Anagram or not
def are_anagrams(str1, str2):
    return sorted(str1) == sorted(str2)

str1 = "listen"
str2 = "silent"
result = are_anagrams(str1, str2)

if result:
    print(f"{str1} and {str2} are anagrams")
else:
    print(f"{str1} and {str2} are not anagrams")


