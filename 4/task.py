import random


class ChroniclesOfNarnia:
    @staticmethod
    def message():
        return 'Хроніки Нарнії'


class AmphibianMan:
    @staticmethod
    def message():
        return 'Людина-амфібія'


class GulliversTravels:
    @staticmethod
    def message():
        return 'Подорож Гуллівера'


class IslandsInTheOcean:
    @staticmethod
    def message():
        return 'Острови в океані'


class CrimeAndPunishment:
    @staticmethod
    def message():
        return 'Злочині кара'


class ManInBrownSuit:
    @staticmethod
    def message():
        return 'Людина в коричневому костюмі'


class MurderOnMorgueStreet:
    @staticmethod
    def message():
        return 'Вбивство на вулиці Морг'


def main():
    fantasy_classes = [ChroniclesOfNarnia, AmphibianMan]
    adventure_classes = [GulliversTravels, IslandsInTheOcean]
    all_classes = fantasy_classes + adventure_classes

    for index in range(1, 197):
        selected_class = random.choice(all_classes)
        print(f'{index}. Обробник повідомлення: {selected_class.message()}')


if __name__ == '__main__':
    main()
