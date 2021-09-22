# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 14:31:40 2021

@author: galih-hermawan

Testing modul

"""

from libHobiMahasiswa import ManajemenBerkas, UtilitasFileKode, Utilitas

utFK = UtilitasFileKode() 
ut = Utilitas()

#============ 01. Tes Delimiter =============
delimiter = utFK.PemisahKolom()
print("___ 01 ___")
print(delimiter)
print("__________")
#============================================

#============ 02. Baca file kodeData.txt ===================
isiFileKode = ManajemenBerkas("kodeData.txt").BacaBerkas()
print("\n___ 02 ___")
print(isiFileKode)
print("__________")
#===========================================================

#========== 03. Baca nama file data dan kolom ============
lstFile, lstKolom = utFK.AmbilKodeDataFile()
print("\n___ 03 ___")
for i, data in enumerate(lstFile):
    print(f"File {i+1} : {data} \nKolom : {lstKolom[i]}")
print("__________")
lstPolaFile, lstKolomPola = utFK.AmbilKodePola()
for i, data in enumerate(lstPolaFile):
    print(f"Pola {i+1} : {data} \nKolom : {lstKolomPola[i]}")
print("__________")
#===========================================================

#=== 04. Konversi baris format kode [mahasiswa] ke bentuk list ===
kolomMahasiswa = lstKolom[0]
lstKolomMahasiswa = utFK.AmbilKolom(kolomMahasiswa, delimiter)
print("\n___ 04 ___")
print(lstKolomMahasiswa)
print("__________")
#===========================================================

#========== 05. Bentuk list semua format kolom ============
print("\n___ 05 ___")
print(utFK.DaftarKolom(lstKolom, delimiter))
print("__________")
#===========================================================

#========== 06. Konversi isi file kode ke kamus ============
kamus = utFK.KamusFile_Kode(delimiter)
print("\n___ 06 ___")
print(kamus)
print("__________")
#===========================================================

#========== 07. Konversi isi file kode ke kamus ============
print("\n___ 07 ___")
dataMhs = ManajemenBerkas("dataMahasiswa.txt").BacaBerkas()
print(dataMhs)
print("__________")
#===========================================================

#===== 08. Verifikasi format kolom dan data [file mahasiswa] ======
print("\n___ 08 ___")
statusVerifikasi = utFK.VerifikasiFile(kolomMahasiswa, dataMhs, delimiter)

if statusVerifikasi: print("Verifikasi file mahasiswa sukses dan format file valid.")
print("__________")
#===========================================================

#===== 09. Verifikasi semua file ======
print("\n___ 09 ___")
status = utFK.HasilVerifikasiFile(delimiter)
print("Verifikasi file sukses dan format semua file valid.") if status else print("Verifikasi tidak sukses dan format data file ada yang tidak sesuai.")
print("__________")
#======================================

# TESTING UTILITAS

#=========================== 10. Tes pencarian nim ===========================
print("\n___ 10 ___")
nim1 = "10110009" # format penuh, terdaftar
nim2 = "10110088" # format penuh, tidak terdaftar
nim3 = "10009" # format sebagian, terdaftar
kolomNIM = 0 # posisi nomor urut format data NIM pada data mahasiswa
statusCariData1 = ut.CariData(nim1, kolomNIM, dataMhs, delimiter, True, False )
statusCariData2 = ut.CariData(nim2, kolomNIM, dataMhs, delimiter, True, False)
print(f"Status nim {nim1} ditemukan? {statusCariData1}")
print(f"Status nim {nim2} ditemukan? {statusCariData2}")
statusCariData3 = ut.CariData(nim3, kolomNIM, dataMhs, delimiter, True, False )
print(f"Status nim {nim3} ditemukan? {statusCariData3}")
statusCariData4 = ut.CariData(nim3, kolomNIM, dataMhs, delimiter, False, False ) # pencarian sebagian
print(f"Status nim {nim3} ditemukan? {statusCariData4}")
print("__________")
#=================================================================================

#== 11. Tes pencarian nim dengan return value nomor indeks baris atau empy list ===
print("\n___ 11 ___")
noIndeksBarisMhs = ut.CariData(nim1, kolomNIM, dataMhs, delimiter, True, True )
print(f"NIM {nim1} ditemukan pada indeks baris ke: {noIndeksBarisMhs}")
noIndeksBarisMhs2 = ut.CariData(nim2, kolomNIM, dataMhs, delimiter, True, True )
print(f"NIM {nim2} ditemukan pada indeks baris ke: {noIndeksBarisMhs2} # contoh data tidak ditemukan.")
print("__________")
#=================================================================================

#================ 12. Tes pencarian berdasarkan nama mahasiswa ====================
print("\n___ 12 ___")
kolomNamaMahasiswa = 1
nama1 = "adi"
nama2 = "xyz"
noIndeksBarisMhs3 = ut.CariData(nama1, kolomNamaMahasiswa, dataMhs, delimiter, False, True )
print(f"Nama '{nama1}' ditemukan pada indeks baris ke: {noIndeksBarisMhs3}")
noIndeksBarisMhs4 = ut.CariData(nama2, kolomNamaMahasiswa, dataMhs, delimiter, False, True )
print(f"Nama '{nama2}' ditemukan pada indeks baris ke: {noIndeksBarisMhs4}")
print("__________")
#=================================================================================

#================ 13. Tes pencarian berdasarkan nama hobi ====================
print("\n___ 13 ___")
dataHobi = ManajemenBerkas("dataHobi.txt").BacaBerkas()
kolomNamaHobi = 1
namaHobi = "bola"
noIndeksHobi = ut.CariData(namaHobi, kolomNamaHobi, dataHobi, delimiter, False, True )
print(f"Nama '{namaHobi}' ditemukan pada indeks baris ke: {noIndeksHobi}")
print("__________")
#=================================================================================

#========= 14. Tes menampilkan data mahasiswa yang sebelumnya ditemukan ============
print("\n___ 14 ___")
nomorKolomSemua = [] # empty list jika ingin menampilkan data di semua kolom
# alternatif penulisan 1
dataMhsDitemukan = ut.AmbilData(noIndeksBarisMhs3, dataMhs, delimiter)
# alternatif penulisan 2
# dataMhsDitemukan = ut.AmbilData(noIndeksBarisMhs3, dataMhs, delimiter, nomorKolomSemua)
print(dataMhsDitemukan)
print("__________")
#=================================================================================

#========= 15. Tes menampilkan data mahasiswa dan memilih kolom ============
print("\n___ 15 ___")
nomorKolom = [0,1,4] # 0:nim, 1:nama, 4:jenis kelamin [tidak harus urut]
dataMhsDitemukan2 = ut.AmbilData(noIndeksBarisMhs3, dataMhs, delimiter, nomorKolom)
print(dataMhsDitemukan2)
print("__________")
#=================================================================================

#========= 16. Mengembalikan nomor indeks dari nama kolom ============
print("\n___ 16 ___")
kunciKamusMhs = "dataMahasiswa.txt"
namaKolom1 = "nim"
namaKolom2 = "nama"
nomorIndeks1 = ut.IndeksKolom(namaKolom1, kunciKamusMhs, kamus)
nomorIndeks2 = ut.IndeksKolom(namaKolom2, kunciKamusMhs, kamus)
print(f"Pada kamus file {kunciKamusMhs}:")
print(f"Kolom {namaKolom1} memiliki nomor indeks = {nomorIndeks1}")
print(f"Kolom {namaKolom2} memiliki nomor indeks = {nomorIndeks2}")
#-----------------------------------------------------------------
kunciKamusMhsHobi = "dataMhsHobi.txt"
namaKolom3 = "kode hobi"
nomorIndeks3 = ut.IndeksKolom(namaKolom3, kunciKamusMhsHobi, kamus)
print(f"\nPada kamus file {kunciKamusMhsHobi}:")
print(f"Kolom {namaKolom3} memiliki nomor indeks = {nomorIndeks3}")
print("__________")
#=================================================================================

#========= 17. Mengembalikan nomor indeks beberapa kolom ============
print("\n___ 17 ___")
daftarKolom = ["nim", "nama", "jenis kelamin", "tinggi"]
daftarNomorIndeks = ut.IndeksKolomMulti(daftarKolom, kunciKamusMhs, kamus, delimiter)
print(daftarKolom)
print(daftarNomorIndeks)
print("__________")
#=================================================================================

#================ 18. Menampilkan daftar hobi berdasarkan NIM ===================
print("\n___ 18 ___")
kunciKamusMhs = "dataMahasiswa.txt"
kunciKamusMhsHobi = "dataMhsHobi.txt"
kunciKamusHobi = "dataHobi.txt"
#----------------------------------"
nimCari = "10110001"
kolomPK = "nim" # primary key
kolomRelasi_Mhs_Hobi = "kode hobi" # atribut Foreign Key (sekutu) MhsHobi dan Hobi
kolomOutput = ["kode hobi","nama hobi"] # data kolom yang ingin diperoleh
dataLuaran = ut.ListDataRelasi(nimCari, kolomPK, kolomRelasi_Mhs_Hobi, kolomOutput, \
              kunciKamusMhsHobi, kunciKamusHobi, kamus, delimiter)
print(f"Mahasiswa nim {nimCari} memiliki hobi {dataLuaran}")
print("__________")
#===============================================================================

#================ 19. Menampilkan daftar mahasiswa berdasarkan kode hobi ===================
print("\n___ 19 ___")
kodeHobiCari = "h07"
kolomPK = "kode hobi" # primary key
kolomRelasi_Mhs_Hobi = "nim" # atribut Foreign Key (sekutu) MhsHobi dan Mahasiswa
kolomOutput = ["nim", "nama", "jenis kelamin"] # data kolom yang ingin diperoleh
dataLuaran = ut.ListDataRelasi(kodeHobiCari, kolomPK, kolomRelasi_Mhs_Hobi, kolomOutput, \
              kunciKamusMhsHobi, kunciKamusMhs, kamus, delimiter)
print(f"Hobi dengan kode {kodeHobiCari} diminati oleh mahasiswa {dataLuaran}")
print("__________")
#===========================================================================