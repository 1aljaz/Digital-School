class Sistem:
    def __init__(self, tip, varnost):
        self.tip = tip
        self.varnost = varnost
    
    def install_system(self):
        # Povecaj varnost za 5
        pass


class Antivirus(Sistem):
    # Dodaj konstruktor, ki doda nov tip za Firewall. Naj bo tipa boolean in naj bo na zacetku nastavljen na True.
    def __init__(firewall=True):
        super().__init__("Antivirus",  5)
    
    def klikni_na_sumljivo_povezavo(self):
        # Zniza varnost za 3
        pass

    def preveri_varnost(self):
        # Ce je varnost 0, napisi to uporabniku
        pass

    def visaj_nevarnost(self):
        # Naj avtomatsko poveca nevarnost
        pass

    
