import sqlite3

verbindung = sqlite3.connect('meinedb.db')
meincursor = verbindung.cursor()


def newdataset(name, kontostand):
    meincursor.execute("""INSERT INTO konto(name,kontostand) VALUES (?,?)""", (newKontoName, newAmount))
    verbindung.commit()
    print("Neuer Datensatz: {fname}, I'm {newAmount}".format(fname=newKontoName, newAmount=newAmount))


def showalldataset():
    meincursor.execute("SELECT * FROM konto")
    ergebnis = meincursor.fetchall()
    for zeile in ergebnis:
        print(zeile)


def deletedataset(name):
    meincursor.execute("DELETE FROM konto WHERE name = ?", (name,))
    verbindung.commit()
    print(f"Datensatz {name} wurde gelöscht.")


while True:
    print("Menü:")
    print("1. Neuer Datensatz")
    print("2. Alle Datensätze")
    print("3. Einen Datensatz löschen")
    print("4. Programm beenden")

    choice = input("Bitte wählen Sie eine Option (1-4): ")

    if choice == "1":
        print("Neuer Datensatz wird erstellt...")
        newKontoName = input("Neuer Name: ")
        newAmount = input("Neuer Betrag: ")
        newdataset(newKontoName,newAmount)
        break
    elif choice == "2":
        print("Alle Datensätze anzeigen...")
        showalldataset()
        break
    elif choice == "3":
        print("Einen Datensatz löschen...")
        datensatz = input("Welchen Datensatz möchtest du löschen?")
        deletedataset(datensatz)
        break
    elif choice == "4":
        print("Programm wird beendet.")
        break
    else:
        print("Ungültige Eingabe. Bitte eine Zahl zwischen 1 und 4 eingeben.")



