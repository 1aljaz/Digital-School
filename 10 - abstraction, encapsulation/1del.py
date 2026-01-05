class Sistem:
    def __init__(self, tip, varnost):
        self.tip = tip
        self.varnost = varnost
    
    def install_system(self):
        # Povecaj varnost za 5
        self.varnost += 5


class Antivirus(Sistem):
    # Dodaj konstruktor, ki doda nov tip za Firewall. Naj bo tipa boolean in naj bo na zacetku nastavljen na True.
    def __init__(self, firewall=True):
        super().__init__("Antivirus",  5)
        self.firewall = firewall

    
    def klikni_na_sumljivo_povezavo(self):
        self.varnost -= 3

    def preveri_varnost(self):
        # Ce je varnost 0, napisi to uporabniku
        if self.varnost <= 0:
            print("Varnosti ni vec.")

    def visaj_nevarnost(self):
        # Naj avtomatsko poveca nevarnost
        self.varnost -= 0.5

antivirus = Antivirus(True)

antivirus.klikni_na_sumljivo_povezavo()
print(antivirus.tip, antivirus.varnost)
antivirus.preveri_varnost()
antivirus.install_system()
print(antivirus.tip, antivirus.varnost)


    
