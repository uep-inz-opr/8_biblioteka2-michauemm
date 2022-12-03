class Biblioteka:
    def __init__(self):
        self.limit_wypozyczen = int()
        self.lista_egzemplarzy = []
        self.lista_ksiazek = []
        self.lista_czytelnikow = []
        self.wynik = []

    def dostepne_egz(self, tytul):
        lista = []
        for element in self.lista_egzemplarzy:
            if tytul == element.tytul and element.wypozyczony == False:
                lista.append(element)
        if len(lista) >= 1:
            return lista
        else:
            return False

    def wypozycz(self, czytelnik, tytul):
        if self.lista_czytelnikow:
            for element in self.lista_czytelnikow:
                if czytelnik in str(element):
                    if element.ilosc_wypozyczen >= 3:
                        self.wynik.append("False")
                        return
                    for ksiazka in element.lista_wypozyczonych:
                        if tytul in str(ksiazka):
                            self.wynik.append("False")
                            return
                    dostep = self.dostepne_egz(tytul)
                    if dostep == False:
                        self.wynik.append("False")
                        return
                    element.lista_wypozyczonych.append(dostep.pop())
                    element.lista_wypozyczonych[-1].wypozyczony = True
                    element.ilosc_wypozyczen += 1
                    self.wynik.append("True")
        else:
            czytelnik = Czytelnik(czytelnik)
            self.lista_czytelnikow.append(czytelnik)
            if czytelnik.ilosc_wypozyczen >= 3:
                self.wynik.append("False")
                return
            for ksiazka in czytelnik.lista_wypozyczonych:
                if tytul in str(ksiazka):
                    self.wynik.append("False")
                    return
            dostep = self.dostepne_egz(tytul)
            if dostep == False:
                self.wynik.append("False")
                return
            czytelnik.lista_wypozyczonych.append(dostep.pop())
            czytelnik.lista_wypozyczonych[-1].wypozyczony = True
            czytelnik.ilosc_wypozyczen += 1
            self.wynik.append("True")
        

    def oddaj(self, czytelnik, tytul):
        if self.lista_czytelnikow:
            for element in self.lista_czytelnikow:
                if czytelnik in str(element):
                    for el in element.lista_wypozyczonych:
                        if tytul in el.tytul:
                            el.wypozyczony = False
                            element.ilosc_wypozyczen -= 1
                            self.wynik.append("True")
                        else:
                            self.wynik.append("False")
        else:
            self.wynik.append("False")

    def dodaj_egzemplarz_ksiazki(self, tytul, autor, rok_wydania):
        ksiazka = Ksiazka(tytul, autor)
        egzemplarz = Egzemplarz(tytul, rok_wydania)
        if ksiazka.tytul not in self.lista_ksiazek:
            self.lista_ksiazek.append(ksiazka.tytul)
        self.lista_egzemplarzy.append(egzemplarz)
        self.wynik.append("True")
        return

class Egzemplarz:

    def __init__(self, tytul, rok_wydania, wypozyczony = False):
        self.tytul = tytul
        self.rok_wydania = int(rok_wydania)
        self.wypozyczony = wypozyczony

    def __repr__(self):
        if self.wypozyczony == False:
            return f"{self.tytul} {self.rok_wydania}, dostępne"
        else:
            return f"{self.tytul} {self.rok_wydania,}, wypożyczone"

class Ksiazka:
    def __init__(self, tytul, autor):
        self.tytul = tytul
        self.autor = autor

    def __repr__(self):
        return f"{self.tytul, self.autor}"

class Czytelnik:

    def __init__(self, nazwisko, ilosc_wypozyczen = 0):
        self.nazwisko = nazwisko
        self.ilosc_wypozyczen = ilosc_wypozyczen
        self.lista_wypozyczonych = []

    def __repr__(self):
        return f"{self.nazwisko}"

def main():
    MojaBiblioteka = Biblioteka()
    n = int(input())
    for i in range(n):
        x = eval(input().strip())
        if "dodaj" in str(x[0]):
            tytul = x[1]
            autor = x[2]
            rok_wydania = x[3]
            MojaBiblioteka.dodaj_egzemplarz_ksiazki(tytul, autor, rok_wydania)

        elif "wypozycz" in str(x[0]):
            czytelnik = x[1]
            tytul = x[2]
            MojaBiblioteka.wypozycz(czytelnik, tytul)

        elif "oddaj" in str(x[0]):
            czytelnik = x[1]
            tytul = x[2]
            MojaBiblioteka.oddaj(czytelnik, tytul)


    for el in MojaBiblioteka.wynik:
        print(el)
main()


