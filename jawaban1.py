def kalimat(x):
    if len(x)>200:
        print('Batas Karakter Maksimal Hanya 200')
    elif len(x)==0:
        print('Masukkan Sebuah Inputan')
    else:
        text = '*{}*'
        print(text.format(x.upper().replace(' ','')))

x= input('Masukkan Sebuah Kalimat : ')
kalimat(x)
# ini adalah sebuah CONTOH