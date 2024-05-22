################ 17. Find the maximum between three numbers ################
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))

if num1 >= num2 and num1 >= num3:
    print("Maximum number:", num1)
elif num2 >= num1 and num2 >= num3:
    print("Maximum number:", num2)
else :
    print("Maximum number:", num3)

