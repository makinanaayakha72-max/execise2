# Question 2: Comparison and Logical Operators
a = int(input("Enter the value for a: "))
b = int(input("Enter the value for b: "))
c = int(input("Enter the value for c: "))
# TODO: Create a condition that checks if a is greater than b
# 1. Get user input


# 2. Check the condition
if a > b:
    print(f"Success: {a} is greater than {b}")
else:
    print(f"Notice: {a} is less than or equal to {b}")

# TODO: Create a condition that checks if b is even (hint: use the modulus operator)
if b % 2 == 0:
    print("b is even")
else:
    print("b is odd")
# TODO: Create a condition that checks if c is less than or equal to a
if c <= a:
    print("c is less than or equal to a")
else:
    print("c is greater than a")
# TODO: Combine the above conditions using logical operators to create a 'final_condition'
#       The 'final_condition' should be True if either:
#       - a is greater than b, or
#       - b is even and c is less than or equal to a

final_condition = (a > b) or (b % 2 == 0 and c <= a)

print(f"The final_condition is: {final_condition}")
