# Latihan sederhana konversi suhu
print("==== KONVERSI SUHU ====")

# Celcius
celcius = float(input("Masukan data dalam celcius = "))
print("Suhu adalah:", celcius, "Celcius")

# Celcius ke Reamur
reamur = (4 / 5) * celcius
print("Suhu dalam reamur adalah:", reamur)

# Celcius ke Fahrenheit
fahrenheit = (9 / 5) * celcius + 32
print("Suhu dalam fahrenheit adalah:", fahrenheit)

# Celcius ke Kelvin
kelvin = celcius + 273
print("Suhu dalam kelvin adalah:", kelvin)
