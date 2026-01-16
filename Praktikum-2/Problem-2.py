# NIM/Nama: Ghina Emelia Yantes
# Tanggal: 17 Oktober 2025
# Deskripsi: Cek Persegi dengan Metode Jarak

# --- INPUT ---
x1 = int(input("Masukkan titik X1: "))
y1 = int(input("Masukkan titik Y1: "))
x2 = int(input("Masukkan titik X2: "))
y2 = int(input("Masukkan titik Y2: "))
x3 = int(input("Masukkan titik X3: "))
y3 = int(input("Masukkan titik Y3: "))
x4 = int(input("Masukkan titik X4: "))
y4 = int(input("Masukkan titik Y4: "))

# --- PROSES ---
# Kita simpan titik dalam list biar mudah diakses
points = [ (x1, y1), (x2, y2), (x3, y3), (x4, y4) ]

# Fungsi sederhana hitung kuadrat jarak (biar tidak perlu akar/float)
# Rumus: (x_a - x_b)^2 + (y_a - y_b)^2
distances = []

# Bandingkan setiap titik dengan titik lainnya (total 6 kombinasi)
for i in range(4):
    for j in range(i + 1, 4):
        dx = points[i][0] - points[j][0]
        dy = points[i][1] - points[j][1]
        dist_sq = dx**2 + dy**2
        distances.append(dist_sq)

# Urutkan jarak dari kecil ke besar
distances.sort()

# --- CEK KONDISI ---
# distances[0] s/d distances[3] adalah 4 sisi terpendek
# distances[4] s/d distances[5] adalah 2 diagonal terpanjang

is_square = (
    distances[0] > 0 and                # Pastikan bukan titik yang sama
    distances[0] == distances[1] and    # 4 sisi harus sama panjang
    distances[1] == distances[2] and
    distances[2] == distances[3] and
    distances[4] == distances[5]        # 2 diagonal harus sama panjang
)

# --- OUTPUT ---
if is_square:
    print("Keempat titik tersebut membentuk persegi")
else:
    print("Keempat titik tersebut tidak membentuk persegi")