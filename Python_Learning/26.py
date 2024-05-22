################ 26. Display message based on temperature state ################
temp = float(input("Enter the temperature in centigrade: "))

if temp < 0:
    print("Freezing weather")
elif temp <= 10:
    print("Very cold weather")
elif temp <= 20:
    print("Cold weather")
elif temp <= 30:
    print("Normal in temperature")
elif temp <= 40:
    print("It's hot")
else:
    print("It's very hot")