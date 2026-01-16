# NIM/Nama: Ghina Emelia Yantes
# Tanggal: 17 Oktober 2025
# Deskripsi: Vidio Gim Tuan Vin (Problem 3)

moral = float(input("Masukkan moral pasukan: "))
wei = int(input("Masukkan banyak prajurit Kerajaan Wei: "))
jarak_wei = int(input("Masukkan jarak tempuh Kerajaan Wei: "))
wu = int(input("Masukkan banyak prajurit Kerajaan Wu: "))
jarak_wu = int(input("Masukkan jarak tempuh Kerajaan Wu: "))

# variabel lain
moral_wei = moral + 0.05

# menghitung power point awal
PP_wu = wu * moral // jarak_wu
PP_wei = wei * moral_wei // jarak_wei


if jarak_wei < jarak_wu:
    PP_wei = PP_wei + 800
    if PP_wu > PP_wei:
        print(f"Kerajaan Wu menang dari Kerajaan Wei dengan selisih sebesar {int(PP_wu - PP_wei)} PP.")
    elif PP_wei > PP_wu:
        print(f"Kerajaan Wei menang dari Kerajaan Wu dengan selisih sebesar {int(PP_wei - PP_wu)} PP.")
    else:
        print("Tidak ada kerjaan yang menang")
elif jarak_wei >= jarak_wu and PP_wu < PP_wei:  
    PP_wu = PP_wu + 1500    
    if PP_wu > PP_wei:
        print(f"Kerajaan Wu menang dari Kerajaan Wei dengan selisih sebesar {int(PP_wu - PP_wei)} PP.")
    elif PP_wei > PP_wu:
        print(f"Kerajaan Wei menang dari Kerajaan Wu dengan selisih sebesar {int(PP_wei - PP_wu)} PP.")
    else:
        print("Tidak ada kerjaan yang menang")
elif jarak_wei >= jarak_wu and PP_wu >= PP_wei:      
    if PP_wu > PP_wei:
        print(f"Kerajaan Wu menang dari Kerajaan Wei dengan selisih sebesar {int(PP_wu - PP_wei)} PP.")
    elif PP_wei > PP_wu:
        print(f"Kerajaan Wei menang dari Kerajaan Wu dengan selisih sebesar {int(PP_wei - PP_wu)} PP.")
    else:
        print("Tidak ada kerjaan yang menang")
else:
    if PP_wu > PP_wei:
        print(f"Kerajaan Wu menang dari Kerajaan Wei dengan selisih sebesar {int(PP_wu - PP_wei)} PP.")
    elif PP_wei > PP_wu:
        print(f"Kerajaan Wei menang dari Kerajaan Wu dengan selisih sebesar {int(PP_wei - PP_wu)} PP.")
    else:
        print("Tidak ada kerajaan yang menang")
