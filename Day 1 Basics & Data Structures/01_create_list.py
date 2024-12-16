
# Question 1: Create a list of the first 10 natural numbers.
# Hint: Think about the range function and how to convert it into a list.
# Steps:
# 1. Use a loop or a built-in function to generate numbers from 1 to 10.
# 2. Store the generated numbers in a list.
# 3. Print the list to verify the output.

# Write your solution below this line:

def natural_number():

    numbers = []

    for i in range(1, 11):
        numbers.append(i)

    return numbers

print(natural_number())



# NOTES:
# - The range function generates numbers from the starting value to the end value.
# - The list function converts the range object into a list.
# - The append method adds elements to the list.