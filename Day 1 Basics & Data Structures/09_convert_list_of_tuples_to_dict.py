
# Question 9: Convert a list of tuples into a dictionary.
# Hint: Use the `dict()` function or iterate through the list manually to add key-value pairs to a dictionary.
# Steps:
# 1. Create a list of tuples where each tuple has two elements: a key and a value (e.g., [('a', 1), ('b', 2)]).
# 2. Convert this list into a dictionary.
# 3. Print the resulting dictionary to verify the output.

# Expected Input:
#   input_list = [('a', 1), ('b', 2), ('c', 3)]
# Expected Output:
#   {'a': 1, 'b': 2, 'c': 3}

# Write your solution below this line:

input_list = [('a', 1), ('b', 2), ('c', 3)]
new_dict = dict(input_list)
print(new_dict)

# For loop
new_dict_loop = {}

for key, value in input_list:
    new_dict_loop[key] = value

print(new_dict_loop)


# NOTES:
# `dict()` function can be used to convert a list of tuples into a dictionary.
# When using a for loop, unpack the key-value pairs directly in the loop header for easy access to each element.
