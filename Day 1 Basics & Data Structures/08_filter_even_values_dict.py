
# Question 8: Filter a dictionary to keep only even values.
# Hint: Use dictionary comprehension or a for loop to check each value and include it only if it's even.
# Steps:
# 1. Create a dictionary with integer values (e.g., {'a': 1, 'b': 2, 'c': 3, 'd': 4}).
# 2. Filter the dictionary to keep only keys with even values.
# 3. Print the resulting dictionary to verify the output.

# Expected Input:
#   input_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
# Expected Output:
#   {'b': 2, 'd': 4}

# Write your solution below this line:

input_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
even_dict = {}

for key, value in dict.items():
    if value % 2 == 0:
        even_dict[key] = value

print(even_dict)



# NOTES:
# - The `items` method is used to access both keys and values in the dictionary.
# - The `%` operator checks if a number is divisible by 2 (i.e., even).
# - The filtered key-value pairs are added to the new dictionary.