nilai = {"Firda": 89, "Inaya": 100, "Deden": 59, "Fawaz": 77}


print("===== Cetak valuenya saja =====")
for skor in nilai.values():
    print("Data nilai: ", skor)
print()

print("===== Cetak indexnya saja =====")
for nama in nilai.keys():
    print("Nama siswa: ", nama)

print("===== Cetak value dan index =====")
for nama, skor in nilai.items():
    print(f"Nama siswa: {nama} \t Nilai: {skor}")
