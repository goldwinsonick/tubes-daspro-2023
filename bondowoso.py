# List untuk menyimpan jin yang sudah dipanggil
from typing import List, Union, Tuple


def summonJin(jin_list: List[List[str]], users:List, jin_max: int = 100) -> List[List[str]]:
    from typing import Union, List
    import recursion

    # Find index yang mau diiisi sama jin baru
    index: int = recursion.findEmptyArrayIndex(jin_list)
    # Aksi ketika tidak ditemukan tempat untuk jin baru alias udah max
    if index == -99:
        print(
            "Jumlah Jin telah maksimal! ({}). Bandung tidak dapat men-summon lebih dari itu".format(jin_max))
    # Aksi ketika ditemukan tempat kosong untuk jin baru
    else:
        # Menampilkan daftar jenis jin yang bisa dipanggil
        print("Jenis jin yang dapat dipanggil:")
        print("(1) Pengumpul - Bertugas mengumpulkan bahan bangunan")
        print("(2) Pembangun - Bertugas membangun candi")

        # Meminta user memilih jenis jin yang ingin dipanggil
        jenis_jin: Union[None, int] = None
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

        # Meminta user memasukkan username dan password untuk jin
        username: Union[str, None] = None
        password: Union[str, None] = None
        # Menyimpan username yang sudah ada dalam jin_list
        existing_usernames: List[str] = [None for i in range(
            recursion.length(jin_list)+1)]
        for i in range(recursion.length(jin_list)):
            existing_usernames[i] = jin_list[i][0]

        # Aksi untuk input username
        while not username:
            username = input("Masukkan username jin: ")
        # Aksi ketika sudah terdapat username yang sama pada list
            if username:
                exists: bool = False
                for i in range(recursion.length(existing_usernames)):
                    if existing_usernames[i] == username:
                        exists = True
                        break
                if exists:
                    print("Username '{}' sudah diambil!".format(username))
                    username = None
        # Validasi password 5-25 character
        while not password or len(password) < 5 or len(password) > 25:
            password = input("Masukkan password jin: ")
            if len(password) < 5 or len(password) > 25:
                print("Password panjangnya harus 5-25 karakter!")

        # Menampilkan pesan bahwa jin sedang dipanggil
        print("Mengumpulkan sesajen...")
        print("Menyerahkan sesajen...")
        print("Membacakan mantra...")

        # Menambahkan jin ke dalam daftar jin yang sudah dipanggil
        jin: List[List[str]] = [username, password,
                                'jin_pengumpul' if jenis_jin == "1" else 'jin_pembangun']
        jin_list[index]: List[str] = jin
        users[index+2]:List[str] = jin

        # Menampilkan pesan bahwa jin berhasil dipanggil
        print("Jin {} berhasil dipanggil!".format(username))
    return jin_list, users

# Skema pengggunaan fungsi summonJin
# jin_list=[None for i in range(101)]
# jin_list =summonJin(jin_list, 100)
# jin_list =summonJin(jin_list, 100)
# jin_list =summonJin(jin_list, 100)
# print(jin_list)

# jin_list: List = [
#     ["jin1", "testing1", "Pembangun"],
#     ["jin2", "testing2", "Pembangun"],
#     ["jin3", "testing3", "Pembangun"],
#     ["jin4", "testing4", "Pengumpul"],
#     ["jin5", "testing5", "Pengumpul"],
#     None
# ]
# candi_list: List = [[1, "jin1", 2, 4, 3], [2, "jin2", 2, 4, 3], None]
# deleted_jin: List = [None for i in range(1)]
# deleted_candi: List = [None for i in range(1)]

