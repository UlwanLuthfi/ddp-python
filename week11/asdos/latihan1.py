class Lingkaran:
    jari2 = 0
    PHI = 3.14

    def __init__(self, jari2):
        self.jari2 = jari2

    def hitung_luas(self):
        luas = self.PHI * (self.jari2**2)

        print(f"Luas lingkaran dengan jari-jari {self.jari2} adalah {luas:.2f}")

    def hitung_keliling(self):
        keliling = 2 * self.PHI * self.jari2

        print(
            f"Keliling lingkaran dengan jari-jari {self.jari2} adalah {keliling:.2f}\n"
        )
