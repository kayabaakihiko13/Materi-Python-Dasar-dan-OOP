flowers=['mawar','melati','anggrek']
latin_name=['Rosa','Jasminum','Orchidaceae']
for flower in flowers:
    print('nama bunga:{}'.format(flower))

for latin,flower in (zip(latin_name,flowers)):
    print(f'nama bunga:{latin}',f' Latin {latin}')

# while loop

## tampilin angka dari 1 sampai 10

angka=1
while angka<11:
    print(angka)
    angka=angka+1
print('akhri dari program')

