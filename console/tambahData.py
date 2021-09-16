# -*- coding: utf-8 -*-
"""
Created on Thu Sep 16 21:59:47 2021

@author: galih-hermawan
"""

from objManajemenBerkas import ManajemenBerkas, Utilitas

nmFile = "dataMahasiswa.txt"
statusFile = ManajemenBerkas(nmFile).PeriksaBerkas()
ut = Utilitas()
#print(statusFile)

if statusFile:
    file1 = open(nmFile, "a", encoding='utf-8')
    with file1:
        # validasi NIM
        while True:
            nim = input("NIM: ")
            if ut.PeriksaNIM(nim):
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
    #print(isi)
else:
    print("Berkas tidak terbaca.")