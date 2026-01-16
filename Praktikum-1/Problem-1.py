# NIM/Nama: Ghina Emelia Yantes
# Tanggal: 3 Oktober 2025
# deskripsi: Problem 1 (Menghitung ukuran file gambar Nona Sal)

# KAMUS
# w = lebar gambar
# h = Tinggi gambar 
# d = kedalaman

# input ukuran
w = int(input("Masukkan lebar gambar (pixel): "))
h = int(input("Masukkan  tinggi gambar (pixel): "))
d = int(input("Masukkan kedalaman warna (bit): "))
rasio = int(input("Masukkan rasio kompresi (persen): "))


# menghitung ukuran gambar
ukuran_bit = w * h * d

# konversi ke byte
ukuran_byte = ukuran_bit / 8 

# ukuran setelah dikompresi
persen_sisa = 100 - rasio
dikompresi = ukuran_byte * (persen_sisa/100)

# ukuran ke mb
ukuran_mb = dikompresi / 1000000

print(f"ukuran file gambar setelah kompresi adalah {ukuran_mb : .2f} MB") #tes

