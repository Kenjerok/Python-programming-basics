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

class Fantasy(ChroniclesOfNarnia, AmphibianMan):
    def get_messages(self):
        return [ChroniclesOfNarnia.get_message(self), AmphibianMan.get_message(self)]

class Adventures(GulliversTravels, IslandsInTheOcean):
    def get_messages(self):
        return [GulliversTravels.get_message(self), IslandsInTheOcean.get_message(self)]

class Detective(CrimeAndPunishment, ManInABrownSuit, MurderInTheRueMorgue):
    def get_messages(self):
        return [CrimeAndPunishment.get_message(self), ManInABrownSuit.get_message(self), MurderInTheRueMorgue.get_message(self)]

fantasy = Fantasy()
adventures = Adventures()
detective = Detective()

print("Фантастика:", fantasy.get_messages())
print("Детектив:", detective.get_messages())
