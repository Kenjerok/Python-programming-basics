def count_positive_numbers(number1, number2, number3):
    
    positive_count = 0

    if number1 > 0:
        positive_count += 1
    if number2 > 0:
        positive_count += 1
    if number3 > 0:
        positive_count += 1

    return positive_count

number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the third number: "))

positive_count = count_positive_numbers(number1, number2, number3)
print("The number of positive numbers among the entered ones:", positive_count)
