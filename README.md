# Rental Mobil
Projek ini adalah aplikasi Rental Mobil sederhana menggunakan bahasa Python berbasis command line. Di aplikasi ini memungkinkan admin untuk mengelola data rental mobil seperti Menampilkan Daftar Mobil yang tersedia, Menambah Data Mobil baru, Memperbarui Informasi Mobil dan Menghapus Data Mobil.

## Fitur

1. **Menampilkan Daftar Mobil**:
   - Menampilkan daftar lengkap mobil yang tersedia untuk disewa atau memfilter berdasarkan ketegori:
     - ID Mobil
     - Nama Mobil
     - Tahun Produksi
     - Harga Sewa Harian
     - Status Rental (Tersedia/Disewakan)

2. **Membuat Data Mobil Baru**:
   - Admin dapat menambahkan mobil baru ke dalam aplikasi dengan ID Mobil tipe data unik (tidak boleh duplikat dengan ID Mobil yang sudah ada), Nama Mobil, Tahun Produksi, Harga Sewa Harian, dan Status Rental.

3. **Memperbarui Informasi Mobil**:
   - Memodifikasi Nama Mobil atau Status Rental Mobil berdasarkan ID mobil.

4. **Menghapus Data Mobil**:
   - Menghapus mobil dari aplikasi berdasarkan ID mobil.

## Akun Admin

Untuk mengakses aplikasi, gunakan detail akun sebagai berikut:

- **Username**: `anripal`
- **Password**: `@Admin123`

## Data Collection Type

Sistem ini menggunakan struktur data berbasis dictionary untuk menyimpan informasi mobil dan akun admin. Berikut adalah strukturnya:

- **Akun Admin**:
    ```python
    admin = {"username": "anripal", "password": "@Admin123"}
    ```

- **Data Rental Mobil**:
    ```python
    rental_mobil = {
        1190: {'Nama Mobil': "Honda Brio", 'Tahun Produksi': 2016, 'Harga Sewa Harian': 1000000, 'Status Rental': "Tersedia"},
        1191: {'Nama Mobil': "Toyota Agya", 'Tahun Produksi': 2018, 'Harga Sewa Harian': 1200000, 'Status Rental': "Disewakan"},
        # Mobil lainnya...
    }
    ```

## Function

- **read_mobil**: Menampilkan informasi mobil berdasarkan berbagai kategori (ID, nama, tahun, dll.).
- **create_mobil**: Menambahkan mobil baru ke dalam sistem.
- **update_mobil**: Memperbarui nama mobil atau status rental.
- **delete_mobil**: Menghapus mobil dari sistem.

## Contoh Interaksi

Selamat Datang di Rental Mobil Program
Masukan Username Anda: anripal Masukan Password Anda: @Admin123

...Berhasil Masuk...
    Fitur :
    1. Menampilkan Daftar Mobil
    2. Menambah Data Mobil
    3. Mengubah Data Mobil
    4. Menghapus Data Mobil
    5. Exit Program

Masukkan fitur yang dipilih : 1


## Persyaratan

- Python
