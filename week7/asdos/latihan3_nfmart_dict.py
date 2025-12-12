# 1 - Buat dictionary
menu = {
    "Ayam Bakar": 20,
    "Sate Ayam": 25,
    "Ayam Geprek": 15,
    "Jus Jeruk": 10,
    "Teh Manis": 5,
    "Teh Tawar": 2,
}

# 2 - Simpan data ke list/variable baru
cart = []
totalHarga = 0

# 3 - Daftar menu
print("---------- Menu ----------")
for key, value in menu.items():
    print(f"{key:11} : {value}K")
print("--------------------------\n")

# 4 - Memilih menu
while True:
    pesanan = input("Pilih makanan: ").title()
    print("Ketik 'exit' untuk keluar")

    if pesanan == "Exit":
        break
    elif menu.get(pesanan) is not None:
        cart.append(pesanan)

# 5 - loop pesanan dan total
print("\n---------- Pesanan ----------")
for pesanan in cart:
    totalHarga += menu.get(pesanan)
    print(pesanan)
print(f"Total harga: {totalHarga}K")
print("-----------------------------\n")
