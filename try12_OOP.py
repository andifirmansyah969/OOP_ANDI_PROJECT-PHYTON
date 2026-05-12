#Contoh Struktur Percabangan If
#input data dari pengguna
nilai_ujian = float(input("masukkan nilai ujian siswa: "))

if nilai_ujian >= 90:
 predikat ="sangat Baik (A)"
elif nilai_ujian >=75:
 predikat ="Baik(B)"
elif nilai_ujian >=60:
 predikat ="Cukup(C)"
else:
 predikat = "Kurang(D) - Memerlukan Remedial"
 

#Menampilkan hasil kategori
print("Hasil Evaluasi", predikat)