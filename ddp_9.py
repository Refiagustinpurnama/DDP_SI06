print('\n---- celcius ke fahreinheit ----')
def celcius_ke_fahrenheit(celcius):
    print(celcius * 9/5 + 32)
celcius_ke_fahrenheit(0)

print('\n---- mencari bilangan genap ----')
def is_genap(genap):
    print(genap %2 == 0)
is_genap(4)
is_genap(7)

print('\n---- mencari keterangan lulus atau tidak ----')
# rata rata nilai kelulusan 70
def skor(nilai):
    if nilai >= 80:
        print("Lulus")
    else:
        print("Gagal")

skor(80)
skor(60)

print('\n---- menampilkan bilangan ganjil yg kurang ----')
def bilangan_ganjil(ganjil):
    for i in range(1,ganjil+1, 2):
        print(i, end=" ")
bilangan_ganjil(20)

