listBuah = ["Pepaya", "Mangga", "Pisang", "Jambu", "Belimbing"]

# ganti buah
print("Buah indeks 2:", listBuah[2])

listBuah[2] = "Apel"
print("Buah indeks 2:", listBuah[2])

# delete buah
print("Buah indeks 4:", listBuah[4])

del listBuah[4]
# print("Buah indeks 4:", listBuah[4])

# insert buah
listBuah.insert(3, "Naga")
listBuah.append("Jeruk")

# print semua buah
print("=== Cetak Semua Buah ===")
for buah in listBuah:
    print("Buah:", buah)

# select element sesuai range
print(listBuah[1:5])
print(listBuah)
