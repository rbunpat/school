#ask for radius and height
radius = int(input("What is the radius of the cylinder? "))
height = int(input("What is the height of the cylinder? "))
#calculate volume
volume = 3.14 * radius * radius * height
#calculate circle area from radius
area = 3.14 * radius * radius
#calculate circle perimeter from radius
perimeter = 2 * 3.14 * radius
#print out the result
print("The perimeter of the cylinder is " + str(perimeter))
print("The area of the cylinder is " + str(area))
print("The volume of the cylinder is " + str(volume))
