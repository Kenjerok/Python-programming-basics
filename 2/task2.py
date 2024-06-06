a = 7
b = 12
result1 = (a < b) and (a % 2 != 0) and (b % 2 == 0) and (a + b > 10)
result2 = (a > 0) and (b > 0) and (a * b > 50) and (b % a == 5)
result3 = (a == b) and (a < b) and (a / 2 == 0)
result4 = (a > b) and (b % 3 == 0) and (a ** b < 5)
print(
    f"Результат першої перевірки {result1}"
    f"\nРезультат другої перевірки {result2}"
    f"\nРезультат третьої перевірки {result3}"
    f"\nРезультат четвертої перевірки {result4}"
    )
