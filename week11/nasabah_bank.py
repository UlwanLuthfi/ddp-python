from Bank import *

gigi = Bank("001", "Buffon", 5000000)
cr7 = Bank("007", "Ronaldo", 7000000)
leo = Bank("010", "Messi", 8000000)
salah = Bank("011", "Mohammad Salah", 9000000)

gigi.nabung(2000000)
leo.nabung(2000000)
cr7.nabung(2000000)
salah.nabung(2000000)

gigi.tarik(1000000)
leo.tarik(1000000)
cr7.tarik(1000000)
salah.tarik(1000000)

gigi.cetak()
cr7.cetak()
leo.cetak()
salah.cetak()
print(f"Jumlah Nasabah: {Bank.jumlahNasabah} orang")
