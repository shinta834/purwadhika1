def sort_ganjil_genap(angka):
    # Membuat list baru untuk memisahkan angka ganjil dan genap yang ada pada list
    angka_ganjil = []
    angka_genap = []
    hasil = []
    for i in angka:
        if i % 2 != 0:
            angka_ganjil.append(i)
        else:
            angka_genap.append(i)
    # Sort angka ganjil
    for i in range(len(angka_ganjil)):
        for j in range(i+1, len(angka_ganjil)):
            if angka_ganjil[i] > angka_ganjil[j]:
                angka_ganjil[i], angka_ganjil[j] = angka_ganjil[j], angka_ganjil[i]
    hasil.append(angka_ganjil)
    # Sort angka genap
    for i in range(len(angka_genap)):
        for j in range(i+1, len(angka_genap)):
            if angka_genap[i] < angka_genap[j]:
                angka_genap[i], angka_genap[j] = angka_genap[j], angka_genap[i]
    hasil.append(angka_genap)
    hasil = angka_ganjil+angka_genap
    print (hasil)
   

sort_ganjil_genap([1,3,2,2,1,5,1,24,12,124,12,21,32,15])
