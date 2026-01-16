# NIM/Nama: 19625114/Ghina Emelia Yantes
# Tanggal: 14 November 2025
# Deskripsi: Penanggalan Martian Tuan Vin (Problem 3)

bulan = ["Solan", "Lunara", "Terran", "Pyron", "Aquen", "Zephyr", "Umbra", "Lumen", "Astra", "Dimensi"]

# Jumlah hari 9 bulan (Solan s/d Astra)
banyak_hari = [37, 38, 39, 40, 39, 36, 41, 36, 37]

def hari_dimensi(tahun):
    x = tahun % 5
    if x == 0:
        return 5
    else:
        return x

def banyak_hari_perbulan(tahun):
    perbulan = list(banyak_hari) 
    perbulan.append(hari_dimensi(tahun))
    return perbulan

def total(tahun):
    return 343 + hari_dimensi(tahun)

def penanggalan(tanggal, bulan, tahun):
    total_hari = 0  
 
    for i in range(tahun):
        total_hari += total(i) 
 
    panjang_bulan_tahun_ini = banyak_hari_perbulan(tahun)
    
    for i in range(bulan - 1): 
        total_hari += panjang_bulan_tahun_ini[i]
        
    total_hari += tanggal
    
    return total_hari

def konversi_ke_tanggal(total_hari): 
    tahun = 0
    hari_tahun_ini = total(tahun) 
    
    while total_hari > hari_tahun_ini:
        total_hari -= hari_tahun_ini
        tahun += 1
        hari_tahun_ini = total(tahun)
        
    bulan_ke = 1 
    panjang_bulan = banyak_hari_perbulan(tahun) 
    
    for i in panjang_bulan:
        if total_hari <= i:
            break 
        
        total_hari -= i 
        bulan_ke += 1
        
    tanggal = total_hari

    nama_bulan_ini = bulan[bulan_ke - 1]
    
    return (tanggal, nama_bulan_ini, tahun)

str_tanggal = input("Masukkan tanggal: ")
str_fungsi = input("Masukkan fungsi: ")
n = int(input("Masukkan n: "))

parts = str_tanggal.split() 
tgl_awal = int(parts[0])
bln_awal = int(parts[1])
thn_awal = int(parts[2])

hari_awal_abs = penanggalan(tgl_awal, bln_awal, thn_awal)

if str_fungsi == "setelah":
    hari_akhir_abs = hari_awal_abs + n
elif str_fungsi == "sebelum":
    hari_akhir_abs = hari_awal_abs - n
else:
    hari_akhir_abs = hari_awal_abs 

(tgl_akhir, nama_bulan_akhir, thn_akhir) = konversi_ke_tanggal(hari_akhir_abs)

print(f"{n} hari {str_fungsi}nya adalah {tgl_akhir} {nama_bulan_akhir} {thn_akhir}")