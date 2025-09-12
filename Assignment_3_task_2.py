# Task 6: Math module operations

import math

# Ask user for input
num = float(input("Enter a number: "))

# Calculations
sqrt_val = math.sqrt(num)
log_val = math.log(num)       # natural logarithm (base e)
sine_val = math.sin(num)      # sine (argument in radians)

# Display results
print(f"Square root of {num} is: {sqrt_val}")
print(f"Natural logarithm of {num} is: {log_val}")
print(f"Sine of {num} (in radians) is: {sine_val}")
