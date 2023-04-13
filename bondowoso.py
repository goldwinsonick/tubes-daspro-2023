# List untukmenyimpan jin yang sudah dipanggil
jin_list = [None for i in range(100)]

# Mekanisme fungsi kerja summonJin
def summonJin(iterasi:int=0) -> None:
    global jin_list

    # Menampilkan daftar jenis jin yang bisa dipanggil
    print("Jenis jin yang dapat dipanggil:")
    print("(1) Pengumpul - Bertugas mengumpulkan bahan bangunan")
    print("(2) Pembangun - Bertugas membangun candi")

    # Meminta pengguna memilih jenis jin yang ingin dipanggil
    jenis_jin = None
    while not (jenis_jin == 1 or jenis_jin == 2):
        jenis_jin = int(
            input("Masukkan nomor jenis jin yang ingin dipanggil: "))
        if not (jenis_jin == 1 or jenis_jin == 2):
            print("Tidak ada jenis jin bernomor {}!".format(jenis_jin))

    # Menampilkan pesan bahwa jin sedang dipilih
    if jenis_jin == 1:
        print("Memilih jin 'Pengumpul'.")
    else:
        print("Memilih jin 'Pembangun'.")

    # Meminta pengguna memasukkan username dan password untuk jin
    username = None
    password = None
    existing_usernames = [jin_list[i][0] for i in range(len(jin_list)) if jin_list[i] is not None and jin_list[i][0] is not None]

    # print(existing_usernames)
    while not username:
        username = input("Masukkan username jin: ")
        if username:
            exists = False
            for i in range(len(existing_usernames)):
                if existing_usernames[i] == username:
                    exists = True
                    break
            if exists:
                print("Username '{}' sudah diambil!".format(username))
                username = None
    while not password or len(password) < 5 or len(password) > 25:
        password = input("Masukkan password jin: ")
        if len(password) < 5 or len(password) > 25:
            print("Password panjangnya harus 5-25 karakter!")

    # Menampilkan pesan bahwa jin sedang dipanggil
    print("Mengumpulkan sesajen...")
    print("Menyerahkan sesajen...")
    print("Membacakan mantra...")

    # Menambahkan jin ke dalam daftar jin yang sudah dipanggil
    jin = [username, password, 'Pengumpul' if jenis_jin == 1 else 'Pembangun']
    jin_list[iterasi] = jin

    # Menampilkan pesan bahwa jin berhasil dipanggil
    print("Jin {} berhasil dipanggil!".format(username))


def summonJinLoop():
    global jin_list
    iterasi = 0
    while True:
        summonJin(iterasi)
        iterasi += 1
        # Cek apakah jumlah jin sudah maksimal (100)
        if iterasi >= len(jin_list):
            print(
                "Jumlah Jin telah maksimal! (100 jin). Bandung tidak dapat men-summon lebih dari itu")
            break
        while True:
            lanjut = input("Apakah kakanda ingin jin lagi? (y/n) ")
            if lanjut == 'y':
                break
            elif lanjut == 'n':
                print("Program summon jin dihentikan.")
                return
            else:
                print("Jawaban tidak valid. Masukkan 'y' atau 'n'.")


# summonJinLoop()
# print(jin_list)
