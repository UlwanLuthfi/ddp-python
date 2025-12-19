from Person import Person


class Dosen(Person):
    def __init__(
        self, nama: str, gender: str, umur: int, gelar: str, jabatan: str, gaji: int = 0
    ):
        super().__init__(nama, gender, umur)
        self.gelar = gelar
        self.jabatan = jabatan
        self.gaji = gaji

    def set_gaji(self, uang: int):
        self.gaji += uang

    def cetak(self):
        super().cetak()
        print(f"Gelar\t\t: {self.gelar}")
        print(f"Jabatan\t\t: {self.jabatan}")
        print(f"Gaji\t\t: {self.gaji:,}".replace(",", "."))
        print("--------------------------")
