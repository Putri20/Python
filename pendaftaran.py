nama = input("Masukan Nama  :")
nis =  input("Masukan NIS :")
jurusan = input("Masukan Jurusan [SI / SIA]:")

if jurusan == "SI"  :
    nama_prodi = " Sistem Informasi"
    harga= 2400000

else:
    jurusan == "SIA" 
    nama_prodi = " Sistem Informasi Akuntasi"
    harga= 2000000

print ("============Pendaftaran Mahasiswa Baru===========")
print  ("Nama: "+str(nama))
print  ("Nis: "+str(nis))
print  ("Prodi: "+str(nama_prodi))
print  ("Biaya: "+str(harga))
