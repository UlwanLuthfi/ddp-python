class BeratIdeal:
    tinggi = 0
    berat = 0

    def __init__(self, tinggi, berat):
        self.tinggi = tinggi / 100
        self.berat = berat

    def perhitungan(self):
        bmi = self.berat / (self.tinggi * self.tinggi)

        if bmi < 18.5:
            keterangan = "Kurus"
        elif bmi >= 18.5 and bmi <= 24.9:
            keterangan = "Ideal"
        elif bmi >= 25 and bmi <= 29.9:
            keterangan = "Gemuk"
        else:
            keterangan = "Obesitas"

        print(bmi)

        print(
            f"Hasil perhitungan BMI dengan \nBerat: {self.berat} \nTinggi: {self.tinggi} \nKeterangan: {keterangan}"
        )
