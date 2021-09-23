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

# menu update data mahasiswa
if pil == 1:
    lstDataMasukan = []
    kodeCari = input("Masukkan nim: ")
    barisMhsDitemukan = ut.CariData(kodeCari, 0, dataMhs, delimiter, True)
    if barisMhsDitemukan:
        lstDataMasukan.append(kodeCari)
        barisDataLama = ut.AmbilData(barisMhsDitemukan, dataMhs, delimiter)[0]
        print("Kosongkan data jika akan menggunakan data lama.")
        for i in range(1,len(daftarKode[0])):
            nmKolom = daftarKode[0][i]
            dataKolom = dataMhsDitemukan = ut.AmbilData(barisMhsDitemukan, dataMhs, delimiter, [i])
            while True:    
                dataMasukan = input(f"Data {nmKolom} lama '{dataKolom[0]}', data baru: ")            
                if dataMasukan.strip():
                    if re.match(polaMhs[i], dataMasukan):
                        dataKolomBaru = dataMasukan
                        break
                    else:
                        print(f"Format '{nmKolom}' tidak sesuai.")
                else:
                    dataKolomBaru = dataKolom[0]
                    break
            lstDataMasukan.append(dataKolomBaru)
        #print("Data baru: ",lstDataMasukan)
        barisDataBaru = delimiter.join(lstDataMasukan)
        #print(barisDataBaru)
        dataBaru = ut.UpdateData(barisDataLama, barisDataBaru, dataMhs)
        #print(dataBaru)
        ManajemenBerkas(fMhs).TulisBerkas(dataBaru)
        print("Pembaruan data berhasil dilakukan.")
    else:
        print(f"Data nim '{kodeCari}' tidak ditemukan.")

# menu update data hobi
elif pil==2:
    kodeCari = input("Masukkan kode hobi: ")
    barisHobiDitemukan = ut.CariData(kodeCari, 0, dataHobi, delimiter, True)
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
            nmHobiBaruSudahAda = ut.CariData(nmHobiBaru, 1, dataHobi, delimiter, True)
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
    kodeCari = input("Masukkan nim: ")
    barisMhsDitemukan = ut.CariData(kodeCari, 0, dataMhsHobi, delimiter, True)
    if barisMhsDitemukan:
        nmHobiBaruSudahAda = False
        # jml hobi mungkin lebih dari satu
        barisDataLama = ut.AmbilData(barisMhsDitemukan, dataMhsHobi, delimiter)
        kodeHobiLama = ut.AmbilData(barisMhsDitemukan, dataMhsHobi, delimiter, [1])
        lstKodeHobiBaru = []
        print(f"Kode hobi lama: {kodeHobiLama}")
        print("Kosongkan data jika ingin menggunakan data lama.")
        for i, data in enumerate(kodeHobiLama):
            while True:
                kodeHobi = input(f"Data lama {i+1}: '{kodeHobiLama[i]}', data baru: ")
                kodeHobi.strip()
                # periksa apakah kodehobi terdaftar di data Hobi
                kodeHobiTerdaftar = ut.CariData(kodeHobi, 0, dataHobi, delimiter, True)
                if not kodeHobi: #kodehobi dikosongkan, menyimpan data lama
                    lstKodeHobiBaru.append(data)
                    break
                elif not kodeHobiTerdaftar:
                    print(f"Kode hobi {kodeHobi} belum terdaftar di data Hobi.")
                elif kodeHobi in kodeHobiLama and kodeHobi != data:
                    print(f"Kode hobi {kodeHobi} sudah pernah disimpan.")
                else:
                    lstKodeHobiBaru.append(kodeHobi)
                    break
           
        barisDataBaru = [delimiter.join([kodeCari,i] )for i in lstKodeHobiBaru]   
        
        print("Data baru: ",barisDataBaru)
        dataBaru = ut.UpdateData(barisDataLama, barisDataBaru, dataMhsHobi)
        #print(dataBaru)
        ManajemenBerkas(fMhsHobi).TulisBerkas(dataBaru)
        print("Pembaruan data berhasil dilakukan.")
    else:
        print(f"Data kode hobi '{kodeCari}' tidak ditemukan.")
else:
    print("Keluar aplikasi.")

