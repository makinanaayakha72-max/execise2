# Question 3: Conditional Statements

# TODO: Ask the user to input a test score (0-100) and store it in a variable called 'score'
score = int(input("Enter a test score (0-100): "))
# TODO: Implement a grading system using if-elif-else statements:
#       90-100: A
#       80-89: B
#       70-79: C
#       60-69: D
#       Below 60: F
  
score = int(input("Enter the student's score: "))

if 90 <= score <= 100:
    grade = "A"
elif 80 <= score <= 89:
    grade = "B"
elif 70 <= score <= 79:
    grade = "C"
elif 60 <= score <= 69:
    grade = "D"
elif 0 <= score < 60:
    grade = "F"
else:
    grade = "Invalid score! Please enter a value between 0 and 100."
# TODO: Print the grade for the given score
print(f"Grade: {grade}")