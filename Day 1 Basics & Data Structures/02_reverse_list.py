
# Question 2: Reverse a list without using the `reversed()` function.
# Hint: Think about slicing and how to iterate over a list in reverse.
# Steps:
# 1. Create a list of your choice (e.g., [1, 2, 3, 4, 5]).
# 2. Reverse the list using slicing or a loop.
# 3. Print the reversed list to verify the output.

# Write your solution below this line:

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

reversed_list = list(reversed(numbers))
print(reversed_list)

# For loop
reversed_list = []

for number in numbers:
    reversed_list.insert(0, number)
    
print(reversed_list)

# Slicing
reversed_list = numbers[::-1]

print(reversed_list)



# NOTES:
# - The insert method adds elements to a list at a specific index.
# - The slicing method reverses the list by stepping backward through the list.
# - The reversed function returns a reverse iterator that can be converted into a list using the list function