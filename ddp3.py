# 1. Buatlah program python untuk menuliskan profil pribadi (nama, nim, kelas, no telp, alamat) menggunakan variabel dan di cetak (print)
#Soal 1
nama = 'Refi Agustin Purnama'
nim = '0110124020'
rombel = 'SI06'
no_telp = '6285894541611'
alamat = 'Srengseng sawah, Kota Jakarta Selaran, Jagakarsa, DKI Jakarta'

print ('nama saya adalah:', nama)
print ('nim saya adalah:', nim)
print ('rombel saya adalah:', rombel)
print ('nomor telepon saya adalah:', no_telp)
print ('alamat saya adalah:', alamat)
print ('======================')


# 2. buat seperti no 1 tapi 1 nama teman kalian
#Soal 2
nama = 'Helma Hafiza Aulia'
nim = '0110124028'
rombel = 'SI05'
no_telp = '6281935163316'
alamat = 'Perumahan Bogor Raya Permai'

print ('nama teman saya adalah:', nama)
print ('nim teman saya adalah:', nim)
print ('rombel teman saya adalah:', rombel)
print ('nomor teman telepon saya adalah:', no_telp)
print ('alamat teman saya adalah:', alamat)
print ('======================')

# 3. Buat program python untuk mencari nilai berat bdan ideal
#Soal 3 Rumus = tb-110x15%
tb = int(input('masukan tinggi badan:'))
bb_ideal = (tb - 110) + ((tb - 100) *0.15)

print('berat badan ideal adalah :',bb_ideal)

# 4. Buat program python untuk mencari nilai konversi dari celcius ke fahreinthel
# rumus + (celcius *9/5) + 32s
# Menghitung Celcius Ke Fahrenheit
print()
print('===Suhu Celcius Ke Fahrenheit===')

# Input Perhitungan
celcius = int(input('Masukan Suhu Celcius: '))

# Proses Perhitungan
rumus_fahrenheit = int(celcius*9/5)+32

# Output Perhitungan
print(celcius, 'Celcius sama dengan', rumus_fahrenheit, 'Fahrenheit')




# Menghitung Luas Tabung
print("")
print("=====Luas Tabung======")

# Input Angka
phi = 3.14
jari2 = int(input('Masukan nilai jari-jari: '))
tinggi = int(input('Masukan nilai tinggi: '))

# Proses Perhitungan
luas_permukaan =  2*phi*jari2*(jari2+tinggi)
luas_alas = phi*jari2**2
luas_selimut = 2 * phi * jari2 * tinggi

# Output Perhitungan
print('Luas Permukaan Tabung Adalah: ', luas_permukaan)
print('Luas Alas Tabung Adalah: ', luas_alas)
print('Luas Selimut Tabung Adalah: ', luas_selimut)



# Menghitung Keliling Tabung
print()
print('===Keliling Tabung===')

# Input Angka
r = int(input("Masukan Jari-Jari: "))
tinggi = int(input("Masukan tinggi: "))
phi = 3.14

# Proses Perhitungan
rumus = 2*phi*r*tinggi

# Output Perhitungan
print('Keliling Tabung Adalah', rumus)
