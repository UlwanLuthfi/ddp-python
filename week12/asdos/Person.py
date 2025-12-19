class Person:
    def __init__(self, nama: str, gender: str, umur: int):
        self.nama = nama
        self.gender = gender
        self.umur = umur

    def cetak(self):
        print(f"Nama\t\t: {self.nama}")
        print(f"Jenis Kelamin\t: {self.gender}")
        print(f"Umur\t\t: {self.umur}")
