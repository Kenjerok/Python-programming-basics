def update_numbers(num1, num2):
    if num1 == num2:
        return "Числа num1 і num2 повинні бути різними."
    else:
        if num1 < num2:
            num1 = (num1 + num2) / 2
            num2 = 2 * num1 * num2
        else:
            num2 = (num1 + num2) / 2
            num1 = 2 * num1 * num2

        return "Після заміни: num1 = {}, num2 = {}".format(num1, num2)

num1 = float(input("Введіть число num1: "))
num2 = float(input("Введіть число num2: "))

result = update_numbers(num1, num2)
print(result)
