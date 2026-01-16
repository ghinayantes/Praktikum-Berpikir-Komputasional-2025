# NIM/Nama: Ghina Emelia Yantes
# Tanggal: 17 Oktober 2025
# Deskripsi: Donor darah Nona Sal (Problem 1)

# KAMUS
# usia = int (input umur)
# berat = int (input berat)
# makan = str (input jawaban Ya/Tidak)
# donor = str (input jawaban Ya/Tidak)

usia = int(input("Masukkan usia: "))
berat = int(input("Masukkan berat badan (kg): "))
makan = str(input("Sudah makan dalam 4 jam terakhir? (Ya/Tidak): "))
donor = str(input("Sudah donor dalam 2 bulan terakhir? (Ya/Tidak): "))

# memisahkan kondisi
if usia >= 17 and usia <= 60 and berat >= 45 and makan == "Ya":
    if donor == "Ya":
        print("Tidak layak donor. Alasan: baru saja donor darah dalam 2 bulan terakhir")
    else:
        print("Layak donor darah. Jenis donor: Donor reguler")
elif usia >= 17 and usia <= 60 and berat >= 45 and makan == "Tidak":
    print("Tidak layak donor. Alasan: Belum makan.")
elif usia >= 17 and usia <= 60 and berat > 70 and makan == "Ya" and donor == "Tidak":
    jenis = "Donor Double (disarankan)"
    print(f"Layak donor darah. Jenis donor: {jenis}")
else:
    if usia < 17 or usia > 60:
        print("Tidak layak donor. Alasan: Tidak memenuhi kriteria usia")
    elif berat < 45:
        print("Tidak layak donor. Alasan: Tidak memenuhi kriteria berat badan")
    else:
        print("Tidak layak donor. Alasan: Tidak memenuhi kriteria usia dan berat badan")

