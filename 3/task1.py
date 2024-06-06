def calculate_power(number):
    if number >= 0:
        result = number ** 2
    else:
        result = number ** 4
    return result

num1 = float(input("Введіть перше число: "))
num2 = float(input("Введіть друге число: "))
num3 = float(input("Введіть третє число: "))

num1_result = calculate_power(num1)
num2_result = calculate_power(num2)
num3_result = calculate_power(num3)

print("Результати піднесення до степеня:")
print("Число 1:", num1, "Результат:", num1_result)
print("Число 2:", num2, "Результат:", num2_result)
print("Число 3:", num3, "Результат:", num3_result)
