# NIM/Nama: Ghina Emelia Yantes
# Tanggal: 3 Oktober 2025
# deskripsi: Problem 2 (Jumlah uang yang dibutuhkan Nona Deb)

uang = int(input("Uang Nona Deb sekarang:"))
harga = int(input("Harga tiket: "))
jumlah = int(input("Jumlah tiket yang dibeli: "))

diskon = 5/100
harga_diskon = harga - harga * diskon

total = jumlah * harga_diskon

pajak = total + (total * 1/10)

uang_kurang = pajak - uang

print(f"Uang Nona Deb sekarang: {uang}")
print(f"Harga tiket: {harga}")
print(f"Jumlah tiket yang dibeli: {jumlah}")
print(f"Nona Deb perlu mengumpulkan uang sebesar: {uang_kurang}")
