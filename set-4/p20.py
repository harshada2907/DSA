#20.Write Program to find maximum scalar product of two vectors
def max_scalar_product(vector1, vector2):
    vector1.sort()
    vector2.sort()
    
    scalar_product = sum(a * b for a, b in zip(vector1, vector2))
    
    return scalar_product


vector1 = [1, 3, 5]
vector2 = [2, 4, 6]

result = max_scalar_product(vector1, vector2)
print("Maximum scalar product:", result)
