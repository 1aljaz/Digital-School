# Naredimo class Lik. Potrebna abstraktna metoda povrsina in obseg.
# Dodaj subclassa Krog in Pravokotnik in dodaj metodo in obseg 
# v ta subclassa. Dodaj tudi getterje in setterje za stranice/radij.
class Lik:
    def __init__(self, stranica):
        self.__stranica = stranica
    
    @property
    def stranica(self):
        return self.__stranica
    
    @stranica.setter
    def stranica(self, stranica):
        self.__stranica = stranica