#Anthony Guzman          3.18           CIS2348
paintColors = {'red':35, 'blue':25, 'green':23}

h = int(input("Enter wall height (feet):\n"))

w = int(input("Enter wall width (feet):\n"))

area = h*w
round(area)
print("Wall area:",area,"square feet")

galls = area / 350

print("Paint needed:","{0:.2f}".format(galls), "gallons")

cans = round(galls)

print("Cans needed:",cans,"can(s)")

color = input("\nChoose a color to paint the wall:\n")

print("Cost of purchasing "+ color +" paint: $"+str(cans*paintColors[color]))