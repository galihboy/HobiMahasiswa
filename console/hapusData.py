# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 16:09:14 2021

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
    dataCari = []
    nim = input("NIM yang akan dihapus: ")
    if ut.PeriksaNIM(nim):
        # cari NIM dalam berkas
        # set True jika ingin menampilkan data yang sudah ditemukan
        dataCari = ut.PeriksaNIMKembar(nim, kamus, True) 
        break
    else:
        print("Format NIM tidak sesuai.")


if len(dataCari) > 0:
    # tampilkan data hasil pencarian jika ada
    print(f"Data ditemukan: {dataCari}")
    while True:
        pil = input("Yakin akan dihapus (y/t)? ")
        pil = pil.lower().strip()
        if pil in ["y", "t"]:
            break
        else:
            print("Ketik 'y' untuk menghapus, atau 't' untuk membatalkan.")
            
    if pil == "y":
        dataBaru = ut.HapusData(nim, kamus) # data baru setelah penghapusan
        #print(f"Data terbaru: {dataBaru}")
        mb.TulisBerkas(dataBaru) # update berkas dengan data terbaru
        print("Data berhasil dihapus dan berkas sudah diperbarui.")
    else:
        print("Data batal dihapus.")
else:
    print("Data tidak ditemukan.")