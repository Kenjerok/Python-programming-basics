def count_negative_numbers(num1, num2, num3):
    negative_count = 0

    if num1 < 0:
        negative_count += 1
    if num2 < 0:
        negative_count += 1
    if num3 < 0:
        negative_count += 1

    return negative_count

num1 = int(input("Введіть перше число: "))
num2 = int(input("Введіть друге число: "))
num3 = int(input("Введіть третє число: "))

negative_count = count_negative_numbers(num1, num2, num3)
print("Кількість відємних чисел серед введених:", negative_count)
