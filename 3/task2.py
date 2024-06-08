import math

def compare_point_distances(x1, y1, x2, y2):
    distance_point_A = math.sqrt(x1**2 + y1**2)
    distance_point_B = math.sqrt(x2**2 + y2**2)

    if distance_point_A < distance_point_B:
        return "Point A is closer to the origin."
    elif distance_point_B < distance_point_A:
        return "Point B is closer to the origin."
    else:
        return "Both points are at the same distance from the origin."

coordinate_x1 = float(input("Enter the x-coordinate of the first point (A): "))
coordinate_y1 = float(input("Enter the y-coordinate of the first point (A): "))
coordinate_x2 = float(input("Enter the x-coordinate of the second point (B): "))
coordinate_y2 = float(input("Enter the y-coordinate of the second point (B): "))

comparison_result = compare_point_distances(coordinate_x1, coordinate_y1, coordinate_x2, coordinate_y2)
print(comparison_result)
