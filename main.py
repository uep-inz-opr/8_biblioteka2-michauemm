class Biblioteka:
    def __init__(self):
        self.limit_wypozyczen = int()
        self.lista_egzemplarzy = []
        self.lista_ksiazek = []
        self.lista_czytelnikow = []


    def dostepne_egz(self, tytul):
        for element in self.lista_egzemplarzy:
            if tytul == element.tytul and element.wypozyczony == False:
                lista = []
                lista.append(element)
        return lista

    def wypozycz(self, czytelnik, tytul):
        if czytelnik.ilosc_wypozyczen >= 3:
            # print("Nie mozna wypozyczyc wiecej niz 3")
            return False
        for ksiazka in czytelnik.lista_wypozyczonych:
            if tytul in str(ksiazka):
                # print("Nie można wypożyczyć tej samej książki dwa razy")
                return False
        dostep = self.dostepne_egz(tytul)
        czytelnik.lista_wypozyczonych.append(dostep.pop())
        czytelnik.lista_wypozyczonych[-1].wypozyczony = True
        czytelnik.ilosc_wypozyczen += 1
        return True


    def oddaj(self, czytelnik, tytul):
        for element in czytelnik.lista_wypozyczonych:
            if tytul == element.tytul:
                element.wypozyczony = False
                czytelnik.ilosc_wypozyczen -= 1
                return True
            else:
                return False

    def dodaj_egzemplarz_ksiazki(self, tytul, autor, rok_wydania):
        ksiazka = Ksiazka(tytul, autor)
        egzemplarz = Egzemplarz(tytul, rok_wydania)
        if ksiazka.tytul not in self.lista_ksiazek:
            self.lista_ksiazek.append(ksiazka.tytul)
        self.lista_egzemplarzy.append(egzemplarz)
        return True


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


    def dodaj_do_listy_czytelnikow(self, biblioteka):
        biblioteka.lista_czytelnikow.append(self)

    def __repr__(self):
        return f"{self.nazwisko}"

MojaBiblioteka = Biblioteka()
wynik = []
n = int(input())
for i in range(n):
    x = eval(input().strip())
    if "dodaj" in str(x[0]):
        tytul = x[1]
        autor = x[2]
        rok_wydania = x[3]
        MojaBiblioteka.dodaj_egzemplarz_ksiazki(tytul, autor, rok_wydania)
        wynik.append(MojaBiblioteka.dodaj_egzemplarz_ksiazki(tytul, autor, rok_wydania))
    elif "wypozycz" in str(x[0]):
        czytelnik = Czytelnik(x[1])
        czytelnik.dodaj_do_listy_czytelnikow(MojaBiblioteka)
        tytul = x[2]
        MojaBiblioteka.wypozycz(czytelnik, tytul)
        wynik.append(MojaBiblioteka.wypozycz(czytelnik, tytul))
    elif "oddaj" in str(x[0]):
        czytelnik = Czytelnik(x[1])
        czytelnik.dodaj_do_listy_czytelnikow(MojaBiblioteka)
        tytul = x[2]
        MojaBiblioteka.oddaj(czytelnik, tytul)
        wynik.append(MojaBiblioteka.oddaj(czytelnik, tytul))

for el in wynik:
    print(el)
