print("==== Luas Bidang ====")

print("Pilih Bidang: \n1. Lingkaran \n2. Segitiga \n3. Persegi Panjang")

pilihan = int(input("\nPilih nomor bidang: "))

if pilihan == 1:
    bidang = "lingkaran"
    jari2 = float(input("Masukan jari-jari lingkaran: "))
    luas = 3.14 * (jari2 * jari2)

    print(f"Bidang {bidang} dengan jari-jari {jari2} luasnya = {luas}")

elif pilihan == 2:
    bidang = "Segitiga"
    alas = float(input("Masukan alas segitiga: "))
    tinggi = float(input("Masukan tinggi segitiga: "))
    luas = (alas * tinggi) / 2

    print(f"Bidang {bidang} dengan alas {alas} dan tinggi {tinggi} luasnya = {luas}")

elif pilihan == 3:
    bidang = "Persegi Panjang"
    panjang = float(input("Masukan panjang persegi panjang: "))
    lebar = float(input("Masukan lebar persegi panjang: "))
    luas = panjang * lebar

    print(
        f"Bidang {bidang} dengan panjang {panjang} dan lebar {lebar} luasnya = {luas}"
    )

else:
    print("Input nomor bidangnya")
