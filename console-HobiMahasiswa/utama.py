# -*- coding: utf-8 -*-
"""
Created on Sat Sep 18 21:13:45 2021

@author: galih-hermawan
"""

while True:
    print("Aplikasi Pengelolaan Data Hobi Mahasiswa.")
    pilM = input("[l] lihat, [c] cari, [x] keluar : ") 
    pilM = pilM.lower().strip()
    if pilM == "l":
        exec(open('lihatData.py').read())
    elif pilM == "c":
        exec(open('cariData.py').read())
    elif pilM == "x":
        break
    else:
        print("Pilih sesuai menu tersedia.")