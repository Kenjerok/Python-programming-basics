def count_negative_numbers(number1, number2, number3):
    negative_count = 0

    if number1 < 0:
        negative_count += 1
    if number2 < 0:
        negative_count += 1
    if number3 < 0:
        negative_count += 1

    return negative_count

number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the third number: "))

negative_count = count_negative_numbers(number1, number2, number3)
print("The number of negative numbers among the entered ones:", negative_count)
