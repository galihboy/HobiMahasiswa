# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 15:18:51 2021

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
print("Data yang ingin diperbarui:")
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
    pass
# menu update data hobi
elif pil==2:
    kodeCari = input("Masukkan kode hobi: ")
    barisHobiDitemukan = ut.CariData(kodeCari, 0, dataHobi, delimiter)
    if barisHobiDitemukan:
        nmHobiBaruSudahAda = False
        barisDataLama = ut.AmbilData(barisHobiDitemukan, dataHobi, delimiter)[0]
        nmHobiLama = ut.AmbilData(barisHobiDitemukan, dataHobi, delimiter, [1])[0]
        print("Kosongkan data jika ingin menggunakan data lama.")
        nmHobi = input(f"Data lama: '{nmHobiLama}', data baru: ")
        nmHobi.strip()
        if nmHobi:
            nmHobiBaru = nmHobi
            # cek apakah hobi baru sudah pernah ada di data hobi
            nmHobiBaruSudahAda = ut.CariData(nmHobiBaru, 1, dataHobi, delimiter)
        else:
            nmHobiBaru = nmHobiLama
        
        if nmHobiBaruSudahAda:
            print("Nama hobi baru sudah ada.")
        else:
            barisDataBaru = delimiter.join([kodeCari, nmHobiBaru])
            print(barisDataBaru)
            dataBaru = ut.UpdateData(barisDataLama, barisDataBaru, dataHobi)
            ManajemenBerkas(fHobi).TulisBerkas(dataBaru)
            print("Pembaruan data berhasil dilakukan.")
    else:
        print(f"Data kode hobi '{kodeCari}' tidak ditemukan.")
# menu update data mhshobi
elif pil==3:
    pass
else:
    print("Keluar aplikasi.")

