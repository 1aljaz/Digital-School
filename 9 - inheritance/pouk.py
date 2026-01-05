class Zivali:
    # pasma, starost
    def __init__(self, pasma, starost):
        self.__pasma = pasma
        self.__starost = starost
    
    # getter
    def pasma(self):
        return self.__pasma

    # setter
    def pasma1(self, pasma):
        if 'a' not in pasma:
            self.__pasma = pasma
    




krava = Zivali("Krava", 15)
print(krava.pasma())
krava.pasma1("kuza")
print(krava.pasma())
krava.pasma1("zelva")
print(krava.pasma())