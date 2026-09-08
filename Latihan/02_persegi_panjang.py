# Input kasus 1
print("=== Kasus 1 ===")
panjang1 = float(input("Masukkan panjang (cm): "))
lebar1 = float(input("Masukkan lebar (cm): "))

luas1 = panjang1 * lebar1
keliling1 = 2 * (panjang1 + lebar1)

# Input kasus 2
print("\n=== Kasus 2 ===")
panjang2 = float(input("Masukkan panjang (cm): "))
lebar2 = float(input("Masukkan lebar (cm): "))

luas2 = panjang2 * lebar2
keliling2 = 2 * (panjang2 + lebar2)

# Tampilkan hasil
print("\n--- Hasil Perhitungan ---")
print(f"Kasus 1 → Luas: {luas1:.2f} cm², Keliling: {keliling1:.2f} cm")
print(f"Kasus 2 → Luas: {luas2:.2f} cm², Keliling: {keliling2:.2f} cm")
