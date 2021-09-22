# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 14:15:55 2021

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
            
    # membersihkan list dari empty string/values
    def BersihkanEmptyList(self, daftar):
        return [x for x in daftar if x]
    
    # membaca isi file dan dikembalikan dalam bentuk list
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
    
    def TulisBerkas(self, listData):
        statusFile = self.PeriksaBerkas()
        if statusFile:
            file1 = open(self.namaFile, "w", encoding='utf-8')
            with file1:    
                for d in listData:
                    file1.write(d + "\n")
            file1.close()
    
    def TambahDataBerkas(self, barisData):
        statusFile = self.PeriksaBerkas()
        if statusFile:
            file1 = open(self.namaFile, "a", encoding='utf-8')
            with file1:    
                file1.write("\n" + barisData)
            file1.close()  
            self.RapikanBerkas()
        #return self.BersihkanEmptyList(isi)

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

class UtilitasFileKode:
    
    polaKodeData = "{.*}"
    polaNamaFile = "^file\[.*\]"
    polaBaris = "^file\[.*\]={.*}$"
    #--------------------------------------
    polaBarisPola = "^pola\[.*\]={.*}$"
    polaNamaFilePola = "^pola\[.*\]"
    polaDataPola = "{.*}"
    polaDataUmum = "^.+$"
    #--------------------------------------
    fileKode = "kodeData.txt"
    mb = ManajemenBerkas(fileKode)
    
    def __init__(self):
        pass        
    
    # mengambil karakter (string) delimiter/pemisah kolom dari file
    def PemisahKolom(self):
        isi = self.mb.BacaBerkas()
        kunci = "delimiter-kolom="
        strPemisah = ""
        
        for teks in isi:
            teks = teks.strip()
            if teks.find(kunci) != -1:
                strPemisah = teks.split(kunci)[1]
            #else:
            #    print("Format delimiter salah.")
        return strPemisah
    
    # list kolom untuk satu baris kode - berdasarkan daftar kode mentah (raw)
    # dapat digunakan untuk konversi raw values (kolom) ke bentuk list
    def AmbilKolom(self, barisKode, delimiter):
        daftarKolom = []
        if barisKode.find(delimiter) == -1:
            daftarKolom.append(barisKode)
        else:
            lstKode = barisKode.split(delimiter)
            [daftarKolom.append(i) for i in lstKode]
        return daftarKolom
    
    # list kolom untuk semua baris kode
    # dapat digunakan untuk konversi raw values (kolom) ke bentuk list untuk semuat baris data
    def DaftarKolom(self, daftarKode, delimiter):
        lstKolom = []
        [lstKolom.append(self.AmbilKolom(x, delimiter)) for x in daftarKode]
        return lstKolom

    # mengambil daftar nama file penyimpanan dan daftar kode (mentah/raw)
    def AmbilKodeDataFile(self):
        kode = self.mb.BacaBerkas()
        daftarNamaFile = []
        daftarKode = []
        for i in kode:
            i = i.strip()
            cekPola = re.match(self.polaBaris, i)
            if cekPola:
                nmFile = re.findall(self.polaNamaFile, i)
                nmFile = re.sub("file\[|\]","", nmFile[0])
                kodeFile = re.findall(self.polaKodeData, i)
                kodeFile = re.sub("{|}", "", kodeFile[0])
                daftarKode.append(kodeFile)
                daftarNamaFile.append(nmFile)
            #print(f"{nmFile} : {cekPola}")
        return daftarNamaFile, daftarKode
    
    # mengambil daftar nama file penyimpanan dan daftar kode (mentah/raw)
    def AmbilKodePola(self):
        kode = self.mb.BacaBerkas()
        daftarNamaFile = []
        daftarKode = []
        for i in kode:
            i = i.strip()
            cekPola = re.match(self.polaBarisPola, i)
            if cekPola:
                nmFile = re.findall(self.polaNamaFilePola, i)
                nmFile = re.sub("pola\[|\]","", nmFile[0])
                kodeFile = re.findall(self.polaDataPola, i)
                kodeFile = re.sub("{{|}}", "", kodeFile[0])
                daftarKode.append(kodeFile)
                daftarNamaFile.append(nmFile)
            #print(f"{nmFile} : {cekPola}")
        # pola kolom yang kosong diisi dengan pola umum
        #daftarKode = [self.polaUmum if d=="" else d for i, d in enumerate(daftarKode)]
        return daftarNamaFile, daftarKode

    # mengorganisir dalam kamus berupa nama file dan list nama kolom
    def KamusFile_Kode(self, delimiter):
        kamus = {}
        lstFile, lstKode = self.AmbilKodeDataFile()
    
        for i in range(len(lstFile)):
            kunci = lstFile[i]
            lstKolom = self.AmbilKolom(lstKode[i], delimiter)
            kamus[kunci]=lstKolom
        return kamus
    
    # melakukan verifikasi per berkas data
    def VerifikasiFile(self, lstKolom, sumberData, delimiter):
        pesan = ""
        status = True
        # isi file teks tidak boleh kosong
        if len(sumberData) == 0 : 
            pesan = f"\nFile {sumberData} masih kosong."
            status = False
            # format kolom tidak boleh kosong
        elif len(lstKolom) == 0 :
            pesan = "\nFormat kolom belum diisi lengkap."
            status = False
        # format kolom ada yang tidak mengandung delimiter sesuai yang ditetapkan
        elif lstKolom.find(delimiter) == -1:
            pesan = "\nFormat kolom tidak mengandung delimiter yang ditetapkan."
            status = False
        # jumlah kolom setiap baris data apakah sama dengan jumlah kolom pada format
        else:
            for j in range(len(sumberData)):
                pjgFormat = len(self.AmbilKolom(lstKolom, delimiter))
                pjgData = len(self.AmbilKolom(sumberData[j], delimiter))
                if pjgFormat != pjgData :
                    pesan = f"\nJumlah kolom format = {pjgFormat}, \
                        \nJumlah kolom data baris ke-{j+1} = {pjgData}. Tidak konsisten."
                    status = False
                    break
        
        print(pesan)
        return status
    
    # menampilkan hasil verifikasi file
    def HasilVerifikasiFile(self, delimiter):
        lstFile, lstKode = self.AmbilKodeDataFile()
        statusVerifikasiAll = True
        for i in range(len(lstFile)):
            hasilVerifikasi = self.VerifikasiFile(lstKode[i], ManajemenBerkas(lstFile[i]).BacaBerkas(), delimiter)
            statusVerifikasiAll = statusVerifikasiAll and hasilVerifikasi
            print(f"Verifikasi {lstFile[i]}: {hasilVerifikasi}")
    
        return statusVerifikasiAll
    
