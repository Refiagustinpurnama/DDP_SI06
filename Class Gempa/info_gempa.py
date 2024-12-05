from Gempa import *

# Membuat objek Gempa dengan Lokasi dan Skala
gempa1 = Gempa("Banten", 1.2)
gempa2 = Gempa("Palu", 6.1)
gempa3 = Gempa("Cianjur", 5.6)
gempa4 = Gempa("Jayapura", 3.3)
gempa5 = Gempa("Garut", 4.0)

# Info gempa
print("\n ====== Gempa Bumi Info ======")
print()
gempa1.Dampak() # Memanggil method dampak()

# Info gempa
print()
gempa2.Dampak() # Memanggil method dampak()

# Info gempa
print()
gempa3.Dampak() # Memanggil method dampak()

# Info gempa
print()
gempa4.Dampak() # Memanggil method dampak()

# Info gempa
print()
gempa5.Dampak() # Memanggil method dampak()
