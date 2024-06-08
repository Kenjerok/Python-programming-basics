def count_integer_numbers(num1, num2, num3):
    integer_count = 0

    if num1 == int(num1):
        integer_count += 1
    if num2 == int(num2):
        integer_count += 1
    if num3 == int(num3):
        integer_count += 1

    return integer_count

num1 = float(input("Enter the number num1: "))
num2 = float(input("Enter the number num2: "))
num3 = float(input("Enter the number num3: "))

integer_count = count_integer_numbers(num1, num2, num3)
print("The number of integers among the entered ones:", integer_count)
