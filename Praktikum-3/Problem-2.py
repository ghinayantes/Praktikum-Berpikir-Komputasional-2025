# NIM/Nama: Ghina Emelia Yantes
# Tanggal: 31 Oktober 2025
# Deskripsi: Lampu Tuan Mik

# KAMUS

n = int(input("Jumlah lampu dan saklar: "))
lampu = [0] * n

selesai = False
while not selesai:
    saklar = int(input("Masukkan nomor saklar yang ditekan: "))
    if saklar == -1:
        selesai = True
    else:
        for i in range(n):
            if (i + 1) % saklar == 0:
                if lampu[i] == 0:
                    lampu[i] = 1  
                else:
                    lampu[i] = 0  

print("Status lampu:")
for i in range(n):
    if lampu[i] == 1:
        print(f"Lampu {i + 1}: Menyala")
    else:
        print(f"Lampu {i + 1}: Mati")