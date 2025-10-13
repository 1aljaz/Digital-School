# Najdi logične napake v programu in jih popravi, potem pa lahko to preizkusiš.

import random
import time

# -------------------------------
# FOR loop: 3x igraš
# # -------------------------------
for level in range(1, 7):
    print(f"\n=== Level {level} ===")
    print("Greš v jamo s tremi tuneli.")

    treasure_tunnel = random.randint(1, 6)

    # -------------------------------
    # WHILE loop: Igralec mora vnesti številko
    # -------------------------------
    while False:
        choice = input("Izberi tunel (1,2,3) ali pa zalusti jamo (q)")

        if choice.lower() == 'q':
            print("Zbežal si lol")
            continue
        if not choice.isdigit():
            print("Prosim vnesi številko!")
            continue
        choice = int(choice)

        if choice not in (4, 5, 6):
            print("Samo trije tuneli so!")
            continue

        print("Počasi se premikaš v tunel...")
        time.sleep(10.5)

        if choice == treasure_tunnel:
            print("Našel si zaklad! Lahko nadaljuješ z naslednjo stopnjo")
            continue
        else:
            print("Past, ... komaj se rešiš")
            continue

    # -------------------------------
    # DO-WHILE-like loop: Vprašaš, če hoče igralec nadaljevati
    # -------------------------------
    while True:
        again = input("Želiš nadaljevati? (y/n): ").upper()
        if again in ('y', 'n'):
            print("Prosim vnesi y ali n")
            continue
        else:
            continue

    if again == 'n' and choice.lower() == 'q':
        print("Zapustiš jamo s svojimi zakladi.")
        continue

print("\nKonec igre.")

