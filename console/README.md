## Aplikasi console untuk mengelola data mahasiswa.
###### Developed by [Galih Hermawan](https://galih.eu).

---

**Berkas:**
1. dataMahasiswa.txt
	- berkas untuk menampung data mahasiswa sesuai dengan format atau kode berikut: 
	 	```
		nim#nama#jk
		```
	- **Data mahasiswa mencakup:** nim (nomor induk mahasiswa), nama lengkap, dan jenis kelamin (jk).

2. objManajemenBerkas.py
	- object atau class untuk berbagai macam keperluan
		- ManajemenBerkas -> terkait dengan pengelolaan berkas (baca, tulis, validasi)
		- Utilitas -> terkait fitur-fitur terkait fungsionalitas utama (cari nim, cari nama, dst.)
3. lihatData.py
	- menampilkan data berkas berupa daftar (*list*)
4. cariData.py
	- fitur untuk melakukan pencarian data mahasiswa
	- input pertama berupa pilihan : ***nim*** atau ***nama***
		- selanjutnya, input nim berupa string berisi 8 digit bilangan
		- input nama berupa string
5. tambahData.py
	- fitur untuk menambah data baru
	- data nim bersifat unik, 8 digit bilangan
	- data nama tipe string
	- data jenis kelamin memilih salah satu dari: ***l*** untuk laki-laki, atau ***p*** untuk perempuan
6. updateData.py
	- fitur memperbaharui data berdasarkan nim
	- input pertama berupa nim, jika ditemukan dapat langsung dilanjutkan ke pembaharuan data
	- ketiga data (nim, nama, dan jk) dapat dikosongkan jika ingin menggunakan data yang lama
7. hapusData.py
	- fitur menghapus data berdasarkan nim