def validate_triangle(angle_a, angle_b):
    if angle_a + angle_b >= 180:
        return "Such a triangle does not exist, as the sum of the angles is greater than or equal to 180 degrees."
    else:
        result = "Such a triangle exists.\n"
        if angle_a == 90 or angle_b == 90 or (180 - angle_a - angle_b) == 90:
            result += "The triangle is a right triangle."
        else:
            result += "The triangle is not a right triangle."
        return result

angle_a = float(input("Enter the measure of the first angle of the triangle (in degrees): "))
angle_b = float(input("Enter the measure of the second angle of the triangle (in degrees): "))

validation_result = validate_triangle(angle_a, angle_b)
print(validation_result)
