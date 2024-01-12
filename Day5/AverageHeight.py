# Input a Python list of student heights
student_heights = input().split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n]) # type: ignore
# 🚨 Don't change the code above 👆
  
# Write your code below this row 👇
total_height = 0 
for height in student_heights:
    total_height += height # type: ignore
print(f"total height = {total_height}")

student_amt = 0 
for amount in student_heights:
    student_amt += 1
print (f"number of students = {student_amt}")

avg_height = total_height / student_amt
rounded_height = round(avg_height)
print(f"average height = {rounded_height}")