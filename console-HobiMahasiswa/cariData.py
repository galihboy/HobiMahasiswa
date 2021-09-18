# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 22:49:56 2021

@author: galih-hermawan
"""

from objManajemenBerkas import ManajemenBerkas, Utilitas

def TampilData(dataCari, data):
    if len(dataCari) > 0:
        # tampilkan data hasil pencarian jika ada
        #print(dataCari)
        dataOutput = ut.LihatDataCari(data, dataCari)
        print(dataOutput)
    else:
        print("Data tidak ditemukan.")

ut = Utilitas() 
daftarFile = ["dataMahasiswa.txt", "dataHobi.txt", "dataMhsHobi.txt"]



menu = 1
while True:
    pilMenu = input("Cari data: \n(1) mahasiswa, \n(2) hobi, \
                    \n(3) mahasiswa beserta hobi, \
                    \n(4) hobi beserta mahasiswa, \
                    \n(0) keluar. \nTulis angka: ")
    if pilMenu == "1":
        mb = ManajemenBerkas(daftarFile[0])
        data = mb.BacaBerkas() # baca isi file
        while True:
            pilihan = input ("Ketik angka untuk cari data: \n[1] nim \n[2] nama \
                             \n[3] tempat lahir \n[4] tanggal lahir \
                            \n[5] jenis kelamin \
                            \n[6] tempat tinggal \n[7] tanggal terdaftar \
                            \n[8] tinggi badan \n[0] untuk keluar. \
                             \nNomor pilihan: ")
            pilihan = pilihan.lower().strip()
            dataCari = []
            
            if pilihan == "1":
                nim = input("NIM yang dicari: ")
                # validasi NIM
                if ut.PeriksaNIM(nim):
                    # cari NIM dalam berkas
                    # set True jika ingin menampilkan data yang sudah ditemukan
                    #dataCari = ut.CariNIM(nim, data)
                    dataCari = ut.CariData(nim, 0, data, True) #True untuk pencarian tepat
                    TampilData(dataCari, data)
                else:
                    print("Format NIM tidak sesuai.")
            elif pilihan == "2":
                nama = input("Nama yang dicari: ")
                # method cari nama dan ambil hasilnya dalam list
                #dataCari = ut.CariNamaBaru(nama, data)
                dataCari = ut.CariData(nama, 1, data) # kolom nomor 1: nama
                TampilData(dataCari, data)
            elif pilihan == "3":
                kota1 = input("Kota tempat lahir: ")
                # method cari kota tempat lahir dan ambil hasilnya dalam list
                dataCari = ut.CariData(kota1, 2, data) # kolom nomor 2: kota tempat lahir
                TampilData(dataCari, data)      
            elif pilihan == "4":
                ttl = input("Tanggal lahir: ")
                # method cari tanggal lahir dan ambil hasilnya dalam list
                dataCari = ut.CariData(ttl, 3, data) # kolom nomor 3: tanggal lahir
                TampilData(dataCari, data)
            elif pilihan == "5":
                jk = input("Jenis kelamin (l/p): ")
                # method cari tempat tinggal dan ambil hasilnya dalam list
                dataCari = ut.CariData(jk, 4, data, True)
                TampilData(dataCari, data)     
            elif pilihan == "6":
                kota2 = input("Kota tempat tinggal: ")
                # method cari tempat tinggal dan ambil hasilnya dalam list
                dataCari = ut.CariData(kota2, 5, data)
                TampilData(dataCari, data) 
            elif pilihan == "7":
                ttl = input("Tanggal terdaftar: ")
                # method cari tanggal terdaftar dan ambil hasilnya dalam list
                dataCari = ut.CariData(ttl, 6, data)
                TampilData(dataCari, data)
            elif pilihan == "8":
                tinggi = input("Tinggi badan: ")
                # method cari tanggal terdaftar dan ambil hasilnya dalam list
                dataCari = ut.CariData(tinggi, 7, data, True)
                TampilData(dataCari, data)
            elif pilihan =="0":
                break
            else:
                print("Masukkan nomor pilihan yang tersedia.")
    elif pilMenu == "2":
        mb = ManajemenBerkas(daftarFile[1])
        data = mb.BacaBerkas() # baca isi file
        namaHobi = input("Nama hobi yang dicari: ")
        # method cari nama hobi dan ambil hasilnya dalam list
        dataCari = ut.CariData(namaHobi, 1, data)
        TampilData(dataCari, data)
    elif pilMenu == "3":        
        dataMhs = ManajemenBerkas(daftarFile[0]).BacaBerkas()
        dataHobi = ManajemenBerkas(daftarFile[1]).BacaBerkas()
        dataMhsHobi = ManajemenBerkas(daftarFile[2]).BacaBerkas()
        nama = input("Nama yang dicari: ")
        # method cari nama dan ambil hasilnya dalam list
        dataCari = ut.CariData(nama, 1, dataMhs) # kolom nomor 1: nama
        if len(dataCari) != 0:
            # list mahasiswa
            daftarMhsCari = ut.LihatDataCari(dataMhs, dataCari)
            # list nim saja
            daftarNIM = [x.split("#")[0] for i,x in enumerate(daftarMhsCari)]
            outMhshobi = []
            mhsTanpaHobi = []
            # list kode hobi berdasarkan nim
            for iNIM in daftarNIM:
                idxKodeHobi = ut.CariData(iNIM, 0, dataMhsHobi)
                if len(idxKodeHobi) == 0:
                    # daftar mhs tanpa hobi
                    mhsTanpaHobi.append(iNIM)
                else:
                    # daftar mahasiswa yang memiliki hobi
                    outMhshobi.append(ut.LihatDataCari(dataMhsHobi, idxKodeHobi))
            # list kode hobi untuk nim yang terdaftar (memiliki hobi)
            if len(outMhshobi) != 0:
                for i, iMhsHobi in enumerate(outMhshobi):
                    if len(iMhsHobi)>0:
                        oNIM = iMhsHobi[0].split("#")[0]
                        oNama = dataMhs[ut.CariData(oNIM, 0, dataMhs, True)[0]].split("#")[1]
                        print(f"\nMahasiswa {i+1}: {oNIM} {oNama}, memiliki hobi:")
                        for h in iMhsHobi:
                            oKodeHobi = h.split("#")[1]
                            daftarHobi = dataHobi[ut.CariData(oKodeHobi, 0, dataHobi, True)[0]].split("#")[1]
                            print(oKodeHobi, daftarHobi)

            # daftar mahasiswa yang dicari ada, tapi tidak punya hobi
            if len(mhsTanpaHobi)>0:
                print("\nMahasiswa ditemukan namun tidak punya hobi:")
                for iMhs in mhsTanpaHobi:
                    for allMhsCari in daftarMhsCari:
                        if allMhsCari.find(iMhs) == 0:
                            oNIM = allMhsCari.split("#")[0]
                            oNama = allMhsCari.split("#")[1]
                            print(oNIM, oNama)
 
        else:
            print(f"Mahasiswa dengan nama '{nama}' tidak ditemukan.")
    elif pilMenu == "4":        
        dataMhs = ManajemenBerkas(daftarFile[0]).BacaBerkas()
        dataHobi = ManajemenBerkas(daftarFile[1]).BacaBerkas()
        dataMhsHobi = ManajemenBerkas(daftarFile[2]).BacaBerkas()
        nama = input("Nama hobi yang dicari: ")
        # method cari nama dan ambil hasilnya dalam list
        dataCari = ut.CariData(nama, 1, dataHobi) # kolom nomor 1: nama hobi
        if len(dataCari) != 0:
            # list hobi
            daftarHobiCari = ut.LihatDataCari(dataHobi, dataCari)
            # list kode hobi saja
            daftarKodeHobi = [x.split("#")[0] for i,x in enumerate(daftarHobiCari)]
            outMhshobi = []
            hobiTanpaMhs = []
            # list nim berdasarkan hobi
            for iKodeHobi in daftarKodeHobi:
                idxNIM = ut.CariData(iKodeHobi, 1, dataMhsHobi)
                if len(idxNIM) == 0:
                    # daftar hobi tanpa peminat
                    hobiTanpaMhs.append(iKodeHobi)
                else:
                    # daftar hobi dengan peminat
                    outMhshobi.append(ut.LihatDataCari(dataMhsHobi, idxNIM))
            
            # list kode hobi untuk nim yang terdaftar (memiliki hobi)
            if len(outMhshobi) != 0:
                for i, iMhsHobi in enumerate(outMhshobi):
                    if len(iMhsHobi)>0:
                        oKodeHobi = iMhsHobi[0].split("#")[1]
                        #print(oKodeHobi)
                        oNamaHobi = dataHobi[ut.CariData(oKodeHobi, 0, dataHobi, True)[0]].split("#")[1]
                        print(f"\nHobi {i+1}: {oKodeHobi} {oNamaHobi}, diminati oleh:")
                        for h in iMhsHobi:
                            oNim = h.split("#")[0]
                            daftarMhs = dataMhs[ut.CariData(oNim, 0, dataMhs, True)[0]].split("#")[1]
                            print(oNim, daftarMhs)

            # daftar hobi yang dicari ada, tapi tidak ada peminat
            if len(hobiTanpaMhs)>0:
                print("\nHobi ditemukan namun tidak punya peminat:")
                for iHobi in hobiTanpaMhs:
                    for allHobiCari in daftarHobiCari:
                        if allHobiCari.find(iHobi) == 0:
                            oKodeHobi = allHobiCari.split("#")[0]
                            oNamaHobi = allHobiCari.split("#")[1]
                            print(oKodeHobi, oNamaHobi)

        else:
            print(f"Hobi dengan '{nama}' tidak ditemukan.")
    elif pilMenu == "0":
        break
    else:
        print("Pilih angka sesuai yang tertulis pada menu.")