# -*- coding: utf-8 -*-
"""
Created on Sat Sep 18 22:25:06 2021

@author: galih-hermawan
"""

from objManajemenBerkas import ManajemenBerkas, Utilitas

ut = Utilitas() 
 
daftarFile = ["dataMahasiswa.txt", "dataHobi.txt", "dataMhsHobi.txt"]

while True:
    pilMenu = input("Menu menambah data: \n(1) mahasiswa, \n(2) hobi, \
                    \n(3) mahasiswa hobi, \
                    \n(0) keluar. \nTulis angka: ")
    
    if pilMenu in ["1", "2", "3"]:
        nmFile = daftarFile[int(pilMenu)-1]
        statusFile = ManajemenBerkas(nmFile).PeriksaBerkas()
        mb = ManajemenBerkas(nmFile)
        data = mb.BacaBerkas() # baca isi file
    
    if pilMenu == "1":
        if statusFile:
            file1 = open(nmFile, "a", encoding='utf-8')
            with file1:
                # validasi data baru
                nim, nama, kotaLahir, tglLahir, jk, \
                    kotaTinggal, tglTerdaftar, tinggi = ut.ValidasiDataMahasiswa(data)
                #nim, nama, jk = ut.ValidasiData(data)
                isi = [nim, nama, kotaLahir, tglLahir, jk.lower(), \
                       kotaTinggal, tglTerdaftar, tinggi]
                isi = "#".join(isi) # gabungkan isi list dengan tanda pemisah "#"
                file1.write("\n")
                file1.write(isi) 

            file1.close()    
            mb.RapikanBerkas()
        else:
            print("Berkas tidak terbaca.")
    elif pilMenu == "2":
        if statusFile:
            file1 = open(nmFile, "a", encoding='utf-8')
            with file1:
                # validasi data baru
                kodeHobi, namaHobi = ut.ValidasiDataHobi(data)
                isi = [kodeHobi, namaHobi]
                isi = "#".join(isi) # gabungkan isi list dengan tanda pemisah "#"
                file1.write("\n")
                file1.write(isi) 
                
            file1.close()    
            mb.RapikanBerkas()
        else:
            print("Berkas tidak terbaca.")
    elif pilMenu == "3":
        if statusFile:
            file1 = open(nmFile, "a", encoding='utf-8')
            with file1:
                # validasi data baru
                dataMhs = ManajemenBerkas(daftarFile[0]).BacaBerkas()
                dataHobi = ManajemenBerkas(daftarFile[1]).BacaBerkas()
                nim, kodeHobi = ut.ValidasiDataMhsHobi(data, dataMhs, dataHobi)
                isi = [nim, kodeHobi]
                isi = "#".join(isi) # gabungkan isi list dengan tanda pemisah "#"
                file1.write("\n")
                file1.write(isi) 
                
            file1.close()    
            mb.RapikanBerkas()
        else:
            print("Berkas tidak terbaca.")
    elif pilMenu == "0":
        print("Keluar aplikasi.")
        break
    else:
        print("Pilih angka sesuai yang tertulis pada menu.")
    
    
