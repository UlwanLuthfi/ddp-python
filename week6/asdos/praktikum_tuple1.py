nama = str(input("Masukan nama pegawai: "))
jabatan = str(input("Masukan jabatan: "))
agama = str(input("Masukan agama: "))
statusPerkawinan = str(input("Masukan status perkawinan: "))

# Hitung gaji
if jabatan == "Manager":
    gajiPokok = 15000000
elif jabatan == "Asisten Manager":
    gajiPokok = 10000000
elif jabatan == "Supervisor":
    gajiPokok = 7000000
elif jabatan == "Staff":
    gajiPokok = 4000000
else:
    gajiPokok = 0

# Tunjangan Jabatan
tunjanganJabatan = 0.3 * gajiPokok

# BPJS
bpjs = 0.1 * gajiPokok

# Tunjangan Keluarga
tunjanganKeluarga = (0, 0.1 * gajiPokok)[statusPerkawinan == "menikah"]

# Gaji Kotor
gajiKotor = gajiPokok + tunjanganJabatan + bpjs + tunjanganKeluarga

# zakat
zakat = (0, 0.025 * gajiKotor)[agama == "islam" and gajiKotor >= 7000000]

# Gaji bersih
gajiBersih = gajiKotor - zakat

print(
    "Nama Pegawai\t\t: %s"
    "\nJabatan\t\t\t: %s"
    "\nStatus\t\t\t: %s"
    "\nGaji Pokok\t\t: %s"
    "\nTunjangan Jabatan\t: Rp. %i"
    "\nTunjangan Keluarga\t: Rp. %i"
    "\nBPJS\t\t\t: Rp. %i"
    "\nZakat Profesi\t\t: Rp. %.2f"
    "\nGaji Bersih\t\t: Rp. %.2f"
    % (
        nama,
        jabatan,
        statusPerkawinan,
        gajiPokok,
        tunjanganJabatan,
        tunjanganKeluarga,
        bpjs,
        zakat,
        gajiBersih,
    )
)
