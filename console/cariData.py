# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 22:49:56 2021

@author: galih-hermawan
"""

from objManajemenBerkas import ManajemenBerkas, Utilitas

nmFile = "dataMahasiswa.txt"

mb = ManajemenBerkas(nmFile)
data = mb.BacaBerkas() # baca isi file
ut = Utilitas() 

# merapikan isi file ke dalam list
kamus = []
for i in data:
    d = i.split("#")
    kamus.append(d)
    
while True:
    pilihan = input ("Cari berdasarkan nama atau nim ? ")
    pilihan = pilihan.lower().strip()
    dataCari = []
    
    if pilihan == "nim":
        nim = input("NIM yang dicari: ")
        # validasi NIM
        if ut.PeriksaNIM(nim):
            # cari NIM dalam berkas
            # set True jika ingin menampilkan data yang sudah ditemukan
            dataCari = ut.PeriksaNIMKembar(nim, kamus, True) 
            break
        else:
            print("Format NIM tidak sesuai.")
    elif pilihan == "nama":
        nama = input("Nama yang dicari: ")
        # method cari nama dan ambil hasilnya dalam list
        dataCari = ut.CariNama(nama, kamus)
        break
    else:
        print("Masukkan salah satu dari 'nim' atau 'nama'.")

if len(dataCari) > 0:
    # tampilkan data hasil pencarian jika ada
    print(dataCari)
else:
    print("Data tidak ditemukan.")
        