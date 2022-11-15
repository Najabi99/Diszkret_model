from passenger import Utas


class Allomas:
    def __init__(self, nev, kapcsolatok, varakozok):
        self.nev = nev
        self.kapcsolatok = kapcsolatok
        self.varakozok = varakozok

    def get_kapcsolatok(self):
        return self.kapcsolatok

    def get_nev(self):
        return self.nev

    def get_varakozok(self):
        return self.varakozok
