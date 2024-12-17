
# Question 11: Check if a list is a palindrome.
# Hint: A list is a palindrome if it reads the same forward and backward. Use slicing or a loop to check this condition.
# Steps:
# 1. Create a list of elements (e.g., [1, 2, 3, 2, 1]).
# 2. Compare the list with its reversed version to check if it's a palindrome.
# 3. Print "Palindrome" if it is, or "Not a palindrome" otherwise.

# Expected Input:
#   input_list = [1, 2, 3, 2, 1]
# Expected Output:
#   Palindrome

# Write your solution below this line:

input_list = [1, 2, 3, 2, 1]
reversed_list = input_list[::-1]

if input_list == reversed_list:
    print("Palindrome")
else:
    print("Not a palindrome")


# Using a for loop
is_palindrome = True

for i in range(len(input_list) // 2):
    if input_list[i] != input_list[-(i + 1)]:
        is_palindrome = False
        break

if is_palindrome:
    print("Palindrome")
else:
    print("Not a palindrome")



# NOTES:
# - [::-1] is a slicing technique that reverses the list.
# - len() returns the length of the list.
# - The // operator performs integer division.
# - The range() function generates a sequence of numbers.
# - [-(i + 1)] accesses elements from the end of the list.
# - The break statement exits the loop prematurely.