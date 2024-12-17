
# Question 13: Remove all occurrences of a specific element from a list.
# Hint: Use a loop or list comprehension to filter out the target element.
# Steps:
# 1. Create a list of elements with some repeated occurrences (e.g., [1, 2, 3, 2, 4, 2, 5]).
# 2. Remove all occurrences of a specific element (e.g., 2).
# 3. Print the resulting list to verify the output.

# Expected Input:
#   input_list = [1, 2, 3, 2, 4, 2, 5]
#   target = 2
# Expected Output:
#   [1, 3, 4, 5]

# Write your solution below this line:

input_list = [1, 2, 3, 2, 4, 2, 5]
target = 2

new_list = []

for i in input_list:
    if i != target:
        new_list.append(i)

print(new_list)



# NOTES:
# - The loop iterates through each element in the input list.
# - The if condition filters out the target element.
# - The append method adds non-target elements to the new list.
# - The resulting list contains all elements except the target.