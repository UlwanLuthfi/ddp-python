import module
import module as hitung
from module import pangkat, penjumlahan
from module import *
from module import pangkat as jokowi, penjumlahan as prabowo

print("====== Menggunakan Modul - 1 ======")
module.penjumlahan(10, 10)
module.pengurangan(10, 10)

print("\n====== Menggunakan Modul - Alias ======")
hitung.perkalian(10, 10)
hitung.pembagian(10, 10)

print("\n====== Menggunakan Modul - Sebagian Fungsi ======")
pangkat(10, 2)
penjumlahan(10, 10)

print("\n====== Menggunakan Modul - Seluruh Fungsi ======")
penjumlahan(10, 10)
pengurangan(10, 10)
perkalian(10, 10)
pembagian(10, 10)
pangkat(10, 2)

print("\n====== Menggunakan Modul - Alias Fungsi ======")
jokowi(10, 2)
prabowo(10, 10)
