class Zivali:
    def __init__(self, ime, kolicina):
        self.ime = ime
        self.kolicina = kolicina
    
    def dodaj_enga(self):
        self.kolicina += 1

ime = "neki"

class Macka(Zivali):
    def __init__(self, ime, kolicina, barva):
        super().__init__(ime, kolicina)
        self.barva = barva

def add(a, b):
    return a+b    

def zmnozi(a, b):
    return a*b

def deli(a,b):
    return a/b

def operacija(operacija1, a, b):
    return operacija1(a, b)


for f in (add, zmnozi, deli):
    print(operacija(f, 4, 5))


    
print(operacija(add, 1, 2))    
    

bober = Zivali("bober", 12)
obj1 = Macka(ime, 12, "crna")

obj1.dodaj_enga()
print(obj1.kolicina, obj1.ime)

macka = Zivali("Macka", 15)
Zivali.dodaj_enga(macka)
print(macka.kolicina)