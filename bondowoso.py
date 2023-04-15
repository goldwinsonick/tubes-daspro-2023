# List untuk menyimpan jin yang sudah dipanggil
from main import candi
jin_list = [None for i in range(3)]

def summonJin() -> None:
    from typing import Union, List
    import recursion
    global jin_list
    # Find index yang mau diiisi sama jin baru
    index: int = recursion.findEmptyArrayIndex(jin_list)
    # Menampilkan daftar jenis jin yang bisa dipanggil
    print("Jenis jin yang dapat dipanggil:")
    print("(1) Pengumpul - Bertugas mengumpulkan bahan bangunan")
    print("(2) Pembangun - Bertugas membangun candi")

    # Meminta pengguna memilih jenis jin yang ingin dipanggil
    jenis_jin: Union[None,int] = None
    while not (jenis_jin == "1" or jenis_jin == "2"):
        jenis_jin: str = (
            input("Masukkan nomor jenis jin yang ingin dipanggil: "))
        typeJenisJin: bool = recursion.isDigit(jenis_jin)
        if (not (jenis_jin == "1" or jenis_jin == "2")) and typeJenisJin == True:
            print("Tidak ada jenis jin bernomor {}!".format(jenis_jin))
        elif not typeJenisJin:
            print("Masukkan nomor bukan huruf")

    # Menampilkan pesan bahwa jin sedang dipilih
    if jenis_jin == "1":
        print("Memilih jin 'Pengumpul'.")
    else:
        print("Memilih jin 'Pembangun'.")

    # Meminta pengguna memasukkan username dan password untuk jin
    username: Union[str, None] = None
    password: Union[str, None] = None
    existing_usernames:List[str] = [jin_list[i][0] for i in range(
        recursion.length(jin_list)) if jin_list[i] != None and jin_list[i][0] != None]

    # print(existing_usernames)
    while not username:
        username = input("Masukkan username jin: ")
        if username:
            exists:bool = False
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
    jin:List[List[str]] = [username, password, 'Pengumpul' if jenis_jin == "1" else 'Pembangun']
    jin_list[index]:List[str] = jin

    # Menampilkan pesan bahwa jin berhasil dipanggil
    # print("Jin {} berhasil dipanggil!".format(username))


def summonJinLoop() -> None:
    import recursion
    global jin_list
    checking_index:int = recursion.findEmptyArrayIndex(jin_list)
    while checking_index != -99:
        summonJin()
        # Cek apakah jumlah jin sudah maksimal (100)
        checkingIndexLagi:int = recursion.findEmptyArrayIndex(jin_list)
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
    from typing import Union, List
    global jin_list, candi_list
    import recursion

    length_jin_list:int = recursion.length(jin_list)
    length_candi_list:int = recursion.length(candi_list)
    # Meminta pengguna memasukkan username jin yang ingin dihapus
    username:str = input("Masukkan username jin yang ingin dihapus: ")

    # Mencari jin dengan username yang sesuai
    jin_index:Union[None, int] = None
    for i in range(length_jin_list):
        if jin_list[i] != None and jin_list[i][0] == username:
            jin_index = i
            break

    # Jika jin tidak ditemukan
    if jin_index == None:
        print("Tidak ada jin dengan username tersebut.")
        return

    # Meminta konfirmasi dari pengguna untuk menghapus jin
    confirmation:Union[str,None] = None
    while not (confirmation == "Y" or confirmation == "N"):
        confirmation = input(
            "Apakah anda yakin ingin menghapus jin dengan username {} (Y/N)? ".format(username)).upper()
        if not (confirmation == "Y" or confirmation == "N"):
            print("Pilihan yang dimasukkan tidak valid.")

    # Jika pengguna memilih untuk menghapus jin
    if confirmation == "Y":
        # Menghapus jin dari jin_list
        jin_list[jin_index]:Union[List, None] = None
        recursion.shiftToEnd(jin_list, jin_index, length_jin_list)

        # Menghapus candi yang dibuat oleh jin tersebut dari candi_list
        for i in range(recursion.length(candi_list)):
            if candi_list[i] != None and candi_list[i][1] == username:
                candi_list[i] = None
                recursion.shiftToEnd(candi_list, i, length_candi_list)

        print("Jin telah berhasil dihapus dari alam gaib.")
# hapusJin()
# print(jin_list)
# print(candi_list)

def ubahJin() -> None:
    global jin_list
    import recursion
    username:str = input("Masukkan username jin : ")
    length_jin_list:int = recursion.length(jin_list)
    # Mencari jin dengan username yang diinputkan
    for i in range(length_jin_list):
        if jin_list[i] and jin_list[i][0] == username:
            tipe_lama:str = jin_list[i][2]
            tipe_baru:str = "Pembangun" if tipe_lama == "Pengumpul" else "Pengumpul"
            confirm:str = input(
                f"Jin ini bertipe “{tipe_lama}”. Yakin ingin mengubah ke tipe “{tipe_baru}” (Y/N)? ")
            if confirm.lower() == "y":
                jin_list[i][2]:str = tipe_baru
                print("Jin telah berhasil diubah.")
            return
    print("Tidak ada jin dengan username tersebut.")

# ubahJin()
# print(jin_list)