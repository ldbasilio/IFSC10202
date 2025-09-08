from math import sin, cos, acos, pi

print ("The Great Circle Calculator")
radius = float(input("Enter the Radius (6371): "))
firstX1 = float(input("First Point - Latitude: "))
firstY1 = float(input("First Point - Longitude: "))
secondX2 = float(input("Second Point - Latitude: "))
secondY2 = float(input("Second Point - Longitude: "))

finalX1 = firstX1 * pi / 180
finalX2 = secondX2 * pi / 180
finalY1 = firstY1 * pi / 180
finalY2 = secondY2 * pi / 180

formula = radius * acos(
    sin(finalX1) * sin(finalX2)
    + cos(finalX1) * cos(finalX2) * cos(finalY1 - finalY2)
)

print (round(formula, 2))