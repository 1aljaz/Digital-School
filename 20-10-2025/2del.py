# Naredi program, ki ti bo generiral gesla. Funkcija gen_geslo(dolzina:int, velike_crke:boolean, stevilke:boolean, simboli:boolean) naj vrne geslo, ki 
# naj nujno vključuje male črke, če želi uporabnik uporabiti še velike črke, številke ali simbole naj nastavi boolean vrednosti na true.


import random
import string
def gen_geslo(dolzina, velike_crke=True, stevilke=False, simboli=False):
    baza = string.ascii_letters
    # Imamo še string.digits in string.punctuation
    geslo = ""
    moznosti = [male,velike,stevilke, simboli]
    for i in range(dolzina):
        if random.random
        
