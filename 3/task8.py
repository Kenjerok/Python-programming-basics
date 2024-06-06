def count_positive_numbers(num1, num2, num3):

    positive_count = 0

    if num1 > 0:
        positive_count += 1
    if num2 > 0:
        positive_count += 1
    if num3 > 0:
        positive_count += 1

    return positive_count

num1 = int(input("Введіть перше число: "))
num2 = int(input("Введіть друго число: "))
num3 = int(input("Введіть третє число: "))

positive_count = count_positive_numbers(num1, num2, num3)
print("Кількість додатних чисел серед введених:", positive_count)
