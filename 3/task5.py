def determine_point_location(x, y):
    if x == 0 and y == 0:
        return "The point is at the origin."
    elif x == 0:
        return "The point is on the Y-axis."
    elif y == 0:
        return "The point is on the X-axis."
    else:
        if x > 0:
            if y > 0:
                return "The point is in the first quadrant."
            else:
                return "The point is in the fourth quadrant."
        else:
            if y > 0:
                return "The point is in the second quadrant."
            else:
                return "The point is in the third quadrant."

x = float(input("Enter the x-coordinate of point A: "))
y = float(input("Enter the y-coordinate of point A: "))

location_result = determine_point_location(x, y)
print(location_result)
