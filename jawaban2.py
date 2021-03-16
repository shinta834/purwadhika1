def nomorHp (x):
    if len(x) > 13 :
        print ('Nomor HP hanya maksimal 13 Angka')
    elif (x[0] != str(0)) and (x[1] != str(8)):
        print ('Nomor HP harus dimulai dengan "08"')
    else :
        print ('Nomor HP Saya Adalah ',x)

x = input('Masukkan Nomor HP : ')
nomorHp(x)
# 13467812436782
# 1324213513
# 085340984234
