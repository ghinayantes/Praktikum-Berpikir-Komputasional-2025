# NIM/Nama: Ghina Emelia Yantes
# Tanggal: 31 Oktober 2025
# Deskripsi: Permainan Nona Sal

n = int(input("Masukkan besar n: "))

deb = [0] * n
mik = [0] * n
vin = [0] * n

i = 0
while i < n:
    deb[i] = int(input(f"Masukkan angka ke-{i+1} Nona Deb: "))
    i = i + 1

i = 0
while i < n:
    mik[i] = int(input(f"Masukkan angka ke-{i+1} Tuan Mik: "))
    i = i + 1

i = 0
while i < n:
    vin[i] = int(input(f"Masukkan angka ke-{i+1} Tuan Vin: "))
    i = i + 1

sisa_deb = n
sisa_mik = n
sisa_vin = n

pemenang_deb = 0
pemenang_mik = 0
pemenang_vin = 0

while not (pemenang_deb == 1 or pemenang_mik == 1 or pemenang_vin == 1):
    panggil = int(input("Masukkan angka yang dipanggil: "))

    min_selisih = abs(panggil - deb[0])
    idx_min = 0
    i = 1
    while i < n:
        if abs(panggil - deb[i]) < min_selisih:
            min_selisih = abs(panggil - deb[i])
            idx_min = i
        i = i + 1
    if deb[idx_min] != -1:
        deb[idx_min] = -1
        sisa_deb = sisa_deb - 1

    min_selisih = abs(panggil - mik[0])
    idx_min = 0
    i = 1
    while i < n:
        if abs(panggil - mik[i]) < min_selisih:
            min_selisih = abs(panggil - mik[i])
            idx_min = i
        i = i + 1
    if mik[idx_min] != -1:
        mik[idx_min] = -1
        sisa_mik = sisa_mik - 1

    min_selisih = abs(panggil - vin[0])
    idx_min = 0
    i = 1
    while i < n:
        if abs(panggil - vin[i]) < min_selisih:
            min_selisih = abs(panggil - vin[i])
            idx_min = i
        i = i + 1
    if vin[idx_min] != -1:
        vin[idx_min] = -1
        sisa_vin = sisa_vin - 1

    if sisa_deb == 0:
        pemenang_deb = 1
    if sisa_mik == 0:
        pemenang_mik = 1
    if sisa_vin == 0:
        pemenang_vin = 1

print("Pemenang dari permainan ini adalah", end=" ")

if pemenang_deb == 1:
    print("Nona Deb", end="")
if pemenang_mik == 1:
    if pemenang_deb == 1:
        print(",", end=" ")
    print("Tuan Mik", end="")
if pemenang_vin == 1:
    if pemenang_deb == 1 or pemenang_mik == 1:
        print(",", end=" ")
    print("Tuan Vin")