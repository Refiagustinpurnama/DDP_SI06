#soal 1

angka = int(input("masukan bilangan bulat: "))
ganjil = "bilangan ganjil"
genap = "bilangan genap"

if angka % 2 == 0:
    print(genap)
elif angka % 2 != 0:
    print(ganjil)
else :
    print("input tidak valid")

print("=========================")

#soal 2

nilai_ujian = int(input("masukan nilai ujian: "))

if nilai_ujian >= 75:
  print(" Selamat Lulus")
else :
  print("Tidak Lulus, Coba lagi taun depan")

  #soal 3

usia = int(input("masukan usia anda: "))

if usia >= 18:
   print("Anda sudah dewasa")
elif usia >= 13 and usia <= 17:
   print("Anda masih remaja")
else :
   print("Anda masih anak-anak")

   #soal 4

status_anggota = input("Masukan status keanggotaan anda: ")
if status_anggota == "gold" or status_anggota == "silver":
   print("Selamat anda mendapatkan diskon")
else :
   print("Maaf anda tidak mendapatkan diskon, coba lagi..")

   #soal 5

jumlah_pembelian = int(input("Masukan jumlah pembelian:"))
harga_item = 1000
harga_diskon = harga_item * jumlah_pembelian *(10/100)
harga_total = harga_item * jumlah_pembelian
total = harga_total - harga_diskon

print(f"Anda mendapatkan diskon 10%, harga per item {harga_item} jadi total yang harus dibayar {total}") if jumlah_pembelian > 100 else print(f"harga per item {harga_item}, jadi total yang harus dibayar adalah {harga_total}")