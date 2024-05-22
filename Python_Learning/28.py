################ 28. Determine the grade using a grading system ################
marks = int(input("Enter the marks: "))

if 90 <= marks <= 100:
    grade = "A"
elif 87 <= marks < 90:
    grade = "B+"
elif 84 <= marks < 87:
    grade = "B"
elif 80 <= marks < 84:
    grade = "B-"
elif 77 <= marks < 80:
    grade = "C+"
elif 74 <= marks < 77:
    grade = "C"
elif 70 <= marks < 74:
    grade = "C-"
elif 65 <= marks < 70:
    grade = "D+"
elif 60 <= marks < 65:
    grade = "D"
else:
    grade = "F"

print("The grade is:", grade)