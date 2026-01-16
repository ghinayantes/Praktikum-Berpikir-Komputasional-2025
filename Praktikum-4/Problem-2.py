# NIM/Nama: 19625114/Ghina Emelia Yantes
# Tanggal: 14 November 2025
# Deskripsi: Bahasa rahasia Tuan Vin (Problem 2)

def cek_huruf(kata):
    vokal = "aiueo"
    konsonan = "bcdfghjklmnpqrstvwxyz"
    ada_vokal = False
    ada_konsonan = False

    for i in kata:
        if i in vokal:
            ada_vokal = True
        elif i in konsonan:     
            ada_konsonan = True

    return ada_vokal and ada_konsonan


# Fungsi untuk Mengecek huruf yang bersebelahan
def sebelahanbeda(kata):
    for i in range(len(kata) - 1):
        if kata[i] == kata[i + 1]:   
            return False
    return True

# Fungsi untuk Mengecek palindrom
def palindrom(kata):
    balik_kata = ""   
    for i in kata:
        balik_kata = i + balik_kata
    return kata == balik_kata

kata = input("Masukkan kata: ")

if cek_huruf(kata) == True and sebelahanbeda(kata) == True and palindrom(kata) == True:
    print("Kata tersebut termasuk dalam Bahasa Vin")
else:
    print("Kata tersebut tidak termasuk dalam Bahasa Vin")