# Task 1: Calculate Factorial Using a Function 


# Problem Statement: Write a Python program that:
# 1.   Defines a function named factorial that takes a number as an argument and calculates its factorial 
# using a loop or recursion.
# 2.   Returns the calculated factorial.
# 3.   Calls the function with a sample number and prints the output.


# def factorial(n) :
#     result = 1
#     for i in range(1, n  ):
#         result *= i
#     return result

# num = 5
# print(f"Factorial of {num} is {factorial(num)}")

# Task 2: Using the Math Module for Calculations
 
# Problem Statement: Write a Python program that:
# 1.   Asks the user for a number as input.
# 2.   Uses the math module to calculate the:
# o   Square root of the number
# o   Natural logarithm (log base e) of the number
# o   Sine of the number (in radians)

import math


num = float(input("Enter a number: "))

Sqrt = math.sqrt(num)
Log = math.log(num)         
Sine = math.sin(num)      

# Step 3: Print results
print(f"Square root : {num} is {Sqrt}");
print(f"logarithm : {num} is {Log}");
print(f"Sine : {num} radians is {Sine}");
