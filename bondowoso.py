import recursion
jin_list = []  # List untuk menyimpan jin yang sudah dipanggil

def summonJin() -> None:
    global jin_list

    # Cek apakah jumlah jin sudah maksimal (100)
    if recursion.length(jin_list) >= 100:
        print("Jumlah Jin telah maksimal! (100 jin). Bandung tidak dapat men-summon lebih dari itu")
        return

    # Menampilkan daftar jenis jin yang bisa dipanggil
    print("Jenis jin yang dapat dipanggil:")
    print("(1) Pengumpul - Bertugas mengumpulkan bahan bangunan")
    print("(2) Pembangun - Bertugas membangun candi")

    # Meminta pengguna memilih jenis jin yang ingin dipanggil
    jenis_jin = None
    while jenis_jin not in [1, 2]:
        jenis_jin = int(
            input("Masukkan nomor jenis jin yang ingin dipanggil: "))
        if jenis_jin not in [1, 2]:
            print("Tidak ada jenis jin bernomor {}!".format(jenis_jin))

    # Menampilkan pesan bahwa jin sedang dipilih
    if jenis_jin == 1:
        print("Memilih jin 'Pengumpul'.")
    else:
        print("Memilih jin 'Pembangun'.")

    # Meminta pengguna memasukkan username dan password untuk jin
    username = None
    password = None
    while not username or username in [jin['username'] for jin in jin_list]:
        username = input("Masukkan username jin: ")
        if username in [jin['username'] for jin in jin_list]:
            print("Username '{}' sudah diambil!".format(username))
    while not password or len(password) < 5 or len(password) > 25:
        password = input("Masukkan password jin: ")
        if len(password) < 5 or len(password) > 25:
            print("Password panjangnya harus 5-25 karakter!")

    # Menampilkan pesan bahwa jin sedang dipanggil
    print("Mengumpulkan sesajen...")
    print("Menyerahkan sesajen...")
    print("Membacakan mantra...")

    # Menambahkan jin ke dalam daftar jin yang sudah dipanggil
    jin = {
        'username': username,
        'password': password,
        'jenis': 'Pengumpul' if jenis_jin == 1 else 'Pembangun'
    }
    jin_list += [jin]

    # Menampilkan pesan bahwa jin berhasil dipanggil
    print("Jin {} berhasil dipanggil!".format(username))

while True :
    summonJin()
    print(jin_list)
    summonJin()
    print(jin_list)