def hapusJin(jin_list: List, candi_list: List, deleted_jin: List, deleted_candi: List, users) -> Union[List, Tuple[List, List, List, List]]:
    from typing import Union, List
    import recursion

    length_jin_list: int = recursion.length(jin_list)
    length_candi_list: int = recursion.length(candi_list)
    # Meminta user memasukkan username jin yang ingin dihapus
    username: str = input("Masukkan username jin yang ingin dihapus: ")

    # Mencari jin dengan username yang sesuai
    jin_index: Union[None, int] = None
    for i in range(length_jin_list):
        if jin_list[i] != None and jin_list[i][0] == username:
            jin_index = i
            break

    # Jika jin tidak ditemukan
    if jin_index == None:
        print("Tidak ada jin dengan username tersebut.")
        return jin_list, candi_list, deleted_jin, deleted_candi, users

    # Meminta konfirmasi dari user untuk menghapus jin
    confirmation: Union[str, None] = None
    while not (confirmation == "Y" or confirmation == "N"):
        confirmation = input(
            "Apakah anda yakin ingin menghapus jin dengan username {} (Y/N)? ".format(username)).upper()
        if not (confirmation == "Y" or confirmation == "N"):
            print("Pilihan yang dimasukkan tidak valid.")

    # Jika user memilih untuk menghapus jin
    if confirmation == "Y":
        # Menyiapkan skema untuk menambahkan 1 array
        temp_list_deleted_jin = [None for i in range(
            recursion.length(deleted_jin)+2)]
        temp_list_deleted_candi = [None for i in range(
            recursion.length(deleted_candi)+2)]

        # copy data dari deleted jin sebelumnya
        for i in range(recursion.length(deleted_jin)):
            temp_list_deleted_jin[i] = deleted_jin[i]

        # Copy data baru dengan mark baru ke deleted sebelumnya
        empty_index_array_temp_jin = recursion.findEmptyArrayIndex(
            temp_list_deleted_jin)
        temp_list_deleted_jin[empty_index_array_temp_jin] = jin_list[jin_index]
        deleted_jin = temp_list_deleted_jin

        # Menghapus jin dari jin_list
        jin_list[jin_index]: Union[List, None] = None
        users[jin_index+2]: Union[List, None] = None
        recursion.shiftToEnd(jin_list, jin_index, length_jin_list)
        recursion.shiftToEnd(users, jin_index+2, length_jin_list+2)

        # Menghapus candi yang dibuat oleh jin tersebut dari candi_list
        for i in range(recursion.length(candi_list)):
            if candi_list[i] != None and candi_list[i][1] == username:
                # copy data dari deleted candi sebelumnya
                for j in range(recursion.length(deleted_candi)):
                    temp_list_deleted_candi[j] = deleted_candi[j]

                # Copy data dengan mark baru ke deleted sebelumnya
                empty_index_array_temp_candi = recursion.findEmptyArrayIndex(
                    temp_list_deleted_candi)
                temp_list_deleted_candi[empty_index_array_temp_candi] = candi_list[i]
                deleted_candi = temp_list_deleted_candi
                # Menghapus candi dari candi_list
                # copy data dengan mengurangi 1 index dengan tanpa menyertakan candi_list[i]
                candi_clear = [None for i in range(length_candi_list)]
                for k in range(length_candi_list):
                    if candi_list[k] != candi_list[i]:
                        candi_clear[k] = candi_list[k]

                candi_list = candi_clear

                recursion.shiftToEnd(candi_list, i, length_candi_list)
        print("Jin telah berhasil dihapus dari alam gaib.")
        return jin_list, candi_list, deleted_jin, deleted_candi, users
    elif confirmation == "N":
        return jin_list, candi_list, deleted_jin, deleted_candi, users


# skema penggunaan
# jin_list, candi_list, deleted_jin, deleted_candi = hapusJin(
#     jin_list, candi_list, deleted_jin, deleted_candi)
# jin_list, candi_list, deleted_jin, deleted_candi = hapusJin(
#     jin_list, candi_list, deleted_jin, deleted_candi)
# print("jin:", jin_list)
# print("deleted jin:", deleted_jin)
# print("candi:", candi_list)
# print("deleted candi:", deleted_candi)


def ubahJin(jin_list: List[List[str]], users):
    import recursion
    username: str = input("Masukkan username jin : ")
    length_jin_list: int = recursion.length(jin_list)
    # Mencari jin dengan username yang diinputkan
    for i in range(length_jin_list):
        if jin_list[i] and jin_list[i][0] == username:
            tipe_lama: str = jin_list[i][2]
            tipe_baru: str = "jin_pembangun" if tipe_lama == "jin_pengumpul" else "jin_pengumpul"
            confirm: str = input(
                f"Jin ini bertipe “{tipe_lama}”. Yakin ingin mengubah ke tipe “{tipe_baru}” (Y/N)? ")
            if confirm.lower() == "y":
                jin_list[i][2]: str = tipe_baru
                users[i+2][2]: str = tipe_baru
                print("Jin telah berhasil diubah.")
    print("Tidak ada jin dengan username tersebut.")
    return jin_list, users

# ubahJin(jin_list)
# print(jin_list)