class Utilitas:
    # RegEx
    # tanggal = yyyy-mm-dd
    polaTanggal = "^(?:19|20)\d\d(-)(?:0[1-9]|1[012])(-)(?:0[1-9]|[12]\d|3[01])$"
    # kode hobi = haa -> a: angka
    polaKodeHobi = "^(h)(?:0[1-9]|\d\d)$"
    
    def __init__(self):
        pass

    # Mencari data dalam sumber data
    # dataCari = string masukan yang akan dicari
    # noKolom = posisi nomor kolom yang jadi target pencarian
    # sumberData = sumber data file
    # tepat = False (mencari sub string dalam string), True (mencari string utuh)
    # inclData = True (memunculkan no urut/baris data yang ditemukan), 
    #            False (hanya memunculkan True [ditemukan] atau False [tidak ketemu])
    def CariData(self, dataCari, noKolom, sumberData, delimiter, \
                 tepat = False, inclData = True):
        dataCari = dataCari.lower().strip()
        if tepat:
            hasil = [i for i,data in enumerate(sumberData) if data.split(delimiter)[noKolom].lower()==dataCari]
        else:        
            hasil = [i for i,data in enumerate(sumberData) if dataCari in data.split(delimiter)[noKolom].lower()]
            
        if not inclData:
            return len(hasil) > 0
        else:
            return hasil
    
    # data baris (format raw) dari sumber data yang diinginkan
    # daftarIndek = nomor urut baris (hasil pencarian)
    # sumberData = sumber data dari file
    # delimiter = pemisah kolom
    # outputKolom = list no urut kolom yang ingin ditampilkan
    def AmbilData(self, daftarIndeks, sumberData, delimiter, outputKolom = []):
        hasil = []
        for i,data in enumerate(daftarIndeks):
            if len(outputKolom) == 0:
                hasil = [sumberData[data] for i,data in enumerate(daftarIndeks)]
                #print(hasil)
            else:
                isiKolom = []
                for o in outputKolom:
                    isiKolom.append(sumberData[data].split(delimiter)[int(o)])
                isiBaris = delimiter.join(isiKolom)
                hasil.append(isiBaris)
        return hasil
    
    # mengembalikan nilai indeks (no urut kolom) berdasarkan nama kolom
    def IndeksKolom(self, namaKolom, kunciKamus, kamus):
        return int([i for i,x in enumerate(kamus[kunciKamus]) if x == namaKolom][0])
    
    # mengembalikan nilai indeks (no urut kolom) berdasarkan nama kolom
    # untuk banyak kolom sekaligus
    def IndeksKolomMulti(self, listKolom, kunciKamus, kamus, delimiter):
        nomorKolom = []
        #sbrData = BacaBerkas(kunciKamus)
        for nk in listKolom:
            nomorKolom.append(self.IndeksKolom(nk, kunciKamus, kamus))
        #print(nomorKolom)
        return nomorKolom
    
    # menampilkan data relasi
    # menampilkan data hobi berdasarkan nim mahasiswa
    # atau, menampilkan data mahasiswa berdasarkan kode hobi
    def ListDataRelasi(self, dataKunciCari, nmKolomKunci, namaKolomFK, lstKolomOutput, \
                      nmFilePenghubung, nmFileTarget, kamus, delimiter) :
        # baca isi berkas
        dataPenghubung = ManajemenBerkas(nmFilePenghubung).BacaBerkas()
        dataTarget = ManajemenBerkas(nmFileTarget).BacaBerkas()
        # nomor kolom Kunci
        nmrKolomDataPenghubung = self.IndeksKolom(nmKolomKunci, nmFilePenghubung, kamus)
        # nomor kolom FK (Foreign Key) pada data Penghubung
        nmrKolomOutputDataPenghubung = self.IndeksKolom(namaKolomFK, nmFilePenghubung, kamus)
        # nomor kolom FK pada data target
        nmrKolomFK = self.IndeksKolom(namaKolomFK, nmFileTarget, kamus)
        # nomor kolom target luaran
        nmrKolomTarget = self.IndeksKolomMulti(lstKolomOutput, nmFileTarget, kamus, delimiter)
        # no baris data kunci cari pada data penghubung
        noBaris = self.CariData(dataKunciCari, nmrKolomDataPenghubung, dataPenghubung, delimiter)
        # kolom FK berdasarkan baris yang sudah ditemukan sebelumnya
        listKodeFK = self.AmbilData(noBaris, dataPenghubung, delimiter, [nmrKolomOutputDataPenghubung])
        #print(listKodeHobi)
        listDataLuaran = []
        for kh in listKodeFK:
            # no baris data FK pada data target
            nmrBarisKolomTarget = self.CariData(kh, nmrKolomFK, dataTarget, delimiter, True)
            # data baris sesuai kolom yang ditentukan
            listDataLuaran.append(self.AmbilData(nmrBarisKolomTarget, dataTarget, delimiter, nmrKolomTarget)[0])
        
        return listDataLuaran
    
    # fitur update file
    # cari baris data lama, jika ketemu ganti dengan baris data baru
    # luaran berupa semua baris data yang siap disimpan ke file
    def UpdateData(self, barisDataLama, barisDataBaru, sumberData):
        dataBaru = [barisDataBaru if d==barisDataLama else d for d in sumberData]
        return dataBaru
