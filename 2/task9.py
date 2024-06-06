fib_sequence = [0, 1]
for i in range(2, 20):
    fib_sequence.append(fib_sequence[i-1] + fib_sequence[i-2])

print("Ряд чисел Фібоначчі від 1 до 20:", fib_sequence)

new_sequence = fib_sequence[4:21]
print("Ряд чисел від 5 до 20:", new_sequence)

even_numbers = []
for num in range(0, 21, 2):
    even_numbers.append(num)

print("Ряд парних чисел від 0 до 20:", even_numbers)

third_numbers = []
for num in range(-1, -21, -3):
    third_numbers.append(num)

print("Кожне третє число в ряді від -1 до -21:", third_numbers)