################ 20. Check whether a number is divisible by 5 or 11 or not ################
num = int(input("Enter a number: "))

if num % 5 == 0 or num % 11 == 0:
    print("Divisible by 5 or 11")
else:
    print("Not divisible by 5 or 11")