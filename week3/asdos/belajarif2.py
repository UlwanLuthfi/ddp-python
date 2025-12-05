nama = input("Masukan nama mahasiswa: ")
mataPelajaran = input("Masukan mata pelajaran: ")
nilai = int(input("Masukan nilai: "))

# Menentukan grade nilai
if nilai >= 85 and nilai <= 100:
    grade = "A"
elif nilai >= 75 and nilai < 85:
    grade = "B"
elif nilai >= 60 and nilai < 75:
    grade = "C"
elif nilai >= 30 and nilai < 60:
    grade = "D"
else:
    grade = "E"

print("Nama:", nama,
      "\nMata Pelajaran:", mataPelajaran,
      "\nNilai:", nilai,
      "\nGrade:", grade)