#20.Write a Program to Replace substring in a string
def replace_substring(original_string, old_substring, new_substring):
    return original_string.replace(old_substring, new_substring)

original_string = "I love programming"
old_substring = "programming"
new_substring = "Python"
result = replace_substring(original_string, old_substring, new_substring)

print("Modified string:", result)
