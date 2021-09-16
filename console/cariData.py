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
    
# validasi NIM
while True:
    nim = input("NIM: ")
    if ut.PeriksaNIM(nim):
        break
    else:
        print("Format NIM tidak sesuai.")

# cari NIM dalam berkas
cariNIM = ut.PeriksaNIMKembar(nim, kamus, True) # set True jika ingin menampilkan data yang sudah ditemukan

if len(cariNIM) > 0:
    print(cariNIM)
else:
    print("Data tidak ditemukan.")
        