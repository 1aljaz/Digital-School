import time
import random

class Pet:
    def __init__(self, ime):
        self.ime = ime
        self.lakota = 5       # 0 = sit, 10 = zelo lačen
        self.sreca = 5    # 0 = nesrečen, 10 = zelo vesel
        self.energija = 5       # 0 = izčrpan, 10 = poln energije
        self.ziv = True

    def eat(self):
        """Naloga učenca: zmanjša lakoto in malenkost poveča energijo."""
        pass

    def play(self):
        """Naloga učenca: poveča srečo, poveča lakoto in zmanjša energijo."""
        pass

    def sleep(self):
        """Naloga učenca: močno obnovi energijo, vendar lakota rahlo naraste."""
        pass

    def trick(self):
        """Naloga učenca: trik poveča srečo, če je dovolj energije."""
        pass

    def tick(self):
        """
        Samodejno se kliče vsakič, ko se zažene zanka.
        Naloga učenca: lakota naj počasi raste, sreča naj rahlo pada,
        energija naj pada.
        """
        pass

    def status(self):
        print(f"\n--- Status ljubljenčka {self.name} ---")
        print(f"Lakota:    {self.hunger}/10")
        print(f"Sreča:     {self.happiness}/10")
        print(f"Energija:  {self.energy}/10")

    def check_alive(self):
        """Naloga učenca: če je lakota 10 ali energija 0, ljubljenček umre."""
        pass
