class Produkt:
    def __init__(self, id, nazwa, kategoria, cena):
        if cena <= 0:
            raise ZlaCena(cena)
        self.id = id
        self.nazwa = nazwa
        self.kategoria = kategoria
        self.cena = cena

    def __lt__(self, other):
        return self.nazwa.lower() < other.nazwa.lower()

    def __eq__(self, other):
        return self.nazwa.lower() == other.nazwa.lower()

    def __str__(self):
        return f"{self.id} {self.nazwa} {self.kategoria} {self.cena:.2f}"


class ZlaCena(Exception):
    def __init__(self, cena):
        super().__init__(f"Cena: {cena} nie może być ujemna!")


class Magazyn:
    def __init__(self):
        self.produkty = []
        self.stan_magazynowy = {}

    def dodaj_produkt(self, produkt, ilosc):
        if produkt.id in self.stan_magazynowy:
            self.stan_magazynowy[produkt.id] += ilosc
        else:
            self.produkty.append(produkt)
            self.stan_magazynowy[produkt.id] = ilosc

    def wyswietl_produkty(self):
        for produkt in sorted(self.produkty):
            print(produkt)

    def aktualna_wartosc_magazynu(self):
        wartosc = 0
        for produkt in self.produkty:
            wartosc += produkt.cena * self.stan_magazynowy[produkt.id]
        return wartosc

    def zapisz_stan_magazynu(self, plik):
        with open(plik, 'w') as f:
            for produkt in sorted(self.produkty):
                f.write(f"{produkt} {self.stan_magazynowy[produkt.id]}\n")
        f.close()

    def wczytaj_produkty_z_pliku(self, plik):
        with open(plik, 'r') as f:
            for linia in f:
                dane = linia.strip().split()
                id = int(dane[0])
                nazwa = dane[1]
                kategoria = dane[2]
                cena = float(dane[3])
                ilosc = int(dane[4])
                produkt = Produkt(id, nazwa, kategoria, cena)
                self.dodaj_produkt(produkt, ilosc)
        f.close()


mag = Magazyn()

mag.dodaj_produkt(Produkt(1, "Chleb", "Pieczywo", 3.50), 10)
mag.dodaj_produkt(Produkt(2, "Mleko", "Nabial", 2.80), 20)
mag.dodaj_produkt(Produkt(3, "Jablko", "Owoce", 1.50), 30)

print("Lista produktów posortowana alfabetycznie:")
mag.wyswietl_produkty()

mag.zapisz_stan_magazynu("zapisz.txt")

mag.wczytaj_produkty_z_pliku("czytaj.txt")

print("\nLista produktów posortowana alfabetycznie po wczytaniu dodatkowych produktów:")
mag.wyswietl_produkty()

print("\nAktualna wartość magazynu:")
print(mag.aktualna_wartosc_magazynu())
# p1 = Produkt(5, 'sok', 'picie', -1)
