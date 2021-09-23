# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 22:19:35 2021

@author: galih-hermawan
"""


from libHobiMahasiswa import ManajemenBerkas, UtilitasFileKode, Utilitas

ut = Utilitas()
utFK = UtilitasFileKode() 
delimiter = utFK.PemisahKolom()
lstFile, lstKolomKode = utFK.AmbilKodeDataFile()

fMhs, fHobi, fMhsHobi = lstFile[0], lstFile[1], lstFile[2]

dataMhs = ManajemenBerkas(lstFile[0]).BacaBerkas()
dataHobi = ManajemenBerkas(lstFile[1]).BacaBerkas()
dataMhsHobi = ManajemenBerkas(lstFile[2]).BacaBerkas()
kamus = utFK.KamusFile_Kode(delimiter)

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
    kodeCari = input("Masukkan NIM: ")
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
        print(f"Data nim '{kodeCari}' tidak ditemukan.")
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
    kodeCari = input("Masukkan NIM: ")
    barisMhsDitemukan = ut.CariData(kodeCari, 0, dataMhsHobi, delimiter, True)
    if barisMhsDitemukan:
        lstMhsHobi = ut.AmbilData(barisMhsDitemukan, dataMhsHobi, delimiter)
        lstKodeHobi = ut.AmbilData(barisMhsDitemukan, dataMhsHobi, delimiter,[1])
        print(f"Kode hobi yang sedang diminati adalah : {lstKodeHobi}")
        while True:
            pilKodeHobi = input("Masukkan kode hobi yang akan dihapus: ")
            pilKetemu = ut.CariData(pilKodeHobi, 1, lstMhsHobi, delimiter, True)
            if pilKetemu:
                dataHapus = delimiter.join([kodeCari, pilKodeHobi])
                tanya = input(f"Data yang akan dihapus '{dataHapus}'. Lanjut dihapus (y/t) ? ")
                if tanya.lower().strip() == "y":
                    dataBaru = ut.HapusData(dataHapus, dataMhsHobi)
                    #print(dataBaru)
                    ManajemenBerkas(fMhsHobi).TulisBerkas(dataBaru)
                    print("Penghapusan data berhasil dilakukan.")
                    break
                else:
                    print("Penghapusan dibatalkan.")
                    break
            else:
                print(f"Kode hobi '{pilKodeHobi}' untuk nim '{kodeCari}' tidak ditemukan di data MhsHobi.")
                
       # barisDataLama = ut.AmbilData(barisMhsDitemukan, dataMhsHobi, delimiter)
       # tanya = input(f"Yakin akan menghapus data '{barisDataLama}' ? (y/t) = ")
       # if tanya.lower().strip() == "y":
       #     dataBaru = ut.HapusData(barisDataLama, dataMhsHobi)
       #     print(dataBaru)
            #ManajemenBerkas(fMhsHobi).TulisBerkas(dataBaru)
       #     print("Penghapusan data berhasil dilakukan.")
       # else:
       #     print("Penghapusan data dibatalkan.")
    else:
        print(f"Data nim '{kodeCari}' tidak ditemukan.")
else:
    print("Keluar aplikasi.")