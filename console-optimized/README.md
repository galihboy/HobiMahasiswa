## Aplikasi console untuk mengelola data mahasiswa, hobi dan mahasiswa hobi.
###### Developed by [Galih Hermawan](https://galih.eu).
---

Aplikasi ini dibangun sebagai sarana edukasi untuk mendemokan bagaimana mengakses data yang tersimpan dalam file teks. Data disimpan dengan menggunakan pola atau format tertentu yang ditetapkan. Berikutnya melalui aplikasi (berbasis console) dapat dilakukan pengaksesan atau pengelolaan data, seperti: melihat, mencari, memperbarui, menambah, dan menghapus data.

**Bahasa pemrograman:** python 3.8

**Berkas:**
1. kodeData.txt
	- digunakan untuk memuat tanda delimiter (pemisah) antar kolom, kamus (pemetaan) nama berkas penyimpanan data, nama kolom, dan kamus untuk pola regex (regular expression) buat keperluan validasi data masukan.
2. dataMahasiswa.txt, mencakup: nim (nomor induk mahasiswa), nama lengkap, kota lahir, tanggal lahir, dan jenis kelamin (jk), tempat tinggal, tanggal terdaftar, dan tinggi badan --> kolom unik: nim
	- format data: 
	 	```
		nim#nama#kota lahir#tanggal lahir#jenis kelamin#kota tinggal#tanggal daftar#tinggi
		```
	dataHobi.txt, mencakup: kode hobi, nama hobi --> kolom unik: kode hobi
	- format data:
		```
		kode hobi#nama hobi
		```
	dataMhsHobi.txt, mencakup: nim, kode hobi --> kedua kolom dianggap sejenis foreign key (FK)
	- format data:
		```
		nim#kode hobi
		```
2. libHobiMahasiswa.py
	- object atau class untuk berbagai macam keperluan
		- ManajemenBerkas -> terkait dengan pengelolaan berkas (baca, tulis, validasi)
		- UtilitasFileKode -> terkait fitur mengambil delimiter, mengambil kolom, menerjemahkan kolom berdasarkan indeks, dst.
		- Utilitas -> terkait fitur-fitur terkait fungsionalitas utama (cari data, ambil data, dst.)
3. lihatData.py
	- menampilkan data berkas berupa daftar (*list*)
4. cariData.py
	- fitur untuk melakukan pencarian data mahasiswa, data hobi, data mahasiswa disertai hobi, data hobi disertai mahasiswa
5. tambahData.py
	- fitur untuk menambah data baru
	- data unik (primary key): nim di mahasiswa, dan kode hobi di hobi
	- data unik di mhshobi berupa pasangan FK nim dan kode hobi (secara bersamaan)
6. updateData.py
	- fitur memperbarui data
	- untuk data mahasiswa dan hobi, selain kolom kunci dapat diperbarui
	- data kosong menunjukkan data yang disimpan adalah data yang lama
7. hapusData.py
	- fitur menghapus data
	- data mahasiswa dan hobi, yang kolom uniknya menjadi tamu (FK) di data mhshobi, tidak bisa dihapus
8. testing.py
	- untuk menguji sebagian fitur/metode yang ada di libHobiMahasiswa
	
**Format data masukan (dan makna pola RegEx).**

```
nim = wajib delapan digit angka
tipe tanggal = yyyy-mm-dd (tahun-bulan-tanggal)
jenis kelamin (jk) = l/p
kode hobi = hxx (xx adalah angka 01-99)
tinggi badan = 2-3 digit angka
selain itu bebas (alpha numeric) minimal 1 karakter
```
