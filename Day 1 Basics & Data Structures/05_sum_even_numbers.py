
# Question 5: Sum all the even numbers in a list.
# Hint: Use a loop to iterate through the list and check if each element is even using the modulus operator (%).
# Steps:
# 1. Create a list of integers (e.g., [1, 2, 3, 4, 5, 6]).
# 2. Identify the even numbers using the condition `number % 2 == 0`.
# 3. Sum the even numbers and store the result in a variable.
# 4. Print the sum to verify the output.

# Expected Input: [1, 2, 3, 4, 5, 6]
# Expected Output: 12 (2 + 4 + 6)

# Write your solution below this line:

number_list = [1, 2, 3, 4, 5, 6]
even_sum = 0

for i in number_list:
    if i % 2 == 0:
        even_sum += i

print(even_sum)

# Using list comprehension
number_list = [1, 2, 3, 4, 5, 6]
even_sum = sum([i for i in number_list if i % 2 == 0])
print(even_sum)



# NOTES:
# - Use the modulus operator (%) to check if a number is even.
# - Loop through the list and sum the even numbers.
# - The sum can be stored in a variable and printed as the final result.
# - List comprehension can also be used to simplify the code.