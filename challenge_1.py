#Ask the user to type in the lengths of the three sides of a triangle
#Calculate the area of the triangle.
# s = (side1+side2+side3)/2
# area = (sqrt) (s(s-a)*(s-b)*(s-c))

import math

side1 = int(input("Please, enter the length of the first side of this triangle: "))
side2 = int(input("What about the length of the second side of this triangle: "))
side3 = int(input("And now for the third length of this triangle: "))

s = (side1+side2+side3)/2

square_calculation = (s*(s-side1)*(s-side2)*(s-side3))

area = math.sqrt(square_calculation)

print(f"The area of the triangle is: {area}")

#I feel the approach for the calculation is accurate, but I believe I should define whether the triangle is valid or not according to the sides provided 
# and make sure numbers are bigger than 0, with if statements.