def check_divisibility(num1, num2, num3, divisor):
    if num1 % divisor == 0 and num2 % divisor == 0 and num3 % divisor == 0:
        return True
    else:
        return False

num1 = int(input("Введіть перше число (num1): "))
num2 = int(input("Введіть друге число (num2): "))
num3 = int(input("Введіть третє число (num3): "))
divisor = int(input("Введіть число-дільник (divisor): "))

if check_divisibility(num1, num2, num3, divisor):
    print(f"Число {divisor} є дільником для {num1}, {num2} та {num3}.")
else:
    print(f"Число {divisor} не є дільником для {num1}, {num2} та {num3}.")
