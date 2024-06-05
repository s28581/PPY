from .exceptions import BelowZero


class ListaZakupow:
    def __init__(self, lista_zakupow=None):
        self.lista = lista_zakupow if lista_zakupow else []
        self.sumaryczna_cena = 0

        for towar, liczba in self.lista:
            self.sumaryczna_cena += towar.cena_jednostkowa * liczba

    def dodaj_do_zakupow(self, towar, liczba):
        if liczba < 0 or towar.cena_jednostkowa < 0:
            raise BelowZero("Cena lub ilość nie może być mniejsza od zera.")
        self.lista.append((towar, liczba))
        self.sumaryczna_cena += towar.cena_jednostkowa * liczba
