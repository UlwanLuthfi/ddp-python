class Bank:
    nomorRekening = ""
    nama = ""
    saldo = 0
    jumlahNasabah = 0
    BANK = "Bank Syariah Nurul Fikri"

    def __init__(self, no, nasabah, saldo):
        self.nomorRekening = no
        self.nama = nasabah
        self.saldo = saldo
        Bank.jumlahNasabah += 1

    def nabung(self, uang):
        self.saldo += uang

    def tarik(self, uang):
        self.saldo -= uang

    def cetak(self):
        print(
            Bank.BANK,
            "\n===================================",
            f"\nNo. Rekening\t: {self.nomorRekening}",
            f"\nNama Nasabah\t: {self.nama}",
            f"\nSaldo\t\t: Rp. {self.saldo:,}",
            "\n===================================\n",
        )
