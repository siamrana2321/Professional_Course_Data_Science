################ 27. Evaluate the value of (a+b) / (c-d) ################
a = float(input("Enter value of a: "))
b = float(input("Enter value of b: "))
c = float(input("Enter value of c: "))
d = float(input("Enter value of d: "))

if c - d != 0:
    result = (a + b) / (c - d)
    print("The result of (a + b) / (c - d) is:", result)
else:
    print("Division by zero is not allowed.")