# NIM/Nama: 19625114/Ghina Emelia Yantes
# Tanggal: 14 November 2025
# Deskripsi: Penukaran koin Nona Sal (Problem 1)


def penukaran(perunggu, perak, emas):       # fungsi untuk menghitung penukaran koin perunggu
    print("Nilai tukar: ")                  # prosedur penukaran koin
    print("10 koin perunggu = 1 koin perak")
    print("10 koin perak = 1 koin emas")

    # Input jumlah perunggu (dimisalkan b)
    b = int(input("Masukkan jumlah perunggu: "))

    if b < 10:
        print("Koin Nona Sal tidak cukup untuk ditukarkan.")
        return (0, 0, 0)
    
    # bagian untuk menghitung penukaran koin
    p = b // 10
    sisa_b = b % 10

    e = p // 10
    sisa_p = p % 10  

    bonus_e = e // 5
    e_tot = e + bonus_e

    return(e_tot, sisa_p, sisa_b)

emas, perak, perunggu = penukaran(0, 0, 0)

if emas != 0 or perak != 0 or perunggu != 0:
    print(f"Nona Sal akan mendapatkan {emas} emas, {perak} perak, dan {perunggu} perunggu dari hasil penukaran.")
