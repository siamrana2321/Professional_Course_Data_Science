################ 12. Convert minutes to hours and minutes ################
minutes = int(input("Enter minutes: "))

hours = minutes // 60
remaining_minutes = minutes % 60

print("Hours:", hours)
print("Minutes:", remaining_minutes)