# 1. Tampilkan judul program
print("KALKULATOR KOORDINAT DUA TITIK")

# 2. Baca x1, y1, x2, dan y2 sebagai float
x1 = float(input("x titik A: "))
y1 = float(input("y titik A: "))
x2 = float(input("x titik B: "))
y2 = float(input("y titik B: "))

# 3. Hitung dx dan dy
dx = x2 - x1
dy = y2 - y1

# 4. Hitung kuadrat dx dan dy, jumlahkan, lalu pangkatkan 0.5
jarak = (dx**2 + dy**2) ** 0.5

# 5. Hitung koordinat titik tengah
x_tengah = (x1 + x2) / 2
y_tengah = (y1 + y2) / 2

# 6. Tampilkan seluruh hasil menggunakan f-string
print(f"\nTitik A : ({x1:.2f}, {y1:.2f})")
print(f"Titik B : ({x2:.2f}, {y2:.2f})")
print(f"Perubahan : dx = {dx:.2f}, dy = {dy:.2f}")
print(f"Jarak A ke B : {jarak:.2f}")
print(f"Titik tengah : ({x_tengah:.2f}, {y_tengah:.2f})")
