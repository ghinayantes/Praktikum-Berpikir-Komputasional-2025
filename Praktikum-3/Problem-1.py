# NIM/Nama: Ghina Emelia Yantes
# Tanggal: 31 Oktober 2025
# Deskripsi: Jam tidur Nona Sal

jam = [0] * 7
total = 0


print("Masukkan jam tidur untuk 7 hari:")
for i in range(7):
    print(f"Hari ke-{i+1}: ", end=" ")
    jam[i] = float(input())

for i in range(7):
    total = jam[i] + total
    
jam_rendah = jam[0]
hari_rendah = 1
for i in range(1, 7):
    if jam[i] < jam_rendah:
        jam_rendah = jam[i]
        hari_rendah = i + 1

streak = False
streak_awal = 0

for i in range(5): 
    if jam[i] < 6 and jam[i+1] < 6 and jam[i+2] < 6:
        streak = True
        streak_awal = i + 1  

print(f"Rata-rata jam tidur: {total/7 :.2f} jam per hari")
print(f"Jam tidur paling sedikit: {jam_rendah} jam (hari ke-{hari_rendah})" )

if streak:
    print(f"PERINGATAN: Ditemukan sleep debt streak! Hari ke-{streak_awal} sampai ke-{streak_awal + 2} tidur kurang dari 6 jam berturut-turut.")
else:
    print("Pola tidur sehat! Tidak ada sleep debt streak.")