
# Question 7: Merge two dictionaries into one.
# Hint: Use the `update()` method or dictionary unpacking to combine dictionaries.
# Steps:
# 1. Create two dictionaries (e.g., {'a': 1, 'b': 2} and {'c': 3, 'd': 4}).
# 2. Merge these dictionaries into a single dictionary.
# 3. Print the resulting dictionary to verify the output.

# Expected Input:
#   dict1 = {'a': 1, 'b': 2}
#   dict2 = {'c': 3, 'd': 4}
# Expected Output:
#   {'a': 1, 'b': 2, 'c': 3, 'd': 4}

# Write your solution below this line:

dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}

dict1.update(dict2)
print(dict1)

# For loop to update Dictionary
merged_dict = dict1.copy()
for key, value in dict2.items():
    merged_dict[key] = value

print(merged_dict)


# NOTES:
# - The `update()` method is the most common way to merge two dictionaries.
# - The `update()` method modifies the original dictionary in place.
# - For loop can also be used to update the dictionary, but it is less efficient than the `update()` method.