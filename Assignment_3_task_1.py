def factorial(n):
    if(n==1 or n==0):
        return 1
    return factorial(n-1) * n

# Sample number
num = 6
print(f"Factorial of {num} is: {factorial(num)}")    