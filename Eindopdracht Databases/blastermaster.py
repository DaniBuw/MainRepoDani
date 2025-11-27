# naam dani buwalda
# datum 28-10-2025 (Sorry dat ik het te laat heb ingeleverd! Ik had een reminder moeten maken maar dat was ik vergeten te doen...)
# eindopdracht databases

import mysql.connector

# verbinding maken met database
db = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="DLaoneisie1102008",
    database="blastermaster"
)

cursor = db.cursor()

# menu laten zien
def menu():
    print("\n1 nieuwe speler toevoegen")
    print("2 nieuw spel toevoegen")
    print("3 highscore invoeren")
    print("4 alle spellen tonen")
    print("5 alle spelers tonen")
    print("6 spellen met highscores")
    print("7 spelers met highscores")
    print("8 inkomsten per spel")
    print("9 stoppen")

# check of game id bestaat
def bestaat_game(game_id):
    cursor.execute("select 1 from game where game_id=%s", (game_id,))
    return cursor.fetchone() is not None

# check of speler id bestaat
def bestaat_speler(player_id):
    cursor.execute("select 1 from player where player_id=%s", (player_id,))
    return cursor.fetchone() is not None

# nieuwe speler toevoegen
def nieuwe_speler():
    naam = input("naam: ").strip()
    email = naam.lower() + "@blastmaster.nova"
    cursor.execute("insert into player (player_naam, player_email) values (%s,%s)", (naam, email))
    db.commit()
    print("speler toegevoegd")

# nieuw spel toevoegen
def nieuw_spel():
    naam = input("spelnaam: ").strip()
    genre = input("genre: ").strip()
    prijs = float(input("prijs: "))
    cursor.execute("insert into game (spelnaam, genre, prijs) values (%s,%s,%s)", (naam, genre, prijs))
    db.commit()
    print("spel toegevoegd")

# nieuwe highscore toevoegen
def nieuwe_highscore():
    game_id = int(input("game id: "))
    player_id = int(input("player id: "))

    # kijken of id klopt
    if not bestaat_game(game_id):
        print("game id bestaat niet")
        return
    if not bestaat_speler(player_id):
        print("player id bestaat niet")
        return

    pogingen = int(input("pogingen: "))
    score = int(input("highscore: "))
    datum = input("datum (yyyy-mm-dd): ").strip()

    cursor.execute("insert into highscore (game_id, player_id, pogingen, high_score, highscore_datum) values (%s,%s,%s,%s,%s)",
                   (game_id, player_id, pogingen, score, datum))
    db.commit()
    print("highscore toegevoegd")

# alle spellen laten zien
def alle_spellen():
    cursor.execute("select * from game")
    for x in cursor.fetchall():
        print(x)

# alle spelers laten zien
def alle_spelers():
    cursor.execute("select * from player")
    for x in cursor.fetchall():
        print(x)

# overzicht van spellen met highscores
def overzicht_spellen_highscores():
    cursor.execute("""
        select game.spelnaam, player.player_naam, highscore.high_score, highscore.highscore_datum
        from highscore
        join game on highscore.game_id = game.game_id
        join player on highscore.player_id = player.player_id
    """)
    for x in cursor.fetchall():
        print(x)

# overzicht van spelers met highscores
def overzicht_spelers_highscores():
    cursor.execute("""
        select player.player_naam, game.spelnaam, highscore.high_score
        from highscore
        join game on highscore.game_id = game.game_id
        join player on highscore.player_id = player.player_id
        order by highscore.high_score desc
    """)
    for x in cursor.fetchall():
        print(x)

# inkomsten per spel berekenen
def inkomsten():
    cursor.execute("""
        select game.spelnaam, sum(game.prijs * highscore.pogingen)
        from highscore
        join game on highscore.game_id = game.game_id
        group by game.game_id, game.spelnaam
    """)
    for x in cursor.fetchall():
        print(x)

print("welkom bij blastmaster highscore systeem")

# hoofdprogramma
while True:
    menu()
    keuze = input("keuze: ").strip()

    if keuze == "1":
        nieuwe_speler()
    elif keuze == "2":
        nieuw_spel()
    elif keuze == "3":
        nieuwe_highscore()
    elif keuze == "4":
        alle_spellen()
    elif keuze == "5":
        alle_spelers()
    elif keuze == "6":
        overzicht_spellen_highscores()
    elif keuze == "7":
        overzicht_spelers_highscores()
    elif keuze == "8":
        inkomsten()
    elif keuze == "9":
        print("programma gestopt")
        cursor.close()
        db.close()
        break
    else:
        print("verkeerde keuze probeer opnieuw")
