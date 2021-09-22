# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 21:44:03 2021

@author: galih-hermawan
"""

from libHobiMahasiswa import ManajemenBerkas, UtilitasFileKode, Utilitas
import re

ut = Utilitas()
utFK = UtilitasFileKode() 
delimiter = utFK.PemisahKolom()
lstFile, lstKolomKode = utFK.AmbilKodeDataFile()
lstPolaFile, lstKolomPola = utFK.AmbilKodePola()

# pola regex untuk menerima minimal 1 karakter apapun
polaUmum = "^.+$"

fMhs, fHobi, fMhsHobi = lstFile[0], lstFile[1], lstFile[2]

dataMhs = ManajemenBerkas(lstFile[0]).BacaBerkas()
dataHobi = ManajemenBerkas(lstFile[1]).BacaBerkas()
dataMhsHobi = ManajemenBerkas(lstFile[2]).BacaBerkas()
kamus = utFK.KamusFile_Kode(delimiter)

daftarKode = utFK.DaftarKolom(lstKolomKode, delimiter)
daftarPola = utFK.DaftarKolom(lstKolomPola, delimiter)
# pola kolom yang kosong diisi dengan pola umum
for dp in range(len(daftarPola)):
    daftarPola[dp] = [polaUmum if d=="" else d for i, d in enumerate(daftarPola[dp])]

polaMhs = daftarPola[0]
polaHobi = daftarPola[1]
polaMhsHobi = daftarPola[2]

# tampil menu
lstPil = []
j = 0
print("Data yang ingin ditambah:")
for i in range(len(lstFile)):
    j += 1
    lstPil.append(j)
    print(f"({j}) {lstFile[i]}.")

strPil = [str(x) for x in lstPil]
lstStrPil = "/".join(strPil)
pil = input(f"Tulis angka menu ({lstStrPil}) atau ketik apapun untuk keluar : ")

if pil.isdigit(): pil = int(pil)

# menu input data mahasiswa
if pil == 1:
    lstDataMasukan = []
    print("Masukkan data mahasiswa berikut.")
    for i, data in enumerate(daftarKode[0]):
        while True:
            dataMasukan = input(f"Data {data}: ")
            if re.match(polaMhs[i], dataMasukan):
                # khusus NIM, tidak boleh kembar
                NIM_Kembar = ut.CariData(dataMasukan, 0, dataMhs, delimiter, True, False)
                if NIM_Kembar:
                    print("NIM sudah terdaftar.")
                else:
                    lstDataMasukan.append(dataMasukan)
                    break
            else:
                print(f"Format {data} salah.")
    
    dataSimpan = delimiter.join(lstDataMasukan)
    while True:
        print("\n________ \nData mahasiswa baru:")
        print(dataSimpan)
        tanya = input("Yakin akan disimpan (y/t) : ")
        tanya = tanya.lower().strip()
        if tanya == "y":
            ManajemenBerkas(fMhs).TambahDataBerkas(dataSimpan)
            print("Data berhasil simpan.")
            break
        elif tanya == 't':
            break
        print('-----------------------------------------------')
# menu input data hobi
elif pil==2:
    lstDataMasukan = [None] * len(daftarKode[1]) # inisialisasi list ukuran hobi
    print("Masukkan data hobi berikut.")
    for i, data in enumerate(daftarKode[1]):
        while True:
            dataMasukan = input(f"Data {data}: ")
            if re.match(polaHobi[i], dataMasukan):
                # khusus kode hobi, tidak boleh kembar
                kodeHobi_Kembar = ut.CariData(dataMasukan, 0, dataHobi, delimiter, True, False)
                if kodeHobi_Kembar:
                    print("Kode hobi sudah terdaftar.")
                else:
                    # khusus pengecekan nama hobi kembar pada looping ke-2
                    if i == 1:
                        nmHobiBaruSudahAda = ut.CariData(dataMasukan, 1, dataHobi, delimiter)
                        if nmHobiBaruSudahAda:
                            print(f"Hobi '{dataMasukan}' sudah ada.")
                        else:
                            lstDataMasukan[1] = (dataMasukan)
                            break
                    else:
                        lstDataMasukan[0] = (dataMasukan)
                        break
            else:
                print(f"Format {data} salah.")
    
    dataSimpan = delimiter.join(lstDataMasukan)
    while True:
        print("\n________ \nData hobi baru:")
        print(dataSimpan)
        tanya = input("Yakin akan disimpan (y/t) : ")
        tanya = tanya.lower().strip()
        if tanya == "y":
            ManajemenBerkas(fHobi).TambahDataBerkas(dataSimpan)
            print("Data berhasil simpan.")
            break
        elif tanya == 't':
            break
        print('-----------------------------------------------')
# menu input data mhshobi
elif pil==3:
    lstDataMasukan = []
    iJawab =  ["tes"] * len(daftarKode[2]) # inisialisasi list ukuran mhshobi
    print("Masukkan data mhshobi berikut.")
    for i, data in enumerate(daftarKode[2]):
        while True:
            dataMasukan = input(f"Data {data}: ")
            iJawab[i] = dataMasukan
            if re.match(polaMhsHobi[i], dataMasukan):
                NIM_terdaftar = ut.CariData(iJawab[0], 0, dataMhs, delimiter, True, False) 
                kodeHobi_terdaftar = ut.CariData(iJawab[1], 0, dataHobi, delimiter, True, False)
                # khusus nim yang sama dengan kode hobi yang sama, jangan dimasukkan
                NIM_Kembar = ut.CariData(iJawab[0], 0, dataMhsHobi, delimiter, True, False)
                kodeHobi_Kembar = ut.CariData(iJawab[1], 1, dataMhsHobi, delimiter, True, False)
                #print(f"nim kembar: {NIM_Kembar} , kode hobi kembar: {kodeHobi_Kembar}")
                if not NIM_terdaftar:
                    print("NIM belum terdaftar di data mahasiswa.")
                # hanya dilakukan di looping kedua (pemeriksaan kode hobi)
                elif i==1 and not kodeHobi_terdaftar:
                    print("Kode hobi belum terdaftar di data hobi.")
                elif NIM_Kembar and kodeHobi_Kembar:
                    print("Kode hobi dengan nim yang sama sudah terdaftar.")
                else:
                    lstDataMasukan.append(dataMasukan)
                    break
            else:
                print(f"Format {data} salah.")
    
    dataSimpan = delimiter.join(lstDataMasukan)
    while True:
        print("________ \nData mhshobi baru:")
        print(dataSimpan)
        tanya = input("Yakin akan disimpan (y/t) : ")
        tanya = tanya.lower().strip()
        if tanya == "y":
            ManajemenBerkas(fMhsHobi).TambahDataBerkas(dataSimpan)
            print("Data berhasil simpan.")
            break
        elif tanya == 't':
            break
        print('-----------------------------------------------')
else:
    print("Keluar aplikasi.")

