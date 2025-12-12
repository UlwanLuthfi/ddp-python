class Gempa:
    # Atribut Class
    lokasi = ""
    skala = 0

    # Method Constructor
    def __init__(self, lokasi, skala):
        self.lokasi = lokasi
        self.skala = skala

    # Method Menghitung Dampak
    def dampak(self):
        if self.skala < 2:
            keterangan = "Tidak terasa"
        elif self.skala >= 2 and self.skala < 4:
            keterangan = "Bangunan retak-retak"
        elif self.skala >= 4 and self.skala < 6:
            keterangan = "Bangunan roboh"
        else:
            keterangan = "Berpotensi tsunami"

        print(
            f"Telah terjadi gempa di {self.lokasi} dengan skala {self.skala} Richter, berdampak {keterangan}"
        )
