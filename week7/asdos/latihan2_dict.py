dataNilai = {"Franco": 90, "Ilham": 60, "Valir": 70, "Argus": 30}

# Cetak all
for nama, nilai in dataNilai.items():
    keterangan = "lulus" if nilai >= 60 else "gagal"
    print(f"Nama siswa: {nama} dan Nilai Siswa: {nilai} dinyatakan {keterangan}")

# Cetak key
for nama in dataNilai.keys():
    print(f"Nama siswa: {nama}")

# Cetak value
for nilai in dataNilai.values():
    print(f"Nilai siswa: {nilai}")
