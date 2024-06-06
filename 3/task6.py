def update_values(value1, value2):
    if value1 != value2:
        max_value = max(value1, value2)
        value1 = max_value
        value2 = max_value
    else:
        value1 = 0
        value2 = 0

    return value1, value2

value1 = int(input("Введіть значення для першої змінної: "))
value2 = int(input("Введіть значення для другої змінної: "))

value1, value2 = update_values(value1, value2)
print("Після заміни: value1 =", value1, ", value2 =", value2)
