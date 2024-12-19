
# Question 16: Given a list of dictionaries, find the dictionary with the highest value for a specific key.
# Hint: Use a loop or the `max()` function with a key parameter to find the desired dictionary.
# Steps:
# 1. Create a list of dictionaries with numeric values for a specific key (e.g., [{'a': 5}, {'a': 10}, {'a': 3}]).
# 2. Identify the dictionary with the highest value for the key 'a'.
# 3. Print the resulting dictionary.

# Expected Input:
#   input_list = [{'a': 5}, {'a': 10}, {'a': 3}]
# Expected Output:
#   {'a': 10}

# Write your solution below this line:

input_list = [{'a': 5}, {'b': 10}, {'c': 3}]

max_value = max(input_list, key=lambda x: list(x.values())[0])
print(max_value)

# Usinf for loop
max_dict = input_list[0]

for i in input_list:
    for key, valuse in i.items():
        if valuse > list(max_dict.values())[0]:
            max_dict = i

print(max_dict)

# Usinf for loop and if condition
max_dict = input_list[0]

for i in input_list:
    if list(i.values())[0] > list(max_dict.values())[0]:
        max_dict = i

print(max_dict)

# NOTES:
# - The `max()` function can find the maximum value in a list based on a specific key.
# - The `key` parameter specifies the function used to extract the comparison key.
# - In this case, a lambda function extracts the value of the key 'a' from each dictionary.
# - `values()` returns a view object that displays a list of all the values in the dictionary.
# - The `list()` function converts the view object to a list to access the first element.

# How for loop works:
# - `max_dict` is stored as the first dictionary in the list.
# - `for i in input_list:` is checking each dictionary in the list.
# - `for key, value in i.items():` is checking each key-value pair in the dictionary.
# - `if value > list(max_dict.values())[0]:` is comparing the value with the current maximum value.
# - If the value is greater, the dictionary is updated as the new maximum value.
