# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 21:59:47 2021

@author: galih-hermawan
"""

from objManajemenBerkas import ManajemenBerkas, Utilitas

nmFile = "dataMahasiswa.txt"
statusFile = ManajemenBerkas(nmFile).PeriksaBerkas()
mb = ManajemenBerkas(nmFile)
data = mb.BacaBerkas() # baca isi file
ut = Utilitas() 

# merapikan isi file ke dalam list
kamus = []
for i in data:
    d = i.split("#")
    kamus.append(d)
    
if statusFile:
    file1 = open(nmFile, "a", encoding='utf-8')
    with file1:
        # validasi data baru
        nim, nama, jk = ut.ValidasiData(kamus)
        isi = [nim, nama, jk.lower()] # masukkan ketiga data dalam list
        isi = "#".join(isi) # gabungkan isi list dengan tanda pemisah "#"
        file1.write(isi) 
        file1.write("\n")
    file1.close()    
else:
    print("Berkas tidak terbaca.")