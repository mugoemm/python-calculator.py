# Simple calculator using basic Python

# Get inputs from the user
num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")
operation = input("Enter an operation (+, -, *, /): ")

# Convert inputs to numbers
num1 = float(num1)
num2 = float(num2)

# Show all results (since no if-else yet)
print("Results:")
print("Addition:", num1 + num2)
print("Subtraction:", num1 - num2)
print("Multiplication:", num1 * num2)
print("Division:", num1 / num2)