# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 21:17:37 2021

@author: galih-hermawan
"""

from objManajemenBerkas import ManajemenBerkas

nmFile = "dataMahasiswa.txt"
statusFile = ManajemenBerkas(nmFile).PeriksaBerkas()
#print(statusFile)

if statusFile:
    file1 = open(nmFile, "r", encoding='utf-8')
    with file1:
        # pisah data file per baris dan hapus data kosong
        isi = file1.read().strip().split("\n")

    file1.close()    
    print(isi)
else:
    print("Berkas tidak terbaca.")