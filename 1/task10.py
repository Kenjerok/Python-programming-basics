user = {
    "ID": 1,
    "Прізвище": "Опацький",
    "Ім’я": "Свят",
    "Група": "ІПЗс-21-2",
    "Курс": 3,
    "Книги (борг)": [],
    "Статистика книг": []
}

def display_user_info():
    print("\nКарта читача:")
    print(f"ID: {user['ID']}")
    print(f"Прізвище: {user['Прізвище']}")
    print(f"Ім’я: {user['Ім’я']}")
    print(f"Група: {user['Група']}")
    print(f"Курс: {user['Курс']}")
    print(f"Книги (борг): {', '.join(user['Книги (борг)']) if user['Книги (борг)'] else 'немає'}")
    print(f"Статистика книг: {', '.join(user['Статистика книг']) if user['Статистика книг'] else 'немає'}")
    print()

def take_book():
    book_name = input("Введіть назву книги, яку бажаєте взяти: ")
    user["Книги (борг)"].append(book_name)
    print(f"Книга '{book_name}' додана до боргу.\n")

def return_book():
    if not user["Книги (борг)"]:
        print("У вас немає книг у боргу.\n")
        return
    
    print("Книги у боргу:")
    for i, book in enumerate(user["Книги (борг)"], 1):
        print(f"{i}. {book}")
    
    book_name = input("Введіть назву книги, яку бажаєте повернути: ")
    if book_name in user["Книги (борг)"]:
        user["Книги (борг)"].remove(book_name)
        user["Статистика книг"].append(book_name)
        print(f"Книга '{book_name}' повернена.\n")
    else:
        print(f"Книга '{book_name}' відсутня у боргу.\n")

def main():
    while True:
        print("Меню:")
        print("1. Вивести карту читача")
        print("2. Взяти книгу")
        print("3. Повернути книгу")
        print("0. Вийти з програми")
        
        choice = input("Введіть ваш вибір: ")
        
        if choice == "1":
            display_user_info()
        elif choice == "2":
            take_book()
        elif choice == "3":
            return_book()
        elif choice == "0":
            print("Вихід з програми.")
            break
        else:
            print("Невірний вибір, спробуйте ще раз.\n")

if __name__ == "__main__":
    main()