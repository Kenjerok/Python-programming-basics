def update_numbers(number1, number2):
    if number1 == number2:
        return "The numbers number1 and number2 must be different."
    else:
        if number1 < number2:
            number1 = (number1 + number2) / 2
            number2 = 2 * number1 * number2
        else:
            number2 = (number1 + number2) / 2
            number1 = 2 * number1 * number2

        return "After update: number1 = {}, number2 = {}".format(number1, number2)

number1 = float(input("Enter number1: "))
number2 = float(input("Enter number2: "))

result = update_numbers(number1, number2)
print(result)
