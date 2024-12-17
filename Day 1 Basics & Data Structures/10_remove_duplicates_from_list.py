
# Question 10: Remove duplicate elements from a list.
# Hint: Use a set to eliminate duplicates or iterate through the list manually to check for duplicates.
# Steps:
# 1. Create a list with duplicate elements (e.g., [1, 2, 2, 3, 4, 4, 5]).
# 2. Remove the duplicate elements while maintaining the order of the unique elements.
# 3. Print the resulting list to verify the output.

# Expected Input:
#   input_list = [1, 2, 2, 3, 4, 4, 5]
# Expected Output:
#   [1, 2, 3, 4, 5]

# Write your solution below this line:

input_list = [1, 2, 2, 3, 4, 4, 5]

unique_list = list(set(input_list))
print(unique_list)

# For loop
unique_list_loop = []
for i in input_list:
    if i not in unique_list_loop:
        unique_list_loop.append(i)

print(unique_list_loop)

# dict.fromkeys()
unique_list_dict = list(dict.fromkeys(input_list))
print(unique_list_dict)



# NOTES:
# - The set() function is used to eliminate duplicates from a list.
# - Check if an element is already in the unique list before appending it to avoid duplicates.
# - `append()` method is used to add elements to a list.
# - `dict.fromkeys()` can be used to remove duplicates while preserving the order of elements in the list.