from Mahasiswa import Mahasiswa
from Dosen import Dosen


def main():
    mahasiswa_list = [
        Mahasiswa("Siti Aminah", "Wanita", 20, "SI", 3, 2.3),
        Mahasiswa("Budi Santoso", "Pria", 23, "TI", 5, 3.75),
    ]

    dosen_list = [
        Dosen("Sirojul Munir", "Pria", 43, "S.Si, M.Kom", "Waket 1"),
        Dosen("Henry Saptono", "Pria", 44, "S.Si, M.Kom", "Ketua LTSI"),
    ]

    dosen_list[0].set_gaji(12_000_000)
    dosen_list[1].set_gaji(10_000_000)

    for obj in mahasiswa_list + dosen_list:
        obj.cetak()


if __name__ == "__main__":
    main()
