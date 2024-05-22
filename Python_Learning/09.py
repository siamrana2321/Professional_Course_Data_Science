################ 9. Calculate total, average, and percentage of marks in five subjects ################
marks = []
total_marks = 0

for i in range(5):
    subject_marks = float(input(f"Enter marks of subject {i+1}: "))
    marks.append(subject_marks)
    total_marks += subject_marks

average = total_marks / 5
percentage = (total_marks / 500) * 100

print("Total marks:", total_marks)
print("Average marks:", average)
print("Percentage:", percentage)