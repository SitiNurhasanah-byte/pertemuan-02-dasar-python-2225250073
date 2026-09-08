# Konstanta tahun sekarang
TAHUN_SEKARANG = 2026

# Input biodata
nama = input("Nama: ")
nim = input("NIM: ")
kelas = input("Kelas: ")
tahun_lahir = int(input("Tahun lahir: "))

# Hitung umur
umur = TAHUN_SEKARANG - tahun_lahir

# Tampilkan kartu biodata dengan f-string
print(f"\nNama : {nama}")
print(f"NIM  : {nim}")
print(f"Kelas: {kelas}")
print(f"Umur : sekitar {umur} tahun")

