import sqlite3

def ustvari_tabelo():
    """
    Tukaj se poveži na 'knjiznica.db', ustvari kurzor in 
    izvedi ukaz: CREATE TABLE IF NOT EXISTS knjige (...)
    Ne pozabi na commit() in close()!
    """
    pass

def dodaj_podatke():
    """
    Vprašaj uporabnika za ime knjige in avtorja.
    Poveži se z bazo in uporabi INSERT INTO z vprašaji (?).
    """
    pass

def izpisi_vse():
    """
    Izvedi SELECT * FROM knjige in uporabi .fetchall(), 
    da dobiš podatke. Nato jih s for zanko izpiši.
    """
    pass


ustvari_tabelo()
# dodaj_podatke()
# izpisi_vse()