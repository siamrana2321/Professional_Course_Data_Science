################ 5. Calculate perimeter and area of a circle ################
import math

radius = float(input("Enter the radius of the circle: "))
perimeter = 2 * math.pi * radius
area = math.pi * (radius ** 2)

print("Perimeter of circle:", perimeter)
print("Area of circle:", area)