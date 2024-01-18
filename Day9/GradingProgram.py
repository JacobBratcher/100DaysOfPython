student_scores = {
  "Harry": 81,
  "Ron": 78,
  "Hermione": 99, 
  "Draco": 74,
  "Neville": 62,
}
# 🚨 Don't change the code above 👆
# TODO-1: Create an empty dictionary called student_grades.
student_grades = {}

# TODO-2: Write your code below to add the grades to student_grades.👇
for student in student_scores:
    score = student_scores[student]
    grade = ""  # Initialize the grade variable
    if score > 90: 
        grade = "Outstanding"
    elif score > 80 and score < 91: 
        grade = "Exceeds Expectations"
    elif score > 70 and score < 81:
        grade = "Acceptable"
    elif score < 71: 
        grade = "Fail"
    student_grades[student] = grade

# 🚨 Don't change the code below 👇
print(student_grades)
