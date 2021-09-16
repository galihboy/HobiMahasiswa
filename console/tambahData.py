# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 21:59:47 2021

@author: galih-hermawan
"""

from objManajemenBerkas import ManajemenBerkas, Utilitas

nmFile = "dataMahasiswa.txt"
statusFile = ManajemenBerkas(nmFile).PeriksaBerkas()
mb = ManajemenBerkas(nmFile)
data = mb.BacaBerkas() # baca isi file
ut = Utilitas() 

# merapikan isi file ke dalam list
kamus = []
for i in data:
    d = i.split("#")
    kamus.append(d)
    
if statusFile:
    file1 = open(nmFile, "a", encoding='utf-8')
    with file1:
        # validasi NIM
        while True:
            nim = input("NIM: ")
            # periksa format NIM
            if ut.PeriksaNIM(nim):
                # periksa apakah NIM sudah terdaftar
                if ut.PeriksaNIMKembar(nim, kamus):
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
        
        isi = [nim, nama, jk.lower()] # masukkan ketiga data dalam list
        isi = "#".join(isi) # gabungkan isi list dengan tanda pemisah "#"
        file1.write(isi) 
        file1.write("\n")
    file1.close()    
else:
    print("Berkas tidak terbaca.")