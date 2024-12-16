
# Question 4: Count the occurrences of each element in a list.
# Hint: Use a dictionary to store elements as keys and their counts as values.
# Steps:
# 1. Create a list with duplicate elements (e.g., [1, 2, 2, 3, 3, 3, 4]).
# 2. Iterate through the list and count the occurrences of each element.
# 3. Store the results in a dictionary.
# 4. Print the dictionary to verify the output.

# Expected Input: [1, 2, 2, 3, 3, 3, 4]
# Expected Output:
#   {1: 1, 2: 2, 3: 3, 4: 1}

# Write your solution below this line:

number_list = [1, 2, 2, 3, 3, 3, 4]

sorted_list = {}

for i in number_list:
    if i in sorted_list:
        sorted_list[i] += 1
    else:
        sorted_list[i] = 1

print(sorted_list)

# Collectiosn module can be used to simplify the code
from collections import Counter

number_list = [1, 2, 2, 3, 3, 3, 4]
count_dict = Counter(number_list)
print(count_dict)


# NOTES:
# - A dictionary is a useful data structure for counting occurrences of elements.
# - Loop through the list and update the count for each element in the dictionary.
# - The final dictionary will contain elements as keys and their counts as values.