# tumple merupakan tipe data yang tidak dapat di ubah/pasti

'''
METHOD Pada di di tumple hanya 
-- index
-- count
--- len

kalian bisa kalian kunjungi di :
https://www.w3schools.com/python/python_tuples.asp
https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences

'''

# mengetahui panjang data
data=(10,30,29)
print('panjang data adalah:',len(data))


## trik penulisan untuk tuple
data_tuple=("Apple",)
print(type(data_tuple))
data_tuple=("Apple")
print(type(data_tuple))

## mengakses data pada tuple
data=(312,3162,3482,32,3,45,10,2,2,1,3,23)
print('value yang di dapatkan pada posisi 1:{}'.format(data[0]))
print('value yang di dapatkan pada posisi 3:{}'.format(data[2]))
tengah=len(data)//2
print('value yang di dapatkan pada tengah:{}'.format(data[tengah-1:tengah+1]))
print('value yang di dapatkan pada akhir:{}'.format(data[-1]))

## data yang di pakai
data=(312,3162,3482,32,3,45,10,2,2,1,3,23)
print('mendapakatkan data ke 2 sampai ke 6:',data[1:6])

## data yang di pakai



