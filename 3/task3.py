def validate_triangle(angle_a, angle_b):
    if angle_a + angle_b >= 180:
        return "Такий трикутник не існує, оскільки сума кутів перевищує або дорівнює 180 градусів."
    else:
        result = "Такий трикутник існує.\n"
        if angle_a == 90 or angle_b == 90 or (180 - angle_a - angle_b) == 90:
            result += "Трикутник є прямокутним."
        else:
            result += "Трикутник не є прямокутним."
        return result

angle_a = float(input("Введіть величину першого кута трикутника (в градусах): "))
angle_b = float(input("Введіть величину другого кута трикутника (в градусах): "))

validation_result = validate_triangle(angle_a, angle_b)
print(validation_result)
