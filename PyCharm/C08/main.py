from Zakupy.towar import Towar
from Zakupy.lista_zakupow import ListaZakupow
from Zakupy.exceptions import BelowZero


def wczytaj_dane():
    while True:
        try:
            nazwa = input("Podaj nazwę towaru: ")
            if nazwa == "quit":
                raise Exception
            cena = float(input("Podaj cenę jednostkową: "))
            if cena < 0:
                raise BelowZero
            liczba = int(input("Podaj ilość do kupienia: "))
            if liczba < 0:
                raise BelowZero
            return nazwa, cena, liczba
        except ValueError:
            print("Nieprawidłowe dane. Spróbuj ponownie.")


if __name__ == "__main__":
    lista_zakupow = ListaZakupow()

    while True:
        try:
            nazwa, cena, liczba = wczytaj_dane()
            towar = Towar(nazwa, cena)
            lista_zakupow.dodaj_do_zakupow(towar, liczba)
            readinput = input("Kontynuować dodawanie? (tak/nie): ")
            if readinput == "nie":
                break
        except BelowZero as e:
            print(e)

    print("\nZakończono dodawanie towarów.")