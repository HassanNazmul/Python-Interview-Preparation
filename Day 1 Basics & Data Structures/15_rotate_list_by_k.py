
# Question 15: Write a function to rotate a list by 'k' elements.
# Hint: Use slicing to rearrange the list or a loop to shift elements manually.
# Steps:
# 1. Create a list of elements (e.g., [1, 2, 3, 4, 5]).
# 2. Rotate the list to the right by 'k' positions (e.g., k=2).
# 3. Print the rotated list to verify the output.

# Expected Input:
#   input_list = [1, 2, 3, 4, 5]
#   k = 2
# Expected Output:
#   [4, 5, 1, 2, 3]

# Write your solution below this line:

input_list = [1, 2, 3, 4, 5]
k = 2

rotated_list = (input_list[-k:] + input_list[:-k])
print(rotated_list)

# Using for loop
k = k % len(input_list)

for _ in range(k):
    input_list.insert(0, input_list.pop())

print(input_list)


# Using While Loop
k = k % len(input_list)

while k > 0:
    input_list.insert(0, input_list.pop())
    k -= 1

print(input_list)

# NOTES:
# - K is the number of elements to rotate the list.
# - :-k is the list from the beginning to the kth element from the end.
# - -k: is the list from the kth element from the end to the end.
# - The rotated list is the concatenation of the two slices.
# - The modulo operator (%) is used to handle cases where k > len(input_list).
