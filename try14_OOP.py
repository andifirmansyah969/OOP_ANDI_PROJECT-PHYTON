#Contoh WHILE Sistem pengisian baterai laptop
#yang akan terus berjalan selama daya mencapai 100%
daya = 7
while daya < 100:
  print("Mengisi daya------ posisi:",daya, "%")
  daya += 5 #Menambahkan daya setiap putaran
 
print("Baterai Penuh")