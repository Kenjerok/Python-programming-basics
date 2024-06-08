def calculate_power(number):
    if number >= 0:
        result = number ** 2
    else:
        result = number ** 4
    return result

num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

num1_result = calculate_power(num1)
num2_result = calculate_power(num2)
num3_result = calculate_power(num3)

print("Power calculation results:")
print("Number 1:", num1, "Result:", num1_result)
print("Number 2:", num2, "Result:", num2_result)
print("Number 3:", num3, "Result:", num3_result)
