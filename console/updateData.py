# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 17:05:02 2021

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
    nimCari = input("NIM yang akan diperbaharui: ")
    if ut.PeriksaNIM(nimCari):
        # cari NIM dalam berkas
        # set True jika ingin menampilkan data yang sudah ditemukan
        dataCari = ut.PeriksaNIMKembar(nimCari, kamus, True) 
        break
    else:
        print("Format NIM tidak sesuai.")
        
if len(dataCari) > 0:
    # tampilkan data hasil pencarian jika ada
    print(f"Data ditemukan: {dataCari}")
    # validasi data
    nim, nama, jk = ut.ValidasiDataUpdate(kamus)
    nimBaru = dataCari[0] if nim == "-" else nim
    namaBaru = dataCari[1] if nama == "-" else nama
    jkBaru = dataCari[2] if jk == "-" else jk
    # baris data baru
    dataUpdate = "#".join([nimBaru, namaBaru, jkBaru])
    
    while True:
        pil = input("Yakin akan di-update (y/t)? ")
        pil = pil.lower().strip()
        if pil in ["y", "t"]:
            break
        else:
            print("Ketik 'y' untuk update, atau 't' untuk membatalkan.")
            
    if pil == "y":
        dataBaru = ut.UpdateData(nimCari, kamus, dataUpdate) # data baru setelah update
        #print(f"Data terbaru: {dataBaru}")
        mb.TulisBerkas(dataBaru) # update berkas dengan data terbaru
        print("Data dan berkas berhasil diperbarui.")
    else:
        print("Data batal dihapus.")
else:
    print("Data tidak ditemukan.")