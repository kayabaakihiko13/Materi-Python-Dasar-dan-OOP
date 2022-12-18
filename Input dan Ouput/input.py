# input data user
data=input('Masukan nama Anda:')
print('selamat datang:',data)
print('tipe data:',data)

# ini cara untuk melakuan input pada data yang berupa angka

## angka integer
angka_int=int(input('masukan angka interger:'))
print('angka =',angka_int,'tipe data:',type(angka_int))

## angka desimal
angka_desimal=float(input('masukan angka desimal:'))
print('angka =',angka_desimal,'tipe data:',type(angka_desimal))

## boolean
'''
Noted: Cukup Triky
'''

data=bool(input('masukan apa aja:'))
print(data)

data_biner=bool(int(input('masukan int:')))
print(data_biner)






