#22.Write Program to find symmetric pairs in an array
def find_symmetric_pairs(pairs):
    pair_dict = {}
    symmetric_pairs = []

    for a, b in pairs:
        if (b, a) in pair_dict:
            symmetric_pairs.append((a, b))
        else:
            pair_dict[(a, b)] = True
    
    return symmetric_pairs

# Example usage
pairs = [(1, 2), (2, 1), (3, 4), (4, 5), (5, 4)]
result = find_symmetric_pairs(pairs)

print("Symmetric pairs:", result)
