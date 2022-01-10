print("==============")
print("   NOMOR 1")
print("==============")
KapaRAM = int(input("Masukan Kapasitas RAM : "))
blok = int(input("Masukan Blok / Unit : "))

petaBit = (KapaRAM / blok)

print("==============")
print("Kapasitas Peta Bit adalah : %d kbps" % petaBit)