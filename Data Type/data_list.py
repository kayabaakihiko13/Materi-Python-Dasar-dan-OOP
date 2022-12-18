# tipe data list merupakan tipe data yang memiliki lebih dari satu value

"""angka=10
angka=20
angka=2
angka=3

contoh di atas kurang efektif,karena setiap line pada value di simpan pada satu variabel tersebut
"""

angka=[10,20,2,3,3,5,73,474]
print(angka)

# operator dan manipulasi data list

## index -- > inti dari index merupakan posisi suatu value pada sebuah variabel
print('nilai pada posisi pertama pada angka adalah:',angka[0])
print('nilai pada posisi kedua pada angka adalah:',angka[1])
print('nilai pada posisi terakhir pada angka adalah:',angka[-1])

## slicing ----> ini dari slicing in merupakan menglihat data sesuai dengan urutan
print('nilai pada posisi awal hingga 4',angka[0:4])
print('nilai dimulai dari posisi ketiga belakang dan sampai akhir',angka[-3:])

# menghitung jumlah value nya pada data

print('jumlah angka 3 di data adalah',angka.count(3))
print('jumlah angka 10 di data adalah',angka.count(10))

# mengtahui posisi pada value yang kita cari

print('angka 3 berada di posisi berapa',angka.index(3))
# print('angka 100 berada di posisi berapa',angka.index(100)) # ini akan error karena tidak ada nilai 100

# cara menambahkan value pada data

angka.append(10) # ini akan
print(angka)





