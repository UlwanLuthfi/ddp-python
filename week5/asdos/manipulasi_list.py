# Manipulasi list
data = ["ucup", "ujang", "jul", "ilham"]

# Mengambil data dari list ini
cobaData = data[-1]
print(cobaData)
cobaData = data[1]
print(cobaData)

# Mengambil info panjang list
jumlahData = len(data)
print(jumlahData)

# Menambahkan item kedalam list
print("\nData sebelum diubah:\n", data)

data.insert(1, "bagas")
print("\nData sesudah insert:\n", data)

# Menambahkan data diakhir list
data.append("hilmi")
print("\nData sesudah append:\n", data)

# Menambahkan list dengan list
dataBaru = ["faris", "apoy", "joni"]
data.extend(dataBaru)
print("\nData sesudah extend:\n", data)

# Mengubah item list
data[3] = "KDM"
print("\nData sesudah diubah:\n", data)

# Menghapus item list
data.remove("hilmi")
del data[3]
data.pop()
print("\nData sesudah remove, delete dan pop:\n", data)
