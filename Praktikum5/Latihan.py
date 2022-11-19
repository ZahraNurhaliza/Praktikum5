# Latihan
print("Nama: Zahra Nurhaliza")
print("Nim: 312210364")

# Membuat List sebanyak 5 elemen dengan nilai bebas
#akses list
c = [10, 27, 35, 80, 95]
print(c) #Menampilkan semua elemen
print(c[2]) #Menampilkan elemen ke 3
print(c[1:3]) #Menampilkan elemen ke 2 sampai dengan ke 4
print(c[4]) #Menampilkan elemen terakhir

print("-------------------------------------------------------------")
#ubah elemen list
c[3] = 30 #Mengubah elemen ke 4
print(c[3]) #Menampilkan elemen ke 4 yang sudah diganti nilainya
c[3:4] = 30, 33 #Mengubah elemen ke 4 sampai dengan elemen terakhir
print(c[3:5]) #Menampilkan elemen ke 4 sampai dengan elemen terakhir

print("-----------------------------------------------------------------")
#tambah elemen list
d = c[0:2] #Mengambil 2 bagian dari list pertama (c) dan jadikan list ke 2 (d)
print(d)
d.append(17) #Menambahkan list d dengan nilai string
print(d)
d.extend([45, 70, 99]) #Menambhakan list d dengan 3 nilai
print(d)
e = c + d #Menggabungkan list d dengan list a
print(e)