import math


def penjumlahan(bilangan1, bilangan2):
    hasil = bilangan1 + bilangan2
    print(f"Hasil penjumlahan dari {bilangan1} + {bilangan2} = {hasil}")


def pengurangan(bilangan1, bilangan2):
    hasil = bilangan1 - bilangan2
    print(f"Hasil pengurangan dari {bilangan1} - {bilangan2} = {hasil}")


def perkalian(bilangan1, bilangan2):
    hasil = bilangan1 * bilangan2
    print(f"Hasil perkalian dari {bilangan1} * {bilangan2} = {hasil}")


def pembagian(bilangan1, bilangan2):
    hasil = bilangan1 / bilangan2
    print(f"Hasil pembagian dari {bilangan1} / {bilangan2} = {hasil}")


def pangkat(bilangan1, bilangan2):
    hasil = math.pow(bilangan1, bilangan2)
    print(f"Hasil dari {bilangan1} pangkat {bilangan2} = {hasil}")


# penjumlahan(10, 10)
# pengurangan(10, 10)
# perkalian(10, 10)
# pembagian(10, 10)
# pangkat(10, 2)
