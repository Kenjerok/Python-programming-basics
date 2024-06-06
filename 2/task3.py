a = 8
b = 6
result1 = (a < b) or (a % 2 != 0) or (b % 2 == 0) or (a + b > 10)
result2 = (a == b) or (a < b) or (a / 2 == 0)
result3 = (a > 10) or (b > 10) or (a * b > 50) or (b % a == 5)
result4 = (a > b) or (b % 3 == 0) or (a ** b < 5)
print(
    f"Результат першої перевірки {result1}"
    f"\nРезультат другої перевірки {result2}"
    f"\nРезультат третьої перевірки {result3}"
    f"\nРезультат четвертої перевірки {result4}"
    )