#Write a Program to Remove brackets from an algebraic expression

def remove_brackets(expression):
    # Remove brackets from the given expression
    return expression.replace('(', '').replace(')', '')

# Example usage
expression = "(a+b)*(c+d)"
result = remove_brackets(expression)
print("Expression without brackets:", result)
