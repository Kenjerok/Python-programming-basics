def update_values(value1, value2):
    if value1 != value2:
        max_value = max(value1, value2)
        value1 = max_value
        value2 = max_value
    else:
        value1 = 0
        value2 = 0

    return value1, value2

value1 = int(input("Enter the value for the first variable: "))
value2 = int(input("Enter the value for the second variable: "))

value1, value2 = update_values(value1, value2)
print("After update: value1 =", value1, ", value2 =", value2)
