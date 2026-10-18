# DIAJENG PERMATASARI
# 065002600031
# PRAKTIKUM ALGORITMA - Program Sederhana dalam Phyton

# input bulan dengan validasi while
while True:
    bulan = int(input("Masukkan bulan (1-12): "))
    if 1 <= bulan <= 12:
        break
    else:
        print("Bulan tidak valid! Masukkan 1-12.")

# Input tahun dengan validasi while
while True:
    tahun = int(input("Masukkan tahun: "))
    if tahun > 0:
        break
    else:
        print("Tahun harus lebih dari 0!")

# Cek kabisat
is_kabisat = (tahun % 4 == 0 and tahun % 100 != 0) or (tahun % 400 == 0)

# Tentukan jumlah hari
if bulan == 2:
    if is_kabisat:
        hari = 29
    else:
        hari = 28
elif bulan in [4, 6, 9, 11]:
    hari = 30
else:
    hari = 31

print(f"Bulan {bulan} tahun {tahun} memiliki {hari} hari.")

