def check_sequence(sequence):
    c0 = c1 = 0
    for i in sequence:
        if i == '0':
            if c1 != 0:
                if c0 != c1:
                    return False
                c0 = c1 = 0
            c0 += 1
        elif i == '1':
            c1 += 1
        else:
            return False
    return c0 == c1

print(check_sequence("01010101"))
print(check_sequence("00011100011"))