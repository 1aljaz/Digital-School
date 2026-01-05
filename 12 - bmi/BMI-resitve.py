from abc import abstractmethod
import datetime
from tkinter import *
from tkinter import ttk


class Oseba:
    def __init__(self, ime, teza, velikost, leto_rojstva):
        self.__ime = ime
        self.__teza = teza
        self.__velikost = velikost
        self.__jeOtrok = False if datetime.datetime.now().year - leto_rojstva >= 17 else True

    @property
    def teza(self):
        return self.__teza

    @teza.setter
    def teza(self, teza):
        if not (isinstance(teza, int) or isinstance(teza, float)):
            print("Teza mora biti stevilka")
            return -1
        if teza >= 0:
            self.__teza = teza

    @property
    def velikost(self):
        return self.__velikost
    
    @property
    def BMI(self):
        return self.__BMI

    @BMI.setter
    def BMI(self, bmi):
        pass

    @velikost.setter
    def velikost(self, velikost):
        if not isinstance(velikost, int):
            print("Velikost mora biti celo število v cm.")
            return -1
        if velikost > 0:
            self.__velikost = velikost

    def izracunajBMI(self):
        """Izracuna BMI osebe."""
        self.__BMI = self.__teza/(self.__velikost/100 )**2 * (1.3 if self.__jeOtrok else 1)

    def izpisiKategorijoBMI(self):
        """Izpise BMI kategorijo osebe."""
        if self.__jeOtrok:
            if self.__BMI < 14:
                print("Underweight")
                return "Underweight"
            elif self.__BMI < 18:
                print("Normal weight")
                return "Normal weight"
            elif self.__BMI < 24:
                print("Overweight")
                return "Overweight"
            print("Obese")
            return "Obese"
        else:
            if self.__BMI < 18.5:
                print("Underweight")
                return "Underweight"
            elif self.__BMI < 25:
                print("Normal weight")
                return "Normal weight"
            elif self.__BMI < 30:
                print("Overweight")
                return "Overweight"
            print("Obese")
            return "Obese"
        

