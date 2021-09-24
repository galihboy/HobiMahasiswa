# -*- coding: utf-8 -*-
"""
Created on Fri Sep 24 21:48:12 2021

@author: galih-hermawan
"""

from libHobiMahasiswa import UtilitasFileKode

utFK = UtilitasFileKode()
delimiter = utFK.PemisahKolom()

while True:
    print("\n------ \nAplikasi Pengelolaan Data Hobi Mahasiswa.")
    pilM = input("[1] Verifikasi File, \n[2] Lihat Data, \n[3] Cari Data, \
                  \n[4] Tambah Data, \n[5] Update Data, \n[6] Hapus Data, \
                  \n[0] Keluar : ") 
    pilM = pilM.lower().strip()
    if pilM == "1":
        print("\n------")
        status = utFK.HasilVerifikasiFile(delimiter)
        print("Verifikasi file sukses dan format semua file valid.") if status else print("Verifikasi tidak sukses dan format data file ada yang tidak sesuai.")
    elif pilM == "2":
        print("\n------")
        exec(open('lihatData.py').read())
    elif pilM == "3":
        print("\n------")
        exec(open('cariData.py').read())
    elif pilM == "4":
        print("\n------")
        exec(open('tambahData.py').read())
    elif pilM == "5":
        print("\n------")
        exec(open('updateData.py').read())
    elif pilM == "6":
        print("\n------")
        exec(open('hapusData.py').read())
    elif pilM == "0":
        break
    else:
        print("Pilih sesuai menu tersedia.")