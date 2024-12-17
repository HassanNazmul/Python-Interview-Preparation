
# Question 12: Find common elements between two lists.
# Hint: Use a set intersection or iterate through both lists to find common elements.
# Steps:
# 1. Create two lists with some overlapping elements (e.g., [1, 2, 3, 4] and [3, 4, 5, 6]).
# 2. Identify and store the common elements between the two lists.
# 3. Print the resulting list of common elements.

# Expected Input:
#   list1 = [1, 2, 3, 4]
#   list2 = [3, 4, 5, 6]
# Expected Output:
#   [3, 4]

# Write your solution below this line:

list1 = [1, 2, 3, 4]
list2 = [3, 4, 5, 6]

common = list(set(list1) & set(list2))
print(common)


# Using a for loop
common_loop = []

for i in list1:
    if i in list2:
        common_loop.append(i)

print(common_loop)



# NOTES:
# - for i in list1: iterates through each element in list1.
# - if i in list2: checks if the element i is in list2.
# - common.append(i): adds the common element i to the common list.


# set1 = {1, 2, 3, 3}
# set2 = {3, 4, 5, 6}

# # Remove duplicates (set stores only unique values)
# print(set1)  # Output: {1, 2, 3}

# # Intersection: Elements common to both sets
# print(set1 & set2)  # Output: {3}

# # Union: All unique elements from both sets
# print(set1 | set2)  # Output: {1, 2, 3, 4, 5, 6}

# # Difference: Elements in set1 but not in set2
# print(set1 - set2)  # Output: {1, 2}

# # Symmetric Difference: Unique elements in set1 and set2
# print(set1 ^ set2)  # Output: {1, 2, 4, 5}

# # Equivalent methods
# print(set1.intersection(set2))  # Output: {3}
# print(set1.union(set2))         # Output: {1, 2, 3, 4, 5, 6}
# print(set1.difference(set2))    # Output: {1, 2}
# print(set1.symmetric_difference(set2))  # Output: {1, 2, 4, 5}