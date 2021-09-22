# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 22:19:35 2021

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
print("Data yang ingin dihapus:")
for i in range(len(lstFile)):
    j += 1
    lstPil.append(j)
    print(f"({j}) {lstFile[i]}.")

strPil = [str(x) for x in lstPil]
lstStrPil = "/".join(strPil)
pil = input(f"Tulis angka menu ({lstStrPil}) atau ketik apapun untuk keluar : ")

if pil.isdigit(): pil = int(pil)

# menu hapus data mahasiswa
if pil == 1:
    kodeCari = input("Masukkan NIM1: ")
    barisMhsDitemukan = ut.CariData(kodeCari, 0, dataMhs, delimiter, True)
    if barisMhsDitemukan:
        nimFK = ut.CariData(kodeCari, 0, dataMhsHobi, delimiter, True)
        # mencegah menghapus nim (mhs) yang menjadi FK di data Mhshobi
        if nimFK:
            print(f"NIM '{kodeCari}' sedang bertamu di data MhsHobi, tidak bisa dihapus.")
        else:
            barisDataLama = ut.AmbilData(barisMhsDitemukan, dataMhs, delimiter)[0]
            tanya = input(f"Yakin akan menghapus data '{barisDataLama}' ? (y/t) = ")
            if tanya.lower().strip() == "y":
                dataBaru = ut.HapusData(barisDataLama, dataMhs)
                #print(dataBaru)
                ManajemenBerkas(fMhs).TulisBerkas(dataBaru)
                print("Penghapusan data berhasil dilakukan.")
            else:
                print("Penghapusan data dibatalkan.")
    else:
        print(f"Data kode hobi '{kodeCari}' tidak ditemukan.")
# menu hapus data hobi
elif pil==2:
    kodeCari = input("Masukkan kode hobi: ")
    barisHobiDitemukan = ut.CariData(kodeCari, 0, dataHobi, delimiter, True)
    if barisHobiDitemukan:
        kodeHobiFK = ut.CariData(kodeCari, 1, dataMhsHobi, delimiter, True)
        # mencegah menghapus kode hobi yang menjadi FK di data Mhshobi
        if kodeHobiFK:
            print(f"Kode hobi '{kodeCari}' sedang bertamu di data MhsHobi, tidak bisa dihapus.")
        else:
            barisDataLama = ut.AmbilData(barisHobiDitemukan, dataHobi, delimiter)[0]
            tanya = input(f"Yakin akan menghapus data '{barisDataLama}' ? (y/t) = ")
            if tanya.lower().strip() == "y":
                dataBaru = ut.HapusData(barisDataLama, dataHobi)
                #print(dataBaru)
                ManajemenBerkas(fHobi).TulisBerkas(dataBaru)
                print("Penghapusan data berhasil dilakukan.")
            else:
                print("Penghapusan data dibatalkan.")
    else:
        print(f"Data kode hobi '{kodeCari}' tidak ditemukan.")
# menu hapus data mhshobi
elif pil==3:
    pass
else:
    print("Keluar aplikasi.")