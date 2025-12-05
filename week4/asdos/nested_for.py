# # Nested loop
# # Segitiga siku
# for baris in range(5):
#     for bintang in range(baris + 1):
#         print("*", end="")
#     print("")

# # Segitiga siku terbalik
# startingPoint = 5
# for baris in range(0, startingPoint):
#     for bintang in range(0, startingPoint):
#         print("* ", end="")
#     startingPoint -= 1
#     print("")

# Segitiga sama kaki
jumlahBaris = int(input("Masukan jumlah baris: "))
karakter = input("Masukan karakter yang diinginkan: ")
space = jumlahBaris - 1
for baris in range(0, jumlahBaris):
    for spasi in range(0, space):
        print(" ", end="")
    space -= 1
    for bintang in range(0, baris + 1):
        print(karakter + " ", end="")
    print("")
