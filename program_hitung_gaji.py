print ("========PROGRAM HITUNG GAJI KARYAWAN KONTRAK PT. DINGIN DAMAI==========")

nama =input("Nama                           :")
gol = input("Golongan[1/2/3]                :")
pen = input("Pendidikan[S1/D3/D1/SMA]       :")
jam = int(input("Jumlah Jam Kerja               :"))

#Golongan Jabatan
if gol == "1":
    golongan=0.05*300000                    #golongan 1 sebesar 5% (15.000)

elif gol =="2":
    golongan = 0.1*300000                   #golongan 2 sebesar 10%(30.000)

elif gol =="3":
    golongan = 0.15*300000                  #golongan 3 sebesar 15%(45.000)

else:
    print("=====================")
    print("Golongan Jabatan tidak sesuai ")

#pendidikan
if pen == "S1"  :
    tunjangan= 0.3*300000                   #S1 sebesar 30%(90.000)

elif pen =="D3" :
    tunjangan= 0.2*300000                   #D3 sebesar 20%(60.000)

elif pen =="D1" :
    tunjangan= 0.05*300000                  #D1 sebesar 5%(15.000)

elif pen == "SMA" :
    tunjangan= 0.025*300000                 #SMA sebesar 2.5%(7.500)

else:
    print("=============================")
    print("tunjangan pendidikan kosong")

#honor lembur
if jam < 8   :
    lembur = 0 * 3500

elif jam > 8 :
    lembur= jam * 3500

else:
    lembur=0*3500

#total Gaji
Gajipokok=300000
Gaji=Gajipokok+golongan+tunjangan+lembur

print ("=========================================")
print ("Nama Karyawan : " , (nama))
print ("=======Honor yang di terima==============")
print ("Tunjangan jabatan       : Rp.", (golongan))
print ("Tunjangan pendidikan    : Rp.", (tunjangan))
print ("Honor Lembur            : Rp.", (lembur))
print ("Gaji pokok              : Rp.", (Gajipokok))
print ("----------------------------------------+")
print ("Total Gaji              : Rp." , (Gaji))

