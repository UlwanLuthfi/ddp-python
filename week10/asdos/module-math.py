import math

print("====== Simulasi Pergerakan / Jarak Tempuh ======")
# Kordinat titik awal
x1 = float(input("Posisi Awal X: "))
y1 = float(input("Posisi Awal Y: "))

# Kordinat titik akhir
x2 = float(input("Posisi Akhir X: "))
y2 = float(input("Posisi Akhir Y: "))

# Fungsi menghitung jarak tempuh
jarak = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)


# Print hasil
print(f"Jarak tempuh Anda: {round(jarak, 2)} meter")
