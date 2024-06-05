class Osoba:
    def __init__(self, imie, nazwisko):
        self.imie = imie
        self.nazwisko = nazwisko

    def __eq__(self, other):
        for i, eli in enumerate(self.nazwisko):
            if not eli == other.nazwisko[i]:
                return False
        if len(self.nazwisko) != len(other.nazwisko):
            return False
        return True

    def __lt__(self, other):
        # Porównujemy najpierw nazwiska, a jeśli są takie same, porównujemy imiona
        if self.nazwisko == other.nazwisko:
            return self.imie < other.imie
        return self.nazwisko < other.nazwisko


o1 = Osoba('asd', 'qwe')
o2 = Osoba('asd', 'qwe')
o3 = Osoba('asd', 'qwer')
print(o1 == o2)
print(o1 == o3)
print(o1 < o2)
print(o1 < o3)
