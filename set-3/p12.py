#12.Write a Program to Remove brackets from an algebraic expression
def remove_brackets(expression):
    expression = expression.replace("(", "")
    expression = expression.replace(")", "")
    expression = expression.replace("{", "")
    expression = expression.replace("}", "")
    expression = expression.replace("[", "")
    expression = expression.replace("]", "")
    return expression

algebraic_expression = input("Enter the algebraic expression: ")
print("Expression without brackets:", remove_brackets(algebraic_expression))
