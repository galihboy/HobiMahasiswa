# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 21:18:30 2021

@author: galih-hermawan
"""

import os
import re

class ManajemenBerkas:
    def __init__(self, namaFile):
        self.namaFile = namaFile
        
    def PeriksaBerkas(self):
        # periksa apakah file valid
        if os.path.isfile(self.namaFile):
            return True
        else:
            try:
                file1 = open(self.namaFile, "r", encoding='utf-8')
                file1.closed()
            except FileNotFoundError:
                print(f"Berkas {self.namaFile} tidak ditemukan.")
                return False
            except OSError:
                print(f"Terdapat kesalahan OS saat membuka file {self.namaFile}")
                return False
            except Exception as err:
                print(f"Terdapat kesalahan tak terduga saat membuka file {self.namaFile} - ",repr(err))
                return False                
            else:
                return True
            
    def BersihkanEmptyList(self, daftar):
        return [x for x in daftar if x]
    
    def BacaBerkas(self):
        statusFile = self.PeriksaBerkas()
        isi = []
        if statusFile:
            file1 = open(self.namaFile, "r", encoding='utf-8')
            with file1:
                # pisah data file per baris dan hapus data kosong
                isi = file1.read().strip().split("\n")
        
            file1.close()  
        return self.BersihkanEmptyList(isi)
    
    def TulisBerkas(self, kamus):
        statusFile = self.PeriksaBerkas()
        isi = []
        if statusFile:
            file1 = open(self.namaFile, "w", encoding='utf-8')
            
            for i in range(len(kamus)):
                dataTulis = "#".join(kamus[i])
                file1.write(dataTulis + "\n")
            file1.close()  
        return isi
    
    # baca file, bersihkan empty values, tulis ulang
    def RapikanBerkas(self):
        statusFile = self.PeriksaBerkas()
        isiBerkas = self.BacaBerkas()
        if statusFile:
            file1 = open(self.namaFile, "w", encoding='utf-8')
            with file1:
                # pisah data file per baris dan hapus data kosong
                for data in isiBerkas:
                    file1.write(data + "\n")
        
            file1.close()  
    
class Utilitas:
    # RegEx
    # tanggal = yyyy-mm-dd
    pola = "^(?:19|20)\d\d(-)(?:0[1-9]|1[012])(-)(?:0[1-9]|[12]\d|3[01])$"
    # kode hobi = haa -> a: angka
    polaKodeHobi = "^(h)(?:0[1-9]|\d\d)$"
    
    def __init__(self):
        pass
    
    def CariData(self, dataCari, noKolom, isiBerkas, tepat = False):
        dataCari = dataCari.lower().strip()
        if tepat:
            return [i for i,data in enumerate(isiBerkas) if data.split("#")[noKolom].lower()==dataCari]
        else:        
            return [i for i,data in enumerate(isiBerkas) if dataCari in data.split("#")[noKolom].lower()]

    def PeriksaNIM(self, nim):
        # panjang karakter harus 8
        if len(nim.strip()) != 8:
            return False
        elif not nim.isdigit(): # NIM harus berisi bilangan semua
            return False
        else:
            return True
        
    def PeriksaNIMKembar(self, nim, daftarMHS, tampilkanData = False):
        kembar = False
        dataCari = []
        for i in range(len(daftarMHS)):
            # jika NIM yang dicari ditemukan
            if daftarMHS[i][0].find(nim) >= 0:
                kembar = True
                dataCari = daftarMHS[i]
                break
            
        if not tampilkanData:
            return kembar
        else:
            return dataCari
    
    def CariNIM(self, NIM, isiBerkas):
        # data.split("#")[0] -> kolom NIM
        return [i for i,data in enumerate(isiBerkas) if data.split("#")[0]==NIM]
    
    def CariNama(self, nama, daftarMHS):
        dataCari = []
        for i in range(len(daftarMHS)):
            # jika Nama yang dicari ditemukan
            if daftarMHS[i][1].find(nama) >= 0:
                dataCari.append(daftarMHS[i])
            
        return dataCari
    
    def CariNamaBaru(self, nama, isiBerkas):
        nama = nama.lower().strip()
        # data.split("#")[1] -> kolom nama
        return [i for i,data in enumerate(isiBerkas) if nama in data.split("#")[1].lower()]
    
    def LihatDataCari(self, isiBerkas, daftarIndeks):
        data = []
        for i in daftarIndeks:
            data.append(isiBerkas[i])
            
        return data
        
    def HapusData(self, nim, daftarMHS):
        dataBaru = []
        for i in range(len(daftarMHS)):
            # jika NIM yang dicari tidak ditemukan
            if daftarMHS[i][0].find(nim) == -1:
                dataBaru.append(daftarMHS[i])
        
        return dataBaru
    
    def UpdateData(self, nim, daftarMHS, dataUpdate):
        dataBaru = []
        for i in range(len(daftarMHS)):
            # jika NIM yang dicari tidak ditemukan
            if daftarMHS[i][0].find(nim) == -1:
                dataBaru.append(daftarMHS[i])
            else:
                dataBaru.append([dataUpdate])
        
        return dataBaru
    
    def ValidasiDataMahasiswa(self, isiBerkas):
        # 10110001#Adi Sudrajat#Bandung#2000-01-01#l#Bandung#2018-08-01#170
        # validasi NIM
        while True:
            nim = input("NIM: ")
            # periksa format NIM
            if self.PeriksaNIM(nim):
                # periksa apakah NIM sudah terdaftar
                dataNIM = self.CariNIM(nim, isiBerkas)
                if len(dataNIM) > 0:
                    print("NIM sudah terdaftar.")
                else:
                    break
            else:
                print("Format NIM tidak sesuai.")
                
        # validasi nama
        while True:
            nama = input("Nama lengkap: ")
            # nama tidak boleh kosong
            if len(nama.strip()) == 0:
                print("Nama harus diisi.")
            else:
                break
        
        # validasi kota lahir
        while True:
            kotaLahir = input("Kota tempat lahir: ")
            # kota lahir tidak boleh kosong
            if len(kotaLahir.strip()) == 0:
                print("Kota lahir harus diisi.")
            else:
                break
        
        # validasi tanggal lahir
        while True:
            tglLahir = input("Tanggal lahir (YYYY-MM-DD): ")
            polaTglLahir = re.match(self.pola, tglLahir)
            # tanggal lahir tidak boleh kosong
            if len(tglLahir.strip()) == 0:
                print("Tanggal lahir harus diisi.")
            elif not polaTglLahir:
                print("Format tanggal lahir salah.")
            else:
                break
            
        # validasi jenis kelamin
        while True:
            jk = input("Jenis kelamin (l/p): ")
            # isi jenis kelamin harus "l" atau "p"
            if jk.lower() not in ['l','p']:
                print("Jenis kelamin harus diisi 'l' atau 'p'.")
            else:
                break
        
         # validasi kota tempat tinggal
        while True:
            kotaTinggal = input("Kota tempat tinggal: ")
            # kota tempat tinggal tidak boleh kosong
            if len(kotaTinggal.strip()) == 0:
                print("Kota tempat tinggal harus diisi.")
            else:
                break
        
        # validasi tanggal terdaftar
        while True:
            tglTerdaftar = input("Tanggal terdaftar (YYYY-MM-DD): ")
            polaTglDaftar = re.match(self.pola, tglTerdaftar)
            # tgl daftar tidak boleh kosong
            if len(tglTerdaftar.strip()) == 0:
                print("Tanggal lahir harus diisi.")
            elif not polaTglDaftar:
                print("Format tanggal lahir salah.")
            else:
                break
            
        # validasi tinggi badan
        while True:
            tinggi = input("Tinggi badan: ")
            # tinggi badan tidak boleh kosong
            if len(tinggi.strip()) == 0:
                print("Tinggi badan harus diisi.")
            elif not tinggi.isdigit():
                print("Tinggi badan harus berupa angka.")
            else:
                break
        
        # 10110001#Adi Sudrajat#Bandung#2000-01-01#l#Bandung#2018-08-01#170
        return nim, nama, kotaLahir, tglLahir, jk, kotaTinggal, tglTerdaftar, tinggi
    
    def ValidasiDataHobi(self, isiBerkas):
        # validasi Kode Hobi
        while True:
            kodeHobi = input("Kode hobi (HXX). X adalah angka: ")
            kodeHobi = kodeHobi.lower().strip()
            kodeTerdaftar = self.CariData(kodeHobi, 0, isiBerkas, True)
            polaSesuai = re.match(self.polaKodeHobi, kodeHobi)
            # kode hobi tidak boleh kosong
            if len(kodeHobi.strip()) == 0:
                print("Kode hobi harus diisi.")
            elif not polaSesuai:
                print("Format kode hobi salah.")
            elif len(kodeTerdaftar) > 0:
                print("Kode hobi sudah terdaftar.")
            else:
                break
                
        # validasi nama hobi
        while True:
            nama = input("Nama hobi: ")
            namaKembar = self.CariData(nama, 1, isiBerkas, True)
            # nama hobi tidak boleh kosong
            if len(nama.strip()) == 0:
                print("Nama hobi harus diisi.")
            elif len(namaKembar) > 0:
                print("Nama hobi sudah terdaftar.")
            else:
                break
        
        return kodeHobi, nama
    
    def ValidasiDataMhsHobi(self, isiBerkas, dataMhs, dataHobi):
        # validasi NIM
        while True:
            nim = input("NIM: ")
            # periksa format NIM
            if self.PeriksaNIM(nim):
                # periksa apakah NIM ada di data Mahasiswa
                dataNIM = self.CariNIM(nim, dataMhs)
                if len(dataNIM) == 0:
                    print("NIM tidak terdapat di daftar Mahasiswa.")
                else:
                    break
            else:
                print("Format NIM tidak sesuai.")
                
        # validasi Kode Hobi
        while True:
            kodeHobi = input("Kode hobi (HXX). X adalah angka: ")
            kodeHobi = kodeHobi.lower().strip()
            # cek kode di data hobi
            kodeTerdaftar = self.CariData(kodeHobi, 0, dataHobi, True)
            # cek kode di data mhs hobi
            kodeKembar = self.CariData(kodeHobi, 1, isiBerkas, True)
            polaSesuai = re.match(self.polaKodeHobi, kodeHobi)
            # kode hobi tidak boleh kosong
            if len(kodeHobi.strip()) == 0:
                print("Kode hobi harus diisi.")
            elif not polaSesuai:
                print("Format kode hobi salah.")
            elif len(kodeTerdaftar) == 0: # kode hobi tidak terdaftar
                print("Kode hobi tidak terdaftar.")
            elif len(kodeKembar) > 0:
                print("Kode hobi dengan nim yang sama sudah ada.")
            else:
                break
        
        return nim, kodeHobi
            
    def ValidasiDataUpdate(self, kamus, nimCari):
        # validasi NIM
        print("Kosongkan jika ingin menggunakan data lama.")
        while True:
            nim = input("NIM baru: ")
            if len(nim.strip()) == 0 or nim.strip()==nimCari:
                nim = "-"
                break
            else:
                # periksa format NIM
                if self.PeriksaNIM(nim):
                    # periksa apakah NIM sudah terdaftar
                    if self.PeriksaNIMKembar(nim, kamus):
                        print("NIM sudah terdaftar.")
                    else:
                        break
                else:
                    print("Format NIM tidak sesuai.")
            
        # validasi nama
        while True:
            nama = input("Nama lengkap baru: ")
            if len(nama.strip()) == 0:
                nama = "-"
            break
            
        # validasi jenis kelamin
        while True:
            jk = input("Jenis kelamin baru (l/p): ")
            if len(jk.strip()) == 0:
                jk = "-"
                break
            else:
                # isi jenis kelamin harus "l" atau "p"
                if jk.lower() not in ['l','p']:
                    print("Jenis kelamin harus diisi 'l' atau 'p'.")
                else:
                    break
        
        return nim, nama, jk