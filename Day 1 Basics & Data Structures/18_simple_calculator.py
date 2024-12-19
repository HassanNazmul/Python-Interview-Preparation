
# Question 18: Implement a simple calculator using functions.
# Hint: Create separate functions for each operation (addition, subtraction, multiplication, division).
# Steps:
# 1. Define functions for addition, subtraction, multiplication, and division.
# 2. Prompt the user for two numbers and an operation.
# 3. Perform the selected operation using the corresponding function.
# 4. Print the result of the operation.

# Expected Input:
#   num1 = 10, num2 = 5, operation = '+'
# Expected Output:
#   15

# Write your solution below this line:

# Define the operations as functions
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

# Inputs
num1 = 10
num2 = 5
operation = '+'

# Perform the operation
if operation == '+':
    total = add(num1, num2)
elif operation == '-':
    total = subtract(num1, num2)
elif operation == '*':
    total = multiply(num1, num2)
elif operation == '/':
    total = divide(num1, num2)
else:
    total = "Invalid operation"

# Output the result
print(total)



# NOTES:
# - The code defines four functions for addition, subtraction, multiplication, and division.
# - The code prompts the user for two numbers and an operation.
# - The code performs the selected operation using the corresponding function.
# - The code prints the result of the operation.