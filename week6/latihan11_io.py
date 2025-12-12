nama = input("Nama Siswa: ")
mataPelajaran = str(input("Mata Pelajaran: "))
nilai = (float(input("Nilai: ")) * 100) / 100

# Tuple & List
keterangan = ("Gagal", "Lulus")[nilai >= 60]

# Cetak format print
print(
    "Nama Siswa: %s"
    "\nMata Pelajaran: %s"
    "\nNilai: %.2f"
    "\nKeterangan: %s" % (nama, mataPelajaran, nilai, keterangan),
)
