# naam: Dani Buwalda
# datum: 17-10-2025
# naam opdracht: eindopdracht blackjack python

import random
import os
from spel_onderdelen import Kaart, Speler, Deler

# kleuren voor tekst
CLR = {
    "rood": "\033[91m",
    "groen": "\033[92m",
    "geel": "\033[93m",
    "blauw": "\033[94m",
    "magenta": "\033[95m",
    "cyan": "\033[96m",
    "reset": "\033[0m",
}

def kleur(txt, naam):
    return CLR.get(naam, "") + txt + CLR["reset"]

def kleur_kaart(kaart_str):
    if "♥" in kaart_str or "♦" in kaart_str:
        return kleur(kaart_str, "rood")
    return kleur(kaart_str, "cyan")

def wis_scherm():
    os.system("cls" if os.name == "nt" else "clear")

# deck met emoji
def maak_deck():
    symbolen = ["♠", "♥", "♦", "♣"]
    namen = ["aas", "heer", "dame", "boer"] + [str(n) for n in range(10, 1, -1)]
    deck = []
    for sym in symbolen:
        for naam in namen:
            if naam in ["boer", "dame", "heer", "10"]:
                waarde = 10
            elif naam == "aas":
                waarde = 11
            else:
                waarde = int(naam)
            kaart = Kaart(naam, waarde, sym)
            deck.append(kaart)
    return deck

def print_blok(titel, regels, punten=None, kleur_titel="cyan"):
    print(kleur("##############", kleur_titel))
    print(kleur(f"{titel}:", kleur_titel))
    print(kleur("##############", kleur_titel))
    for regel in regels:
        print(kleur_kaart(regel))
    print(kleur("--------------", kleur_titel))
    if punten is not None:
        print(kleur(f"punten: {punten}", "geel"))
        print(kleur("##############", kleur_titel))
        print()

def toon_deler(deler, verberg_eerste=True):
    regels = []
    for i, kaart in enumerate(deler.hand.kaarten):
        if verberg_eerste and i == 0:
            regels.append("verborgen kaart")
        else:
            regels.append(str(kaart))
    punten = None if verberg_eerste else deler.hand.punten_deler()
    print_blok("Delers hand", regels, punten, kleur_titel="magenta")

def toon_speler(speler):
    regels = [str(k) for k in speler.hand.kaarten]
    punten = speler.hand.punten_speler()
    print_blok("Spelers hand", regels, punten, kleur_titel="blauw")

def deel_start(deck, speler, deler):
    for _ in range(2):
        kaart = deck.pop()
        deler.hand.pak_kaart(kaart)
    for _ in range(2):
        kaart = deck.pop()
        speler.hand.pak_kaart(kaart)

def vraag_actie():
    print(kleur("1.) HIT", "groen"))
    print(kleur("2.) CALL", "rood"))
    keuze = input("> ").strip()
    if keuze in ["1", "2"]:
        return keuze
    print(kleur("foute keuze probeer opnieuw", "geel"))
    return vraag_actie()

def speler_beurt(deck, speler, deler):
    while True:
        wis_scherm()
        toon_deler(deler, verberg_eerste=True)
        toon_speler(speler)

        punten = speler.hand.punten_speler()
        if punten == 21:
            print(kleur("je hebt 21", "groen"))
            return "speler_wint"
        if punten > 21:
            print(kleur("je bent over de 21", "rood"))
            return "deler_wint"

        keuze = vraag_actie()
        if keuze == "1":
            if len(deck) > 0:
                kaart = deck.pop()
                speler.hand.pak_kaart(kaart)
            else:
                print(kleur("deck is leeg", "geel"))
                return "gelijk"
        else:
            return "call"

def deler_beurt(deck, speler, deler):
    while True:
        punten = deler.hand.punten_deler()
        if punten >= 17:
            break
        if len(deck) == 0:
            break
        kaart = deck.pop()
        deler.hand.pak_kaart(kaart)

    wis_scherm()
    toon_deler(deler, verberg_eerste=False)
    toon_speler(speler)

    s = speler.hand.punten_speler()
    d = deler.hand.punten_deler()

    if d > 21:
        print(kleur("deler is over de 21", "groen"))
        return "speler_wint"
    if s == d:
        print(kleur("gelijkspel", "geel"))
        return "gelijk"
    if s > d:
        print(kleur("je wint", "groen"))
        return "speler_wint"
    else:
        print(kleur("deler wint", "rood"))
        return "deler_wint"

def win_scherm():
    print()
    print(kleur("╔════════════════╗", "groen"))
    print(kleur("║     YOU WIN    ║", "groen"))
    print(kleur("╚════════════════╝", "groen"))
    print()

def lose_scherm():
    print()
    print(kleur("╔════════════════╗", "rood"))
    print(kleur("║    YOU LOSE    ║", "rood"))
    print(kleur("╚════════════════╝", "rood"))
    print()

def spelregels():
    wis_scherm()
    print(kleur("=== SPELREGELS ===", "blauw"))
    print()
    print(kleur("• Doel is om 21 punten te halen", "cyan"))
    print(kleur("• Boer dame heer en 10 tellen als 10", "cyan"))
    print(kleur("• Aas telt als 11 of 1", "cyan"))
    print(kleur("• Jij speelt eerst daarna de deler", "cyan"))
    print(kleur("• De deler stopt bij 17 of hoger", "cyan"))
    print(kleur("• Over 21 is verlies", "cyan"))
    print()
    input(kleur("druk op enter om terug te gaan", "geel"))

def speel_ronde():
    deck = maak_deck()
    random.shuffle(deck)

    speler = Speler("Speler")
    deler = Deler()

    speler.reset_hand()
    deler.reset_hand()

    deel_start(deck, speler, deler)

    uitkomst = speler_beurt(deck, speler, deler)
    if uitkomst == "call":
        uitkomst = deler_beurt(deck, speler, deler)

    if uitkomst == "speler_wint":
        win_scherm()
    elif uitkomst == "deler_wint":
        lose_scherm()

    input(kleur("druk op enter om door te gaan", "geel"))

def start_menu():
    while True:
        wis_scherm()
        print(kleur("=== BLACKJACK ===", "magenta"))
        print(kleur("1.) Start spel", "groen"))
        print(kleur("2.) Spelregels", "blauw"))
        print(kleur("3.) Stop", "rood"))
        keuze = input("> ").strip()

        if keuze == "1":
            speel_ronde()
        elif keuze == "2":
            spelregels()
        elif keuze == "3":
            wis_scherm()
            print(kleur("Tot de volgende keer", "cyan"))
            break
        else:
            print(kleur("Ongeldige keuze probeer opnieuw", "geel"))
            input()

if __name__ == "__main__":
    start_menu()
