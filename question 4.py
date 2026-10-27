# Question 4: Combining Operators and Conditionals

# TODO: Ask the user to input two numbers and store them in variables 'num1' and 'num2'

num1 = int(input("Enter the first number (num1): "))
num2 = int(input("Enter the second number (num2): "))
operation = input("Choose an operation (+, -, *, /): ").strip()


if operation == "+":
    result = num1 + num2
    print(f"Result: {num1} + {num2} = {result}")

elif operation == "-":
    result = num1 - num2
    print(f"Result: {num1} - {num2} = {result}")

elif operation == "*":
    result = num1 * num2
    print(f"Result: {num1} * {num2} = {result}")

elif operation == "/":
    
    if num2 == 0:
        print("Error: Cannot divide by zero.")
    else:
        result = num1 / num2
        print(f"Result: {num1} / {num2} = {result}")

else:
    print("Invalid operation! Please choose +, -, *, or /.")

