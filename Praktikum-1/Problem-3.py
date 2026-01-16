# NIM/Nama: Ghina Emelia Yantes
# Tanggal: 3 Oktober 2025
# deskripsi: Problem 3 (Kompleksitas algoritma Nona Sal)

# KAMUS
# n = banyak operasi 
# t = waktu per operasi
# o = persen overhead
# f = frekuensi

# input data
n = int(input("masukkan jumlah operasi: "))
t = int(input("masukkan waktu per operasi (mikrodetik): "))
o = int(input("Masukkan overhead (persen): "))
f = int(input("Masukkan frekuensi (GHz): "))

# rumus 
t_tot = n * t
t_over = t_tot * (o/100)
t_tot_mikro = t_tot + t_over
t_tot_detik = t_tot_mikro / 1000000

f_hz = f * 1000000000

clock  = t_tot_detik * f_hz

efisiensi = n / t_tot_detik

# hasil
print(f"Clock cycle yang dihasilkan adalah {clock} cycle dengan efisiensi {efisiensi} operasi /detik")