
# Question 17: Generate a list of prime numbers up to a given number.
# Hint: Use a loop to check divisibility for numbers from 2 to the given number.
# Steps:
# 1. Create a function that takes an integer `n` as input.
# 2. Use a loop to check each number from 2 to `n` for primality.
# 3. Append prime numbers to a list and return the list.
# 4. Print the list of prime numbers.

# Expected Input:
#   n = 10
# Expected Output:
#   [2, 3, 5, 7]

# Write your solution below this line:

n = 10
primes = []

for i in range(2, n + 1):
    is_prime = True

    for j in range (2, int(i ** 0.5) + 1):
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(i)

print(primes)



# NOTES:
# - Created a variable to store the prime numbers
# - Iterated through the range of 2 to n
# - Created a variable to store whether the number is prime or not
# - Iterated through the range of 2 to the square root of i + 1
# - Checked if i is divisible by j
# - Appended i to the primes list if i is prime