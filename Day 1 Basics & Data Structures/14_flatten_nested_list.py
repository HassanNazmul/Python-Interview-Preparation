
# Question 14: Flatten a nested list.
# Hint: Use nested loops or recursion to extract all elements from sublists into a single list.
# Steps:
# 1. Create a nested list with sublists (e.g., [[1, 2], [3, 4], [5, 6]]).
# 2. Flatten the nested list so that all elements appear in a single list.
# 3. Print the resulting flattened list to verify the output.

# Expected Input:
#   nested_list = [[1, 2], [3, 4], [5, 6]]
# Expected Output:
#   [1, 2, 3, 4, 5, 6]

# Write your solution below this line:

nested_list = [[1, 2], [3, 4], [5, 6]]
flattened_list = []

for i in nested_list:
    for j in i:
        flattened_list.append(j)

print(flattened_list)



# NOTES:
# - Nested lists are lists that contain other lists as elements.
# - `for i in nested_list` iterates over each sublist in the nested list.
# - `for j in i` iterates over each element in the sublist.
# - `flattened_list.append(j)` adds each element to the `flattened_list`.