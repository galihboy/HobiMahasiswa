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
    
class Utilitas:
    def __init__(self):
        pass
    
    def PeriksaNIM(self, nim):
        # panjang karakter harus 8
        if len(nim.strip()) != 8:
            return False
        elif not nim.isdigit():
            return False
        else:
            return True
        
    def PeriksaNIMKembar(self, nim, daftarMHS, tampilkanData = False):
        kembar = False
        dataCari = []
        for i in range(len(daftarMHS)):
            if daftarMHS[i][0].lower().find(nim) >= 0:
                kembar = True
                dataCari = daftarMHS[i]
                break
            
        if not tampilkanData:
            return kembar
        else:
            return dataCari