# Task 1: Check if a Number is Even or Odd
# Problem Statement:  Write a Python program that:
# 1. 	Takes an integer input from the user.
# 2. 	Checks whether the number is even or odd using an if-else statement.
# 3. 	Displays the result accordingly.
# Expected Output:
# The program should return an output like


x = int(input("Enter an integer: "))
if x % 2 == 0:
    print(f"{x} is an even number.")
else:
    print(f"{x} is an odd number.")


# Task 2: Sum of Integers from 1 to 50 Using a Loop
sum = 0 
for i in range(1,51):
    sum = sum + i

print(f"The Total sum of integers from 1 to 50 is: {sum}")

# Problem Statement: Write a Python program that:
# 1.   Uses a for loop to iterate over numbers from 1 to 50.
# 2.   Calculates the sum of all integers in this range.
# 3.   Displays the final sum.

# Initialize sum variable
total_sum = 0

for number in range(1, 51):
    total_sum += number  

print("The sum of numbers from 1 to 50 is:", total_sum)

