class Works:
    def get_message(self):
        raise NotImplementedError("This method should be overridden by subclasses")

class ChroniclesOfNarnia(Works):
    def get_message(self):
        return "Хроніки Нарнії"

class AmphibianMan(Works):
    def get_message(self):
        return "Людина-амфібія"

class GulliversTravels(Works):
    def get_message(self):
        return "Подорож Гуллівера"

class IslandsInTheOcean(Works):
    def get_message(self):
        return "Острови в океані"

class CrimeAndPunishment(Works):
    def get_message(self):
        return "Злочин і кара"

class ManInABrownSuit(Works):
    def get_message(self):
        return "Людина в коричневому костюмі"

class MurderInTheRueMorgue(Works):
    def get_message(self):
        return "Вбивство на вулиці Морг"

class Fantasy:
    def __init__(self):
        self.books = [ChroniclesOfNarnia(), AmphibianMan()]

    def get_messages(self):
        return [book.get_message() for book in self.books]

class Detective:
    def __init__(self):
        self.books = [CrimeAndPunishment() ,ManInABrownSuit(), MurderInTheRueMorgue()]

    def get_messages(self):
        return [book.get_message() for book in self.books]

fantasy = Fantasy()
detective = Detective()

print("Фантастика:", fantasy.get_messages())
print("Детектив:", detective.get_messages())
