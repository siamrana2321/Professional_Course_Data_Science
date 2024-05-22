################ 25. Check eligibility for admission to a professional course ################
maths = float(input("Enter marks in Maths: "))
physics = float(input("Enter marks in Physics: "))
chemistry = float(input("Enter marks in Chemistry: "))

if (maths >= 65 and physics >= 55 and chemistry >= 50) or (maths + physics + chemistry >= 180) or (maths + physics >= 140):
    print("Eligible for admission.")
else:
    print("Not eligible for admission.")