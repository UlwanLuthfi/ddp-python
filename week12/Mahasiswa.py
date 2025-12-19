from Person import Person


class Mahasiswa(Person):
    def __init__(
        self, nama: str, gender: str, umur: int, prodi: str, semester: int, ipk: int
    ):
        super().__init__(nama, gender, umur)
        self.prodi = prodi
        self.semester = semester
        self.ipk = ipk

    def cetak(self):
        super().cetak()
        print(f"Prodi\t\t: {self.prodi}")
        print(f"Semester\t: {self.semester}")
        print(f"IPK\t\t: {self.ipk}")
        print("----------------------------")
