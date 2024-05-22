################ 4. Calculate area of an equilateral triangle ################
import math

side = float(input("Enter the side length of the equilateral triangle: "))
area = (math.sqrt(3) / 4) * (side ** 2)
print("Area of equilateral triangle:", area)