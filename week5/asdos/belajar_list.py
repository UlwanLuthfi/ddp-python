# list
data = [1, 2, 3, 4]
print(data)

# sekumpulan data numbers
dataNumbers = [1, 2, 3]
print(dataNumbers)

# sekumpulan data boolean
dataBoolean = [True, False, True, False]
print(dataBoolean)

# sekumpulan data campuran
dataCampuran = [1, "ucup", 2, "ujang", 3, True, 4, False]

# list multi-dimensi
listMakanan = [
    ["Bakwan", "Combro", "Misro"],
    ["Sop Iga", "Sop Buntut", "Sop Kaki"],
    ["Nasi Uduk", "Nasi Goreng", "Nasi Rames"],
]

print("=== cetak sesuai index ====")
print(listMakanan[0][0])
print(listMakanan[1][2])
print(listMakanan[2][2])

print("=== cetak semua dengan nested loop ====")
for menu in listMakanan:
    for makanan in menu:
        print(makanan)
