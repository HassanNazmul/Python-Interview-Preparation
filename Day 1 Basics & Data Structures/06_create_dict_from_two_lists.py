
# Question 6: Create a dictionary from two lists: one with keys and the other with values.
# Hint: Use the `zip()` function to pair keys and values together, or iterate through both lists manually.
# Steps:
# 1. Create two lists of the same length, one for keys (e.g., ['a', 'b', 'c']) and one for values (e.g., [1, 2, 3]).
# 2. Combine the lists into a dictionary where each key is paired with its corresponding value.
# 3. Print the resulting dictionary to verify the output.

# Expected Input:
#   keys = ['a', 'b', 'c']
#   values = [1, 2, 3]
# Expected Output:
#   {'a': 1, 'b': 2, 'c': 3}

# Write your solution below this line:

keys = ['a', 'b', 'c']
values = [1, 2, 3]

result_dict = dict(zip(keys, values))
print(result_dict)

# For loop to create a dictionary
result_dict = {}
for key, value in zip(keys, values):
    result_dict[key] = value

print(result_dict)



# NOTES:
# - The `zip()` function is a useful tool for combining two lists into a single dictionary.
# - The `dict()` function can be used to convert a list of key-value pairs into a dictionary.
# - When using a for loop to create a dictionary, you can iterate through both lists simultaneously using the `zip()` function.