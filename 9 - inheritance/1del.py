# Potrebno je narediti, class BankAccount. Lastnosti: stanje, ime, priimek.
# Potrebno je dodati getterje in setterje ter vse propertyje.
# Metode: polozi_denar, dvigni_denar, pošlji denar. V dvigni denar dodaj pogoj, da lahko
# dvignemo denar samo, če ga imamo dovolj. Denar pošljemo drugemu računu.

class BankAccount:
    def __init__(self, stanje, ime, priimek):
        self.__stanje = stanje
        self.__ime = ime
        self.__priimek = priimek
        
    @property
    def stanje(self):
        return self.__stanje
    
    @stanje.setter
    def stanje(self, stanje):
        self.__stanje = stanje
    

    def polozi_denar(self, denar):
        self.__stanje += denar
    
    def dvigni_denar(self, denar):
        if self.__stanje >= denar:
            self.__stanje -= denar
            return True
        else:
            print("Premalo denarja.")
            return False
    
    def nakazi_denar(self, other, denar):
        if self.dvigni_denar(denar):
            other.polozi_denar(denar)
        else:
            print("premalo denarja.")


prvi = BankAccount(200, "aljaz", "marn")
drugi = BankAccount(300, "nejka", "m")

print(prvi.stanje)   
prvi.nakazi_denar(drugi, 100)
prvi.stanje
print(prvi.stanje, drugi.stanje)
