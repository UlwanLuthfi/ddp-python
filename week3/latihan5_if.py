# Latihan if multi kondisi
nama = "Ahmad Sopandi"
jabatan = "Staff"

if jabatan == "Manager":
    gaji = 10000000
elif jabatan == "Asisten Manager":
    gaji = 7000000
elif jabatan == "Staff":
    gaji = 5000000
else:
    gaji = 0

print("Nama pegawai\t:", nama, 
      "\nJabatan\t\t:", jabatan, 
      "\nGaji\t \t:", gaji)
