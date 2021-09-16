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
            