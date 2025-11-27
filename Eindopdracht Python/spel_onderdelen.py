import random

# onderdelen van het blackjack spel

class Kaart:
    def __init__(self, naam, waarde, symbool):
        self.naam = naam
        self.waarde = waarde
        self.symbool = symbool

    def __str__(self):
        # kaart als tekst met emoji
        return f"{self.symbool} {self.naam}"


class Hand:
    def __init__(self):
        # kaarten van speler of deler
        self.kaarten = []

    def pak_kaart(self, kaart):
        # kaart toevoegen
        self.kaarten.append(kaart)

    def punten_speler(self):
        # telt punten van speler
        totaal = 0
        azen = 0
        for kaart in self.kaarten:
            if kaart.naam == "aas":
                totaal += 11
                azen += 1
            else:
                totaal += kaart.waarde
        while totaal > 21 and azen > 0:
            totaal -= 10
            azen -= 1
        return totaal

    def punten_deler(self):
        # punten voor deler met azen als 10
        totaal = 0
        for kaart in self.kaarten:
            if kaart.naam == "aas":
                totaal += 10
            else:
                totaal += kaart.waarde
        return totaal


class Speler:
    def __init__(self, naam):
        self.naam = naam
        self.hand = Hand()

    def reset_hand(self):
        # lege hand bij nieuw spel
        self.hand = Hand()

    def toon_hand(self):
        for kaart in self.hand.kaarten:
            print(kaart)


class Deler(Speler):
    def __init__(self):
        super().__init__("Deler")

    def toon_hand(self, verberg_eerste=False):
        for i, kaart in enumerate(self.hand.kaarten):
            if verberg_eerste and i == 0:
                print("verborgen kaart")
            else:
                print(kaart)
