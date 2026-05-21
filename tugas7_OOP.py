kbps= float(input("masukan jaringan mbps"))
mbps = kbps/1000

if mbps >= 50:
 kategori ="sangat cepat (A)"
elif mbps >= 20:
 kategori ="cepat(B)"
elif mbps >= 5:
 kategori ="lambat(C)"
else:

 kategori = "Kurang(D) - Memerlukan perbaikan"

print("hasil evaluasi:", kategori)