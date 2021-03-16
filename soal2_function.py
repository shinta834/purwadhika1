import math
def mean (angka):
    length = len (angka)
    total_sum = 0
    for i in range (length):
        total_sum += angka[i]
    average = total_sum*1.0/length
    return average
def varian (angka):
    length = len (angka)
    m = mean (angka)
    total_sum=0
    for i in range (length):
        total_sum += (angka[i]-m)**2
    varians = total_sum*1.0/(length-1)
    return varians
def stanDev (angka):
    v = varian (angka)
    return math.sqrt(v)

angka=[int (i) for i in input('Masukkan Angka : ').split(' ')]
a = mean (angka)
b = varian (angka)
c = stanDev (angka)
print(angka)
print('Rata-ratanya adalah',a)
print('Variansinya Adalah', b)
print('Standar Deviasinya Adalah',c)
