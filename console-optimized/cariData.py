# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 18:21:51 2021

@author: galih-hermawan
"""

from libHobiMahasiswa import ManajemenBerkas, UtilitasFileKode, Utilitas

ut = Utilitas()
utFK = UtilitasFileKode() 
delimiter = utFK.PemisahKolom()
lstFile, lstKolom = utFK.AmbilKodeDataFile()
fMhs, fHobi, fMhsHobi = lstFile[0], lstFile[1], lstFile[2]

dataMhs = ManajemenBerkas(lstFile[0]).BacaBerkas()
dataHobi = ManajemenBerkas(lstFile[1]).BacaBerkas()
dataMhsHobi = ManajemenBerkas(lstFile[2]).BacaBerkas()
kamus = utFK.KamusFile_Kode(delimiter)

while True:
    pilMenu = input("Menu Utama. Cari data: \n(1) mahasiswa, \n(2) hobi, \
                    \n(3) mahasiswa beserta hobi, \
                    \n(4) hobi beserta mahasiswa, \
                    \n(0) keluar. \nTulis angka: ")
    # cari mahasiswa
    if pilMenu == "1":
        kolomMhs = lstKolom[0]
        lstKolomMhs = utFK.AmbilKolom(kolomMhs, delimiter)
        
        while True:
            lstPil = []
            j = 0
            print("\nData yang ingin dicari:")
            for i in range(len(lstKolomMhs)):
                j += 1
                lstPil.append(j)
                print(f"({j}) {lstKolomMhs[i]}.")
            strPil = [str(x) for x in lstPil]
            lstStrPil = "/".join(strPil)
            
            pil = input(f"Tulis angka menu ({lstStrPil}) atau ketik apapun untuk keluar : ")
    
            if pil.isdigit(): pil = int(pil)
    
            if pil in lstPil:
                namaKolom = lstKolomMhs[pil-1]
                nomorIndeksKolom = ut.IndeksKolom(namaKolom, fMhs, kamus)
                dataCari = input(f"Masukkan {namaKolom} yang dicari: ")
                dataKetemu = ut.CariData(dataCari, nomorIndeksKolom, dataMhs, delimiter)
                dataLuaran = ut.AmbilData(dataKetemu, dataMhs, delimiter)
                if dataLuaran: 
                    print(dataLuaran)
                else:
                    print(f"Data mahasiswa dengan {namaKolom} '{dataCari}' tidak ditemukan.")
            else:
                print("Keluar dari menu mahasiswa.")
                break
            
            print("------------------------------------------------------------------")
        #print(lstKolomMhs)
    # cari hobi
    elif pilMenu == "2":
        kolomHobi = lstKolom[1]
        lstKolomHobi = utFK.AmbilKolom(kolomHobi, delimiter)
        
        while True:
            lstPil = []
            j = 0
            print("\nData yang ingin dicari:")
            for i in range(len(lstKolomHobi)):
                j += 1
                lstPil.append(j)
                print(f"({j}) {lstKolomHobi[i]}.")
            strPil = [str(x) for x in lstPil]
            lstStrPil = "/".join(strPil)
            
            pil = input(f"Tulis angka menu ({lstStrPil}) atau ketik apapun untuk keluar : ")
    
            if pil.isdigit(): pil = int(pil)
    
            if pil in lstPil:
                namaKolom = lstKolomHobi[pil-1]
                nomorIndeksKolom = ut.IndeksKolom(namaKolom, fHobi, kamus)
                dataCari = input(f"Masukkan {namaKolom} yang dicari: ")
                dataKetemu = ut.CariData(dataCari, nomorIndeksKolom, dataHobi, delimiter)
                dataLuaran = ut.AmbilData(dataKetemu, dataHobi, delimiter)
                if dataLuaran: 
                    print(dataLuaran)
                else:
                    print(f"Data hobi dengan {namaKolom} '{dataCari}' tidak ditemukan.")
            else:
                print("Keluar dari menu hobi.")
                break
            
            print("------------------------------------------------------------------")

    # cari mahasiswa beserta hobi
    elif pilMenu == "3":
        while True:
            nama = input("Nama yang dicari [kosongkan untuk keluar]: ")
            if nama.strip() == "": 
                print("Keluar menu pencarian mahasiswa hobi.")
                break
            namaKolom = "nama"
            namaKolomPK = "nim"
            nomorIndeksKolom = ut.IndeksKolom(namaKolom, fMhs, kamus)
            nomorIndeksKolomPK = ut.IndeksKolom(namaKolomPK, fMhs, kamus)
            daftarBarisMhs = ut.CariData(nama, nomorIndeksKolom, dataMhs, delimiter)
            kolomRelasi_Mhs_Hobi = "kode hobi" # atribut Foreign Key (sekutu) MhsHobi dan Hobi
            kolomOutput = ["kode hobi","nama hobi"] # data kolom yang ingin diperoleh
            
            if len(daftarBarisMhs) == 0:
                print(f"Data nama {nama} tidak ditemukan.")
            else:
                barisDataMhs = ut.AmbilData(daftarBarisMhs, dataMhs, delimiter,[nomorIndeksKolomPK, nomorIndeksKolom])
                lstMhsTanpaHobi = []
                j = 0 
                for iData in barisDataMhs:
                    iNim = iData.split(delimiter)[nomorIndeksKolomPK]
                    dataLuaran = ut.ListDataRelasi(iNim, namaKolomPK, \
                          kolomRelasi_Mhs_Hobi, kolomOutput, \
                          fMhsHobi, fHobi, kamus, delimiter)
                    if dataLuaran: 
                        j += 1
                        print(f"Mahasiswa {j}: {iData}.")
                        print(f"Memiliki hobi: {dataLuaran}")
                        print("-----------------------------------")
                    else:
                        lstMhsTanpaHobi.append(iData)
                if lstMhsTanpaHobi:
                    print("Berikut ini daftar mahasiswa yang ditemukan, tapi belum mencantumkan hobi.")
                    print(lstMhsTanpaHobi)
    # cari hobi beserta mahasiswa
    elif pilMenu == "4":        
        while True:
            nama = input("Nama hobi yang dicari [kosongkan untuk keluar]: ")
            if nama.strip() == "": 
                print("Keluar menu pencarian hobi mahasiswa.")
                break
            namaKolom = "nama hobi"
            namaKolomPK = "kode hobi"
            nomorIndeksKolom = ut.IndeksKolom(namaKolom, fHobi, kamus)
            nomorIndeksKolomPK = ut.IndeksKolom(namaKolomPK, fHobi, kamus)
            daftarBarisHobi = ut.CariData(nama, nomorIndeksKolom, dataHobi, delimiter)
            kolomRelasi_Mhs_Hobi = "nim" # atribut Foreign Key (sekutu) MhsHobi dan Mahasiswa
            kolomOutput = ["nim","nama"] # data kolom yang ingin diperoleh
            
            if len(daftarBarisHobi) == 0:
                print(f"Data hobi {nama} tidak ditemukan.")
            else:
                barisDataHobi = ut.AmbilData(daftarBarisHobi, dataHobi, delimiter,[nomorIndeksKolomPK, nomorIndeksKolom])
                lstHobiTanpaMhs = []
                j = 0 
                for iData in barisDataHobi:
                    iKode = iData.split(delimiter)[nomorIndeksKolomPK]
                    dataLuaran = ut.ListDataRelasi(iKode, namaKolomPK, \
                          kolomRelasi_Mhs_Hobi, kolomOutput, \
                          fMhsHobi, fMhs, kamus, delimiter)
                    if dataLuaran: 
                        j += 1
                        print(f"Hobi {j}: {iData}.")
                        print(f"Diminati oleh mahasiswa: {dataLuaran}")
                        print("-----------------------------------")
                    else:
                        lstHobiTanpaMhs.append(iData)
                if lstHobiTanpaMhs:
                    print("Berikut ini daftar hobi yang ditemukan, tapi belum ada peminatnya.")
                    print(lstHobiTanpaMhs)
    elif pilMenu == "0":
        break
    else:
        print("Pilih angka sesuai yang tertulis pada menu.")
    
    print("------------------------------------------------------------------")
