# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 17:21:48 2021

@author: galih-hermawan
"""

from libHobiMahasiswa import ManajemenBerkas, UtilitasFileKode

utFK = UtilitasFileKode() 
lstFile, lstKolom = utFK.AmbilKodeDataFile()
lstPil = []
j = 0

print("Data yang ingin dilihat:")
for i in range(len(lstFile)):
    j += 1
    lstPil.append(j)
    print(f"({j}) {lstFile[i]}.")
print(f"({j+1}) Semua data.")
lstPil.append(j+1)
strPil = [str(x) for x in lstPil]
lstStrPil = "/".join(strPil)
pil = input(f"Tulis angka menu ({lstStrPil}) atau ketik apapun untuk keluar : ")

if pil.isdigit(): pil = int(pil)

if pil in lstPil[0:len(lstPil)-1]:
    nmFile = lstFile[pil-1]
    mb = ManajemenBerkas(nmFile) 
    data = mb.BacaBerkas()
    print(f"Isi file: {nmFile}")
    print(data)
elif pil == lstPil[-1]:
    for nmFile in lstFile:
        mb = ManajemenBerkas(nmFile) 
        data = mb.BacaBerkas()
        print(f"\n Isi file: {nmFile}")
        print(data)
else:
    print("Keluar aplikasi.")