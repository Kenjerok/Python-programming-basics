def determine_point_location(coord_x, coord_y):
    if coord_x == 0 and coord_y == 0:
        return "Точка знаходиться в початку координат."
    elif coord_x == 0:
        return "Точка знаходиться на вісі Y."
    elif coord_y == 0:
        return "Точка знаходиться на вісі X."
    else:
        if coord_x > 0:
            if coord_y > 0:
                return "Точка знаходиться в першому квадранті."
            else:
                return "Точка знаходиться в четвертому квадранті."
        else:
            if coord_y > 0:
                return "Точка знаходиться в другому квадранті."
            else:
                return "Точка знаходиться в третьому квадранті."

coord_x = float(input("Введіть координату x точки A: "))
coord_y = float(input("Введіть координату y точки A: "))

location_result = determine_point_location(coord_x, coord_y)
print(location_result)
