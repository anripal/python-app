# Database stakeholder
admin = {"username" : "anripal", "password": '@Admin123'}

# Database mobil
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

# Function READ
def read_mobil(level, filter_value=None):
    if level == 1:  # Menampilkan Semua Mobil
        print('''
                    Daftar Mobil
                    ID Mobil\t\t| Nama Mobil \t\t| Tahun Produksi\t| Harga Sewa Harian \t\t| Status Rental''')

        for id_mobil, data in rental_mobil.items():
            print(f'''
                    {id_mobil}\t\t| {data['Nama Mobil']}\t\t| {data['Tahun Produksi']}\t\t\t| {data['Harga Sewa Harian']}\t\t\t| {data['Status Rental']}''')
            
    elif level == 2:  # Berdasarkan ID Mobil
        if filter_value in rental_mobil:
            data = rental_mobil[filter_value]
            print('''
                    Daftar Mobil
                    ID Mobil\t\t| Nama Mobil \t\t| Tahun Produksi\t| Harga Sewa Harian \t\t| Status Rental''')
            print(f'''
                    {filter_value}\t\t| {data['Nama Mobil']}\t\t| {data['Tahun Produksi']}\t\t\t| {data['Harga Sewa Harian']}\t\t\t| {data['Status Rental']}''')
        else:
            print("\nCoba lagi, Data yang diinput tidak ditemukan!")
            
    elif level == 3:  # Berdasarkan Nama Mobil
        temp = 0
        print('''
                    Daftar Mobil
                    ID Mobil\t\t| Nama Mobil \t\t| Tahun Produksi\t| Harga Sewa Harian \t\t| Status Rental''')
        
        for id_mobil, data in rental_mobil.items():
            if filter_value.lower() == data['Nama Mobil'].lower():
                print(f'''
                    {id_mobil}\t\t| {data['Nama Mobil']}\t\t| {data['Tahun Produksi']}\t\t\t| {data['Harga Sewa Harian']}\t\t\t| {data['Status Rental']}''')
            else:
                temp += 1

        if temp == len(rental_mobil):
            print("\nCoba lagi, Data yang diinput tidak ditemukan!")

    elif level == 4:  # Berdasarkan Tahun Produksi
        temp = 0
        print('''
                    Daftar Mobil
                    ID Mobil\t\t| Nama Mobil \t\t| Tahun Produksi\t| Harga Sewa Harian \t\t| Status Rental''')  

        for id_mobil, data in rental_mobil.items():
            if data['Tahun Produksi'] == filter_value:
                print(f'''
                    {id_mobil}\t\t| {data['Nama Mobil']}\t\t| {data['Tahun Produksi']}\t\t\t| {data['Harga Sewa Harian']}\t\t\t| {data['Status Rental']}''')
            else:
                temp += 1

        if temp == len(rental_mobil):
            print("\nCoba lagi, Data yang diinput tidak ditemukan!")

    elif level == 5:  # Berdasarkan Harga Sewa Harian
        temp = 0
        print('''
                    Daftar Mobil
                    ID Mobil\t\t| Nama Mobil \t\t| Tahun Produksi\t| Harga Sewa Harian \t\t| Status Rental''')  
        for id_mobil, data in rental_mobil.items():
            if data['Harga Sewa Harian'] == filter_value:
                print(f'''
                    {id_mobil}\t\t| {data['Nama Mobil']}\t\t| {data['Tahun Produksi']}\t\t\t| {data['Harga Sewa Harian']}\t\t\t| {data['Status Rental']}''')
            else:
                temp += 1

        if temp == len(rental_mobil):
            print("\nCoba lagi, Data yang diinput tidak ditemukan!")

    elif level == 6:  # Berdasarkan Status Rental
        temp = 0
        print('''
                    Daftar Mobil
                    ID Mobil\t\t| Nama Mobil \t\t| Tahun Produksi\t| Harga Sewa Harian \t\t| Status Rental''')  
        for id_mobil, data in rental_mobil.items():
            if data['Status Rental'].lower() == filter_value.lower():
                print(f'''
                    {id_mobil}\t\t| {data['Nama Mobil']}\t\t| {data['Tahun Produksi']}\t\t\t| {data['Harga Sewa Harian']}\t\t\t| {data['Status Rental']}''')
            else:
                temp += 1

        if temp == len(rental_mobil):
            print("\nCoba lagi, Data yang diinput tidak ditemukan!")

# Function CREATE
def create_mobil(id_mobil, nama_mobil, tahun_mobil, harga_sewa, status_mobil, saved):
    if saved.lower() == "ya":
        rental_mobil[id_mobil] = {'Nama Mobil': nama_mobil, 'Tahun Produksi' : tahun_mobil, 'Harga Sewa Harian' : harga_sewa ,'Status Rental': status_mobil}
        print(f"Mobil {nama_mobil} berhasil disimpan.")
    elif saved.lower() == "tidak":
        print(f"Data mobil {nama_mobil} yang dibuat tidak disimpan")
    else:
         print("\nCoba lagi, Pilihan yang diinput tidak tersedia!")

# Function UPDATE
def update_mobil(id_mobil, nama_baru=None, status_baru=None):
    if nama_baru:
        rental_mobil[id_mobil]['Nama Mobil'] = nama_baru
    if status_baru:
        rental_mobil[id_mobil]['Status Rental'] = status_baru

    saved = str(input("Simpan data? Ya/Tidak: "))
    if saved.lower() == "ya":
        print(f"Berhasil memperbarui data mobil dengan ID {id_mobil}.")
    elif saved.lower() == "tidak":
        print(f"Perubahan data mobil dengan ID {id_mobil} tidak disimpan.")

    else:
        print("\nCoba lagi, Pilihan yang diinput tidak tersedia!")

