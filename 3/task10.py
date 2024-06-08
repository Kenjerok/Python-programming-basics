def check_divisibility(num1, num2, num3, divisor):
    if num1 % divisor == 0 and num2 % divisor == 0 and num3 % divisor == 0:
        return True
    else:
        return False

num1 = int(input("Enter the first number (num1): "))
num2 = int(input("Enter the second number (num2): "))
num3 = int(input("Enter the third number (num3): "))
divisor = int(input("Enter the divisor (divisor): "))

if check_divisibility(num1, num2, num3, divisor):
    print(f"The number {divisor} is a divisor for {num1}, {num2}, and {num3}.")
else:
    print(f"The number {divisor} is not a divisor for {num1}, {num2}, and {num3}.")
