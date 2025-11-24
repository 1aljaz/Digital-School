class Character:
    def __init__(self, ime, hp, attack_power):
        self.ime = ime
        self.hp = hp
        self.attack_power = attack_power
    
    def je_ziv(self):
        # Naj pove ali je character ziv
        pass

    def navaden_napad(self, target):
        dmg = self.attack_power
        target.hp -= dmg
        print(f"{self.ime} je napadel {target.ime} za {dmg} dmg.")
    
    def info(self):
        print(f"HP: {self.hp}, ATK: {self.attack_power}")

# Z uporbo dedovanja naredite podrazred razreda Character. 
# Npr. Mage, Warrior, Brawler, Dark Mage, ...
# Primer: Bard

class Bard(Character):
    def __init__(self, ime, hp=80, attack_power=30):
        super().__init__(ime, hp, attack_power)
        self.mana = 100
    
    def poteza(self):
        print("Na voljo imas:\n1) Navaden napad\n2) Curse")
    
    def super_atk(self, target):
        if self.mana >= 25:
            self.mana -= 25
            target.attack_power -= 25
        else:
            print("Imam samo {self.mana} mane. Nimam dovolj.")

# Dodaj se kaksno posat. Ogre, Wearwolf, ...



# Funkcija za battle
def battle(igralec, nasprotnik):
    print("----Začetek boja----")
    print(igralec.info())
    print(nasprotnik.info())
    print()

    while(igralec.je_ziv() and nasprotnik.je_ziv()):
        print(f"Tvoja poteza: \n{igralec.poteza()}")
        izbira = input(">")
        if izbira == 1:
            igralec.navaden_napad(nasprotnik)
        elif izbira == 2:
            igralec.super_atk(nasprotnik)
        else:
            print("Napacna!")
        
        # Dodaj da te lahko nasportnik napada, ce ima se dovolj hp-ja.
        # Izpisi HP obeh.
        # Dodaj 20% moznost, da te nasportnik napade iz njegovim special napadom.
        # DOdaj, kdo je zmagal.

if __name__ == "__main__":
    bard = Bard("Tim")
    nasprotnik = Bard("Tomaz")
    battle(bard, nasprotnik)




