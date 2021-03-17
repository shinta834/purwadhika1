def kata_terpanjang(kalimat):
    list_kata = kalimat.split()
    max_panjang_kata = len(list_kata[0])
    for i in list_kata:
        if len(i) > max_panjang_kata:
            max_panjang_kata = len(i)
            print ('Jumlah Karakter Terbanyak Adalah Sebesar',max_panjang_kata,'Karakter')
    for i in list_kata:
        if len(i) == max_panjang_kata:
            print ('Karakter Yang Berjumlah',max_panjang_kata,'Adalah',i)

                
kalimat = input('Masukkan Kalimat : ')
kata_terpanjang (kalimat)

# saya adalah abcdef