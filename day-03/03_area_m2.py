#Write a Python program that captures the length and
#width of a rectangle in metres, calculates the area,
#and displays the result to two decimal places with the unit m².
length = float(input("Enter length in metres: "))
width = float(input("Enter width in metres: "))

area = length * width

print(f"Area: {area:.2f} m²")
