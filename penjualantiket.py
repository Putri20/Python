nama = input("Nama Pembeli : ")

telp = input("No.Telp :")
tujuan = input("Jurusan [SBY/BL/LMP] :")

if tujuan == "SBY":
    kota= " Surabaya"
    harga= 300000

elif tujuan == "BL":
    kota= "Bali"
    harga= 500000

else:
    kota= "Lampung"
    harga= 500000

jumlah = input("Jumlah Tiket :")

if jumlah >= 3 :
    potongan=(jumlah*harga)*0.1

else:
    potongan=0

total = (jumlah*harga) - potongan


