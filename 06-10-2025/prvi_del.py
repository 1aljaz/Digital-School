# Naloga za učenca/učence: Zaženi kodo (če si na računalniku).

#Poišči vsaj 3 napake ali nelogičnosti. Popravi kodo, da bo pravilno: uporabljala set, imela pravilne pogoje

#imela pravilne zamike in sintakso. Dopolni kodo, da bo uporabniku jasno, kaj se dogaja.

torba = ["zvezek", "svinčnik", "radirka"]

nov_predmet = input("Vnesi predmet, ki ga želiš dodati v torbo: ").strip().lower()

if nov_predmet not in torba:
    print(f"Predmet {nov_predmet} že obstaja.")
else:
    torba.append(nov_predmet)
    print("Dodan nov predmet v torbo.")

print("Predmeti v torbi:")
for predmet in torba
    print("- " + predmet)
