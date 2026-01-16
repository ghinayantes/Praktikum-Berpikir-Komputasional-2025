# NIM/Nama: Ghina Emelia Yantes
# Tanggal: 17 Oktober 2025
# Deskripsi: Koordinat Tuan Mik (Problem 2)

# KAMUS
# x1 -- x4 = int (koordinat sumbu x titik)
# y1 -- y4 = int (koordinat sumbu y titik)

x1 = int(input("Masukkan titik X1: "))
y1 = int(input("Masukkan titik Y1: "))
x2 = int(input("Masukkan titik X2: "))
y2 = int(input("Masukkan titik Y2: "))
x3 = int(input("Masukkan titik X3: "))
y3 = int(input("Masukkan titik Y3: "))
x4 = int(input("Masukkan titik X4: "))
y4 = int(input("Masukkan titik Y4: "))

# kondisi
if (x1 == x3 and x2 == x4) or (x1 == x4 and x2 == x3) or (x1 == x2 and x3 == x4):
    if (y1 == y3 and y2 == y4) or (y1 == y4 and y2 == y3) or (y1 == y2 and y3 == y4):
         print("Keempat titik tersebut membentuk persegi")
    elif (x1 != x2 != x3 != x4) or ((y1 != y2 != y3 != y4)):
         print("Keempat titik tersebut tidak membentuk persegi")
    else:
         print("Keempat titik tersebut tidak membentuk persegi")
else:
     print("Keempat titik tersebut tidak membentuk persegi")