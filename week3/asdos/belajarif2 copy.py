nama = input("Masukan nama mahasiswa: ")
tinggiBadan = int(input("Masukan tinggi badan: "))
beratBadan = int(input("Masukan Berat Badan: "))
tinggiBadanMeter = tinggiBadan / 100
bmi = beratBadan / (tinggiBadanMeter * tinggiBadanMeter)

# Menentukan bmi
if bmi >= 30:
    kategori = "Obesitas"
elif bmi >= 25 and bmi < 30:
    kategori = "Kelebihan berat badan"
elif bmi >= 18.5 and bmi < 25:
    kategori = "Ideal"
elif bmi < 18.5:
    kategori = "Kurus"

print(
    "Nama:",
    nama,
    "\nTinggi Badan",
    tinggiBadan,
    "cm",
    "\nBerat Badan:",
    beratBadan,
    "kg",
    "\nBMI:",
    bmi,
    "\nKategori:",
    kategori,
)
