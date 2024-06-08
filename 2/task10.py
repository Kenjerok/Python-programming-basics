total = 0

for _ in range(9999):
    number = int(input("Введіть ціле число (введіть 0, щоб завершити): "))
    
    if number == 0:
        break
    
    total += number

print("Сума введених чисел:", total)
