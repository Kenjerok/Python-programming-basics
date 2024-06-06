place = int(input("Введіть номер місця в плацкартному вагоні: "))

if 1 <= place <= 36:
    if place % 2 == 0:
        place_type = "верхнє в купе"
    else:
        place_type = "нижнє в купе"
elif 37 <= place <= 54:
    if place % 2 == 0:
        place_type = "верхнє бічне"
    else:
        place_type = "нижнє бічне"
else:
    place_type = "неіснуюче місце"

print(f"Місце {place} - це {place_type}.")