# Function DELETE
def delete_mobil(id_mobil):
    del rental_mobil[id_mobil]
    print(f"Data mobil dengan ID {id_mobil} berhasil dihapus")

while True:
    print("Selamat Datang di Rental Mobil Program")
    userId = str(input("Masukan Username Anda: "))
    userPass = str(input("Masukan Password Anda: "))

    if userId == admin["username"] and userPass == admin["password"]:
        print("\n...Berhasil Masuk...")
        while True:
            pilihanFitur = int(input('''
        Fitur :
        1. Menampilkan Daftar Mobil
        2. Menambah Data Mobil
        3. Mengubah Data Mobil
        4. Menghapus Data Mobil
        5. Exit Program

Masukkan fitur yang dipilih : '''))
            
            # Fitur READ
            if pilihanFitur == 1:
                while True:
                    userInput = int(input('''
                Menampilkan Daftar Mobil berdasarkan Kategori
                1. Semua
                2. ID Mobil
                3. Nama Mobil
                4. Tahun Produksi
                5. Harga Sewa Harian
                6. Status Rental
                7. ke Menu Utama

Masukkan kategori yang dipilih : '''))
                    if userInput == 1:
                        read_mobil(1)
                    
                    elif userInput == 2:
                        a = int(input("Masukkan ID Mobil: "))
                        read_mobil(2, a)

                    elif userInput == 3:
                        a = str(input("Masukkan Nama Mobil: "))
                        read_mobil(3, a)

                    elif userInput == 4:
                        a = int(input("Masukkan Tahun Produksi: "))
                        read_mobil(4, a)

                    elif userInput == 5:
                        a = int(input("Masukkan Harga Sewa Harian: "))
                        read_mobil(5, a)

                    elif userInput == 6:
                        a = str(input("Masukkan Status Rental (Tersedia/Disewakan): ")).capitalize()
                        read_mobil(6, a)

                    elif userInput == 7:
                        break

                    else:
                        print("\nCoba lagi, Pilihan yang diinput tidak tersedia!")

            # Fitur CREATE
            elif pilihanFitur == 2:
                while True:
                    userInput = int(input('''
                Menambah Data Mobil
                1. Input Data
                2. ke Menu Utama

Masukkan kategori yang dipilih : '''))
                    if userInput == 1:
                        a = int(input("Masukkan ID Mobil (4 angka): "))
                        if a not in rental_mobil:
                            b = str(input("Masukkan Nama Mobil: "))
                            c = int(input("Masukkan Tahun Produksi Mobil: "))
                            d = int(input("Masukkan Harga Sewa Harian: "))
                            e = str(input("Masukkan Status Rental (Tersedia/Disewakan): ")).capitalize()
                            f = str(input("Simpan data? Ya/Tidak: "))

                            create_mobil(a, b, c, d, e,f)
                        else:
                            print(f"Data mobil dengan ID {a} sudah ada")
                    elif userInput == 2:
                        break
                    else:
                        print("\nCoba lagi, Pilihan yang diinput tidak tersedia!")
       
            # Fitur UPDATE
            elif pilihanFitur == 3:
                while True:
                    userInput = int(input('''
                Mengubah Data Mobil
                1. Input Data
                2. ke Menu Utama

Masukkan kategori yang dipilih : '''))
                    if userInput == 1:
                        id_mobil = int(input("Masukkan ID Mobil yang ingin diubah: "))
                        if id_mobil in rental_mobil:
                            read_mobil(2, id_mobil)
                            saved = str(input("Lanjutkan perubahan data mobil? Ya/Tidak: "))
                            if saved.lower() == "ya":
                                nama_baru = str(input("Masukkan Nama Mobil baru (kosongkan jika tidak ingin diubah): "))
                                status_baru = str(input("Masukkan Status Rental baru (kosongkan jika tidak ingin diubah): ")).capitalize()
                                update_mobil(id_mobil, nama_baru if nama_baru else None, status_baru if status_baru else None)
                            elif saved.lower() == "tidak":
                                print("Data mobil tidak diubah")
                            else:
                                print("\nCoba lagi, Pilihan yang diinput tidak tersedia!")
                        else:
                            print(f"Data mobil dengan ID {id_mobil} tidak ada")
                    elif userInput == 2:
                        break
                    else:
                        print("\nCoba lagi, Pilihan yang diinput tidak tersedia!")

            # Fitur DELETE
            elif pilihanFitur == 4:
                while True:
                    userInput = int(input('''
                Menghapus Data Mobil
                1. Input Data
                2. ke Menu Utama

Masukkan kategori yang dipilih : '''))
                    if userInput == 1:
                        id_mobil = int(input("Masukkan ID Mobil yang ingin dihapus: "))
                        if id_mobil in rental_mobil:
                            saved = str(input("Lanjut hapus data mobil? Ya/Tidak: "))
                            if saved.lower() == "ya":
                                delete_mobil(id_mobil)
                            elif saved.lower() == "tidak":
                                print(f"Data mobil dengan ID {id_mobil} tidak dihapus")
                            else:
                                print("\nCoba lagi, Pilihan yang diinput tidak tersedia!")
                        else:
                            print(f"Data mobil dengan ID {id_mobil} tidak ditemukan")
                    elif userInput == 2:
                        break
                    else:
                        print("\nCoba lagi, Pilihan yang diinput tidak tersedia!")

            # EXIT
            elif pilihanFitur == 5:
                print("...Exit...")
                break

            # Other Options
            else:
                print("\nCoba lagi, Pilihan yang diinput tidak tersedia!")

    else:
        print("Username atau Password salah. Coba lagi.")