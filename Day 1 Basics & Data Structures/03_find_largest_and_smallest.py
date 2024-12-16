
# Question 3: Find the largest and smallest elements in a list.
# Hint: Use the max() and min() functions for a simple approach, or use loops to find these values manually.
# Steps:
# 1. Create a list of integers (e.g., [3, 1, 4, 1, 5, 9, 2]).
# 2. Identify the largest element.
# 3. Identify the smallest element.
# 4. Print both values to verify the output.

# Expected Input: [3, 1, 4, 1, 5, 9, 2]
# Expected Output:
#   Largest element: 9
#   Smallest element: 1

# Write your solution below this line:

numbers = [3, 1, 4, 1, 5, 9, 2]

# max() function
max_number = max(numbers)
print("Max Number:", max_number)

# min() function
min_number = min(numbers)
print("Min Number:", min_number)

# for loop
def max_min():
    numbers = [3, 1, 4, 1, 5, 9, 2]
    max_number, min_number = numbers[0], numbers[0]

    for i in numbers:
        if i > max_number:
            max_number = i
        if i < min_number:
            min_number = i

    print("Max Number:", max_number)
    print("Min Number:", min_number)

max_min()




# NOTES:
# - The max() and min() functions are the simplest way to find the largest and smallest elements in a list.
# - loop through the list to find the largest and smallest elements manually.