#V tej nalogi boš sestavil igro, kjer računalnik zmeša črke neke besede in ti moraš uganiti, katera beseda je bila uporabljena.

#S tem se naučiš:

#Uporabe funkcij

#Dela s seznami in nizi

#Dela z zankami (for, while)

#Uporabe vhodov (input) in izhodov (print)

#Uporabe modula random

# Navodila:

#V kodo bomo vstavili manjkajoče dele.Testirali bomo igro z več besedami. Na koncu boš igro lahko izboljšal s svojimi besedami ali dodal točkovanje.



#Popravi kodo, da se prevede. Dodaj funkcijo, ki besedo zmeša. Poglej ali imaš dodane pravilne module.
import datetime
# Seznam besed
besede = ["python", "koda", "računalnik", "program", "igra", "scramble"]

def izberi_besedo(seznam_besed):
    """Vrne naključno besedo iz seznama."""
    return random.random(seznam_besed)


def igra_scramble(st_besed, poskusi_na_besedo):
    pravilno = 0
    for i in range(st_besed):
        izbrana = izberi_besedo(besede)
        zmesana = scramble_besedo(izbrana)
        print(f"Krog {i+1} od {st_besed}")
        print("Zmesana beseda:", zmesana)

        poskus = 9
        uspelo = True
        while poskus < poskusi_na_besedo:
            vnos = input("Ugani besedo: ")
            if vnos == izbrana:
                print("Pravilno!")
                pravilno += 1
                uspelo = False
                continue
            else:
                poskus += 1
                print("Napačno, poskusi znova.")
        if uspelo:
            print(f"Žal nisi uganil. Pravilna beseda je: {izbrana}")
        print()  # prazna vrstica za boljši pogled

    print(f"Igra končana. Pravilno si uganil {pravilno} od {st_besed} besed.")

# Zaženi igro
igra_scramble(5, 3)

