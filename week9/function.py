def hitungUmur(tahun_lahir, tahun_sekarang):
    umur = tahun_sekarang - tahun_lahir
    print(f"Siswa yang lahir pada tahun {tahun_lahir} berumur {umur}")


# hitungUmur(2006, 2025)


def status_suhu(suhu):
    if suhu <= 0:
        return "Beku"
    elif suhu <= 16:
        return "Dingin"
    elif suhu <= 20:
        return "Sejuk"
    elif suhu <= 30:
        return "Biasa"
    else:
        return "Panas"


def infoSuhu():
    print("\n\n====== Informasi Suhu di suatu Daerah ======")
    lokasi = input("Masukkan Lokasi\t: ")
    suhu = int(input("Masukkan Suhu\t: "))

    kondisi = status_suhu(suhu)

    print("\n\n====== Informasi Suhu ======")
    print("Lokasi\t:", lokasi)
    print("Suhu\t:", suhu)
    print("Kondisi\t:", kondisi)


# infoSuhu()


def keyword(nama="Firda", pekerjaan="Pelajar", hobi="Memasak"):
    print("\n---------------------------------------")
    print(f"Nama: {nama}")
    print(f"Profesi: {pekerjaan}")
    print(f"Hobi: {hobi}")


# keyword("Fawwaz", "Menghafal Al-quran", "Olahraga")
# keyword("Inaya", hobi="Membaca")
# keyword(pekerjaan="Karyawan")
