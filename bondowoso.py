# List untukmenyimpan jin yang sudah dipanggil
from main import candi
jin_list = [None for i in range(3)]


def summonJin() -> None:
    import recursion
    global jin_list
    # Find index yang mau diiisi sama jin baru
    index = recursion.findEmptyArrayIndex(jin_list)
    # Menampilkan daftar jenis jin yang bisa dipanggil
    print("Jenis jin yang dapat dipanggil:")
    print("(1) Pengumpul - Bertugas mengumpulkan bahan bangunan")
    print("(2) Pembangun - Bertugas membangun candi")

    # Meminta pengguna memilih jenis jin yang ingin dipanggil
    jenis_jin = None
    while not (jenis_jin == "1" or jenis_jin == "2"):
        jenis_jin = (
            input("Masukkan nomor jenis jin yang ingin dipanggil: "))
        typeJenisJin = recursion.isDigit(jenis_jin)
        if (not (jenis_jin == "1" or jenis_jin == "2")) and typeJenisJin == True:
            print("Tidak ada jenis jin bernomor {}!".format(jenis_jin))
        else:
            print("Masukkan nomor bukan huruf")

    # Menampilkan pesan bahwa jin sedang dipilih
    if jenis_jin == "1":
        print("Memilih jin 'Pengumpul'.")
    else:
        print("Memilih jin 'Pembangun'.")

    # Meminta pengguna memasukkan username dan password untuk jin
    username = None
    password = None
    existing_usernames = [jin_list[i][0] for i in range(
        len(jin_list)) if jin_list[i] is not None and jin_list[i][0] is not None]

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
    jin = [username, password, 'Pengumpul' if jenis_jin == "1" else 'Pembangun']
    jin_list[index] = jin

    # Menampilkan pesan bahwa jin berhasil dipanggil
    # print("Jin {} berhasil dipanggil!".format(username))


def summonJinLoop():
    import recursion
    global jin_list
    checking_index = recursion.findEmptyArrayIndex(jin_list)
    while checking_index != -99:
        summonJin()
        # Cek apakah jumlah jin sudah maksimal (100)
        checkingIndexLagi = recursion.findEmptyArrayIndex(jin_list)
        if checkingIndexLagi == -99:
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
jin_list = [
    ["jin1", "testing1", "Pembangun"],
    ["jin2", "testing2", "Pembangun"],
    ["jin3", "testing3", "Pembangun"],
    ["jin4", "testing4", "Pengumpul"],
    ["jin5", "testing5", "Pengumpul"],
    None
]

candi_list = candi


def hapusJin() -> None:
    global jin_list, candi_list
    import recursion

    length_jin_list = recursion.length(jin_list)
    length_candi_list = recursion.length(candi_list)
    # Meminta pengguna memasukkan username jin yang ingin dihapus
    username = input("Masukkan username jin yang ingin dihapus: ")

    # Mencari jin dengan username yang sesuai
    jin_index = None
    for i in range(length_jin_list):
        if jin_list[i] != None and jin_list[i][0] == username:
            jin_index = i
            break

    # Jika jin tidak ditemukan
    if jin_index is None:
        print("Tidak ada jin dengan username tersebut.")
        return

    # Meminta konfirmasi dari pengguna untuk menghapus jin
    confirmation = None
    while not (confirmation == "Y" or confirmation == "N"):
        confirmation = input(
            "Apakah anda yakin ingin menghapus jin dengan username {} (Y/N)? ".format(username)).upper()
        if not (confirmation == "Y" or confirmation == "N"):
            print("Pilihan yang dimasukkan tidak valid.")

    # Jika pengguna memilih untuk menghapus jin
    if confirmation == "Y":
        # Menghapus jin dari jin_list
        jin_list[jin_index] = None
        recursion.shiftToEnd(jin_list, jin_index, length_jin_list)

        # Menghapus candi yang dibuat oleh jin tersebut dari candi_list
        for i in range(recursion.length(candi_list)):
            if candi_list[i] != None and candi_list[i][1] == username:
                candi_list[i] = None
                recursion.shiftToEnd(candi_list, i, length_candi_list)

        print("Jin telah berhasil dihapus dari alam gaib.")


hapusJin()
print(jin_list)
print(candi_list)
