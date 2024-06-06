def print_even_numbers(n, m):
    
    for i in range(-n, n + 1, m):
        if i % 2 == 0:
            print(i)

n, m = 30, 6
print_even_numbers(n, m)