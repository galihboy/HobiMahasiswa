# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 21:18:30 2021

@author: galih-hermawan
"""

import os

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
    
    def BacaBerkas(self):
        statusFile = self.PeriksaBerkas()
        isi = []
        if statusFile:
            file1 = open(self.namaFile, "r", encoding='utf-8')
            with file1:
                # pisah data file per baris dan hapus data kosong
                isi = file1.read().strip().split("\n")
        
            file1.close()  
        return isi
    
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
    
class Utilitas:
    def __init__(self):
        pass
    
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
        
    def CariNama(self, nama, daftarMHS):
        dataCari = []
        for i in range(len(daftarMHS)):
            # jika Nama yang dicari ditemukan
            if daftarMHS[i][1].find(nama) >= 0:
                dataCari.append(daftarMHS[i])
            
        return dataCari
    
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
    
    def ValidasiData(self, kamus):
        # validasi NIM
        while True:
            nim = input("NIM: ")
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
            nama = input("Nama lengkap: ")
            # nama tidak boleh kosong
            if len(nama.strip()) == 0:
                print("Nama harus diisi")
            else:
                break
        
        # validasi jenis kelamin
        while True:
            jk = input("Jenis kelamin (l/p): ")
            # isi jenis kelamin harus "l" atau "p"
            if jk.lower() not in ['l','p']:
                print("Jenis kelamin harus diisi 'l' atau 'p'")
            else:
                break
            
        return nim, nama, jk
    
    def ValidasiDataUpdate(self, kamus):
        # validasi NIM
        print("Kosongkan jika ingin menggunakan data lama.")
        while True:
            nim = input("NIM baru: ")
            if len(nim.strip()) == 0:
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
                    print("Jenis kelamin harus diisi 'l' atau 'p'")
                else:
                    break
        
        return nim, nama, jk