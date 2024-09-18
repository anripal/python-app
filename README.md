# **READ ME**
Gunakan file ini sebagai panduan dalam menjalankan program.

Program ini dibuat sebagai Capstone Project pertama saya di Data Science & Machine Learning bootcamp yang diadakan oleh Purwadhika. Program ini terdiri dari empat fitur dasar pemograman, yaitu Create, Read, Update dan Delete (CRUD). Ini adalah program sederhana sebagai titik awal pengalaman saya di Data Science & Machine Learning. Mohon maklum dan dukungan nya! :)

# Konsep Program
Program ini adalah aplikasi Rental Mobil sederhana menggunakan bahasa Python berbasis command line. Di aplikasi ini, Admin sebagai Stakeholder diminta untuk melakukan login ke program agar dapat mengelola data rental mobil. Pengelolaan yang dimaksud yaitu Menampilkan Daftar Mobil yang tersedia, Menambah Data Mobil baru, Memperbarui Informasi Mobil dan Menghapus Data Mobil (CRUD)

# Fitur
1. **Login ke Program**

   Untuk mengakses program, gunakan detail akun sebagai berikut:
   - **Username**: `anripal`
   - **Password**: `@Admin123`
  
2. **Menampilkan Daftar Mobil**
   
   Menampilkan daftar lengkap mobil yang tersedia untuk disewa atau memfilter berdasarkan ketegori:
     - ID Mobil
     - Nama Mobil
     - Tahun Produksi
     - Harga Sewa Harian
     - Status Rental (Tersedia/Disewakan)
     - Semua

3. **Membuat Data Mobil Baru**
   - Admin dapat menambahkan mobil baru ke dalam program dengan ID Mobil tipe data unik (tidak boleh duplikat dengan ID Mobil yang sudah ada), Nama Mobil, Tahun Produksi, Harga Sewa Harian, dan Status Rental.

4. **Memperbarui Informasi Mobil**
   - Memodifikasi Nama Mobil atau Status Rental Mobil berdasarkan ID mobil.

5. **Menghapus Data Mobil**
   - Menghapus mobil dari program berdasarkan ID mobil.

# **Data Collection Type**

Program ini menggunakan struktur data berbasis Dictionary untuk menyimpan informasi akun admin dan data mobil. Berikut adalah struktur data nya:

1. **Akun Admin**:
    ```python
    admin = {"username": "anripal", "password": "@Admin123"}
    ```

2. **Data Rental Mobil**:
    ```python
   rental_mobil = {
       1190: {'Nama Mobil': "Honda Brio", 'Tahun Produksi': 2016, 'Harga Sewa Harian': 1000000, 'Status Rental': "Tersedia"},
       1191: {'Nama Mobil': "Toyota Agya", 'Tahun Produksi': 2018, 'Harga Sewa Harian': 1200000, 'Status Rental': "Disewakan"},
       1292: {'Nama Mobil': "Honda Brio", 'Tahun Produksi': 2022, 'Harga Sewa Harian': 1500000, 'Status Rental': "Disewakan"},
       1196: {'Nama Mobil': "Honda WRV", 'Tahun Produksi': 2024, 'Harga Sewa Harian': 1800000, 'Status Rental': "Tersedia"},
       1290: {'Nama Mobil': "Toyota Innova", 'Tahun Produksi': 2016, 'Harga Sewa Harian': 1000000, 'Status Rental': "Disewakan"},
       1170: {'Nama Mobil': "Toyota Yarris", 'Tahun Produksi': 2021, 'Harga Sewa Harian': 2000000, 'Status Rental': "Tersedia"},
       1120: {'Nama Mobil': "Honda Jazz", 'Tahun Produksi': 2023, 'Harga Sewa Harian': 1500000, 'Status Rental': "Tersedia"},
       1590: {'Nama Mobil': "Suzuki Ertiga", 'Tahun Produksi': 2016, 'Harga Sewa Harian': 1000000, 'Status Rental': "Disewakan"}
   }
    ```

# **Function**

1. **read_mobil**: Menampilkan informasi mobil berdasarkan berbagai kategori (ID, nama, tahun, dll.).
2. **create_mobil**: Menambahkan mobil baru ke dalam database
3. **update_mobil**: Memperbarui nama mobil atau status rental
4. **delete_mobil**: Menghapus mobil dari database


# **Penggunaan Program**

1. Clone repository ini ke komputer lokal tujuan
2. Jalankan file Python
3. Masuk menggunakan akun admin yang disediakan
4. Gunakan menu untuk mengelola database Rental Mobil

# Contoh Interaksi
1. Login ke program Rental Mobil
   
Admin (user) akan terus diminta untuk mengisi kredensial sampai username dan password benar.

<img width="346" alt="Screenshot 2024-09-18 at 10 33 02 PM" src="https://github.com/user-attachments/assets/a4f8bdef-09a2-47d8-b5e5-22d47380c69f">

3. Menampilkan Data Mobil
Admin (user) dapat menampilkan data mobil sesuai pilihan yang diinginkan

<img width="1061" alt="Screenshot 2024-09-18 at 10 35 03 PM" src="https://github.com/user-attachments/assets/8a42681c-0be0-48d6-8f69-2d86079799f9">

5. Membuat Data Mobil

Admin (user) juga fleksibel untuk memilih fitur saat ini atau kembali ke menu utama. Disini, setelah menampilkan data mobil, Admin (user) ke menu utama agar dapat mengganti fitur Membuat Data Mobil.

Dalam membuat data mobil, Admin(user) perlu mengisi data sesuai dengan yang diperintahkan. Hanya ID Mobil baru yang akan dibuat, jika ID Mobil sudah ada di database maka tidak bisa membuat data baru.

<img width="449" alt="Screenshot 2024-09-18 at 10 37 38 PM" src="https://github.com/user-attachments/assets/ec7f7dcc-245d-4830-9179-b0d1f503d4b7">

4. Mengubah Data Mobil
   
Admin (user) dapat mengubah informasi data mobil, hanya untuk mobil yang ID nya ada di database. Kemudian Admin (user) juga dapat memilih apakah data yang diubah akan disimpan atau dibatalkan.

<img width="987" alt="Screenshot 2024-09-18 at 10 40 52 PM" src="https://github.com/user-attachments/assets/9a3b83ee-6825-408a-9c83-a1ea5741f524">

6. Menghapus Data Mobil

Admin (user) dapat menghapus data mobil yang diinginkan berdasarkan ID Mobil. Hanya ID Mobil yang memang ada di database yang akan di proses, jika ID Mobil tidak ada maka tidak dihapus.
   
<img width="989" alt="Screenshot 2024-09-18 at 10 42 50 PM" src="https://github.com/user-attachments/assets/2ceae517-9d3a-47a1-a284-d70e8228233e">
