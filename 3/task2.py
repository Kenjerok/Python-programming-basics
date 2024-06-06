import math

def compare_point_distances(x1, y1, x2, y2):
    distance_point_A = math.sqrt(x1**2 + y1**2)
    distance_point_B = math.sqrt(x2**2 + y2**2)

    if distance_point_A < distance_point_B:
        return "Точка A знаходиться ближче до початку координат."
    elif distance_point_B < distance_point_A:
        return "Точка B знаходиться ближче до початку координат."
    else:
        return "Точки знаходяться на однаковій відстані до початку координат."

coordinate_x1 = float(input("Введіть координату x першої точки (A): "))
coordinate_y1 = float(input("Введіть координату y першої точки (A): "))
coordinate_x2 = float(input("Введіть координату x другої точки (B): "))
coordinate_y2 = float(input("Введіть координату y другої точки (B): "))

comparison_result = compare_point_distances(coordinate_x1, coordinate_y1, coordinate_x2, coordinate_y2)
print(comparison_result)
