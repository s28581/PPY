class Osoba:
    def __init__(self, imię, nazwisko):
        self.imię = imię
        self.nazwisko = nazwisko

    def __lt__(self, other):
        return self.nazwisko < other.nazwisko

    def __eq__(self, other):
        return self.nazwisko == other.nazwisko and self.imię == other.imię


class Wypożyczający(Osoba):
    def __init__(self, imię, nazwisko, email, id):
        super().__init__(imię, nazwisko)
        self.id = id
        if "@" not in email:
            raise ValueError("Nieprawidłowy adres e-mail: brak znaku '@'")
        self.email = email

class ZłyEmail(Exception):
    def __init__(self, email):
        super().__init__(f"Nieprawidłowy e-mail: '{email}' - brak znaku '@'.")

class Książka:
    def __init__(self, id, tytuł, autor, rok):
        self.id = id
        self.tytuł = tytuł
        self.autor = autor
        self.rok = rok


class Biblioteka:
    def __init__(self):
        self.ksiazki = []
        self.wypożyczający = []
        self.wypożyczenia = {}

    def dodaj_książkę(self, tytuł, autor, rok):
        nowe_id = len(self.ksiazki) + 1
        nowa_ksiazka = Książka(nowe_id, tytuł, autor, rok)
        self.ksiazki.append(nowa_ksiazka)

    def wyświetl_książki(self):
        sorted_books = sorted(self.ksiazki, key=lambda x: x.autor.nazwisko.lower())
        for książka in sorted_books:
            print(f"{książka.tytuł}, {książka.autor.nazwisko}, {książka.rok}")

    def dodaj_wypożyczającego(self, imię, nazwisko, email):
        nowe_id = len(self.wypożyczający) + 1
        nowy_wypożyczający = Wypożyczający(imię, nazwisko, email, nowe_id)
        self.wypożyczający.append(nowy_wypożyczający)

    def wypożycz_książkę(self, id_książki, id_wypożyczającego):
        if id_książki in self.wypożyczenia:
            print("Książka jest już wypożyczona.")
        else:
            self.wypożyczenia[id_książki] = id_wypożyczającego

    def wyświetl_wypożyczenia(self):
        for id_książki, id_wypożyczającego in self.wypożyczenia.items():
            książka = next((ks for ks in self.ksiazki if ks.id == id_książki), None)
            wypożyczający = next((wp for wp in self.wypożyczający if wp.id == id_wypożyczającego), None)
            if książka and wypożyczający:
                print(f"Książka '{książka.tytuł}' wypożyczona przez {wypożyczający.imię} {wypożyczający.nazwisko}")


if __name__ == "__main__":
    biblioteka = Biblioteka()

    autor1 = Osoba("Adam", "Mickiewicz")
    autor2 = Osoba("Henryk", "Sienkiewicz")
    biblioteka.dodaj_książkę("Pan Tadeusz", autor1, 1834)
    biblioteka.dodaj_książkę("Quo Vadis", autor2, 1896)

    biblioteka.dodaj_wypożyczającego("Jan", "Kowalski", "jan.kowalski@example.com")
    biblioteka.dodaj_wypożyczającego("Anna", "Nowak", "anna.nowak@example.com")

    print("Książki w bibliotece:")
    biblioteka.wyświetl_książki()

    biblioteka.wypożycz_książkę(1, 1)

    print("\nWypożyczenia:")
    biblioteka.wyświetl_wypożyczenia()
