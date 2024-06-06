def count_integer_numbers(num1, num2, num3):
    integer_count = 0

    if num1.is_integer():
        integer_count += 1
    if num2.is_integer():
        integer_count += 1
    if num3.is_integer():
        integer_count += 1

    return integer_count

num1 = float(input("Введіть число num1: "))
num2 = float(input("Введіть число num2: "))
num3 = float(input("Введіть число num3: "))

integer_count = count_integer_numbers(num1, num2, num3)
print("Кількість цілих чисел серед введених:", integer_count)
