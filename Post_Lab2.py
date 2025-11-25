# Program to calculate area and perimeter of a rectangle

# Input length and width from the user
length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))

# Calculate area and perimeter
area = length * width
perimeter = 2 * (length + width)

# Display results
print("Area of Rectangle:", area)
print("Perimeter of Rectangle:", perimeter)

# Program to test if a number is even or odd

num = int(input("Enter a number: "))

if num % 2 == 0:
    print(num, "is Even")
else:
    print(num, "is Odd")

# Program to calculate the surface area and volume of a cube

side = float(input("Enter the side length of the cube: "))

# Surface area of a cube = 6a²
surface_area = 6 * (side ** 2)

# Volume of a cube = a³
volume = side ** 3

print("Surface Area of the Cube:", surface_area)
print("Volume of the Cube:", volume)

# Program to solve the equation z = (x + y) * (x - y)

x = float(input("Enter value of x: "))
y = float(input("Enter value of y: "))

z = (x + y) * (x - y)

print("Value of z =", z)

# Program to convert Celsius to Fahrenheit

celsius = float(input("Enter temperature in Celsius: "))

fahrenheit = (celsius * 9/5) + 32

print("Temperature in Fahrenheit:", fahrenheit)
