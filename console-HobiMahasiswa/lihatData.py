# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 21:17:37 2021

@author: galih-hermawan
"""

from objManajemenBerkas import ManajemenBerkas

daftarFile = ["dataMahasiswa.txt", "dataHobi.txt", "dataMhsHobi.txt"]

pil = input("Data yang ingin dilihat (1) mahasiswa, (2) hobi, (3) mhshobi, (4) semua. \nTulis angka: ")

if pil in ["1", "2", "3"]:
    nmFile = daftarFile[int(pil)-1]
    mb = ManajemenBerkas(nmFile) 
    data = mb.BacaBerkas()
    print(f"Isi file: {nmFile}")
    print(data)
elif pil == "4":
    for nmFile in daftarFile:
        mb = ManajemenBerkas(nmFile) 
        data = mb.BacaBerkas()
        print(f"\n Isi file: {nmFile}")
        print(data)
else:
    print("Keluar aplikasi.")
