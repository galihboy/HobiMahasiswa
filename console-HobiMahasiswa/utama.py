# -*- coding: utf-8 -*-
"""
Created on Sat Sep 18 21:13:45 2021

@author: galih-hermawan
"""

from objManajemenBerkas import ManajemenBerkas as mb

while True:
    print("\nAplikasi Pengelolaan Data Hobi Mahasiswa.")
    pilM = input("\n[l] Lihat Data, \n[c] Cari Data, \
                  \n[t] Tambah Data, \n[r] Rapikan berkas, \
                  \n[x] Keluar : ") 
    pilM = pilM.lower().strip()
    if pilM == "l":
        exec(open('lihatData.py').read())
    elif pilM == "c":
        exec(open('cariData.py').read())
    elif pilM == "t":
        exec(open('tambahData.py').read())
    elif pilM == "r":
        mb("dataHobi.txt").RapikanBerkas()
        mb("dataMahasiswa.txt").RapikanBerkas()
        mb("dataMhsHobi.txt").RapikanBerkas()
    elif pilM == "x":
        break
    else:
        print("Pilih sesuai menu tersedia.")