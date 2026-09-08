BOBOT_TUGAS = 0.30
BOBOT_UTS = 0.30
BOBOT_UAS = 0.40

# Input nilai
nama = input("Nama mahasiswa: ")
nilai_tugas = float(input("Nilai tugas: "))
nilai_uts = float(input("Nilai UTS: "))
nilai_uas = float(input("Nilai UAS: "))

# Hitung nilai akhir berdasarkan bobot
nilai_akhir = (
	nilai_tugas * BOBOT_TUGAS
	+ nilai_uts * BOBOT_UTS
	+ nilai_uas * BOBOT_UAS
)

# Tampilkan hasil
print("\n=== Hasil Nilai ===")
print(f"Nama        : {nama}")
print(f"Nilai tugas : {nilai_tugas:.2f}")
print(f"Nilai UTS   : {nilai_uts:.2f}")
print(f"Nilai UAS   : {nilai_uas:.2f}")
print(f"Nilai akhir : {nilai_akhir:.2f}")
