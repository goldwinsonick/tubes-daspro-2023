# List untuk menyimpan jin yang sudah dipanggil
from typing import List, Union, Tuple
import rng


def summonjin(jin_list: List, users: List, jin_max: int = 100) -> Tuple[List, List]:
    import recursion
    # Find index yang mau diiisi sama jin baru
    index: int = recursion.findEmptyArrayIndex(jin_list)
    # Aksi ketika tidak ditemukan tempat untuk jin baru alias udah max
    if index == -99:
        print(f"Jumlah Jin telah maksimal! ({jin_max}). Bandung tidak dapat men-summon lebih dari itu")
    # Aksi ketika ditemukan tempat kosong untuk jin baru
    else:
        # Menampilkan daftar jenis jin yang bisa dipanggil
        print("Jenis jin yang dapat dipanggil:")
        print("(1) Pengumpul - Bertugas mengumpulkan bahan bangunan")
        print("(2) Pembangun - Bertugas membangun candi")

        jenis_jin: Union[None, str] = None
        # Meminta user memilih jenis jin yang ingin dipanggil
        # Aksi ketika input tidak sesuai
        while not (jenis_jin == "1" or jenis_jin == "2"):
            jenis_jin: str = (input("Masukkan nomor jenis jin yang ingin dipanggil: "))
            typeJenisJin: bool = recursion.isDigit(jenis_jin)
            # Aksi ketika input number tapi buakan 1 atau 2
            if (not (jenis_jin == "1" or jenis_jin == "2")) and typeJenisJin == True:
                print(f'Tidak ada jenis jin bernomor "{jenis_jin}" !')
            # Aksi ketika input adalah string
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
        existing_usernames: List[str] = [None for i in range(recursion.length(jin_list)+1)]
        for i in range(recursion.length(jin_list)):
            existing_usernames[i] = jin_list[i][0]

        # Aksi untuk input username
        while not username:
            username = input("Masukkan username jin: ")
        # Aksi ketika sudah terdapat username yang sama pada list
            exists: bool = False
            for i in range(recursion.length(existing_usernames)):
                if existing_usernames[i] == username:
                    exists = True
                    break
            if exists:
                print(f'Username "{username}" sudah diambil!')
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
        jin: List = [username, password,'jin_pengumpul' if jenis_jin == "1" else 'jin_pembangun']
        jin_list[index]: List = jin
        # Menambahkan user baru akibat summonjin
        users = recursion.appends(users, jin)

        # Menampilkan pesan bahwa jin berhasil dipanggil
        print(f'Jin "{username}" berhasil dipanggil!')
    return jin_list, users


# users = [['Bondowoso', 'cintaroro', 'bandung_bondowoso'], ['Roro', 'gasukabondo', 'roro_jonggransasdg'], None]
# Skema pengggunaan fungsi summonJin
# jin_list = [None for i in range(101)]
# jin_list, users = summonjin(jin_list, users, 100)
# print(jin_list, users)
# jin_list, users = summonjin(jin_list, users, 100)
# jin_list, users = summonjin(jin_list, users, 100)
# print(jin_list, users)

# jin_list: List = [
#     ["jin1", "testing1", "jin_pembangun"],
#     ["jin2", "testing2", "jin_pembangun"],
#     ["jin3", "testing3", "jin_pembangun"],
#     ["jin4", "testing4", "jin_pengumpul"],
#     ["jin5", "testing5", "jin_pengumpul"],
#     None
# ]
# users: List = [
#     ['Bondowoso', 'cintaroro', 'bandung_bondowoso'],
#     ['Roro', 'gasukabondo', 'roro_jonggransasdg'],
#     ["jin1", "testing1", "jin_pembangun"],
#     ["jin2", "testing2", "jin_pembangun"],
#     ["jin3", "testing3", "jin_pembangun"],
#     ["jin4", "testing4", "jin_pengumpul"],
#     ["jin5", "testing5", "jin_pengumpul"],
#     None
# ]
# candi_list: List = [[1, "jin1", 2, 4, 3], [2, "jin2", 2, 4, 3], None]
# deleted_jin: List = [None for i in range(1)]
# deleted_candi: List = [None for i in range(1)]


def hilangkanjin( jin_list: List,users:List, candi_list: List, deleted_jin: List, deleted_candi: List) -> Tuple[List, List, List, List]:
    from typing import Union, List
    import recursion
    # inisiasi length arary sebelum dihapus
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
        return jin_list,users, candi_list, deleted_jin, deleted_candi

    # Meminta konfirmasi dari user untuk menghapus jin
    confirmation: Union[str, None] = None
    while not (confirmation == "Y" or confirmation == "N"):
        confirmation = input(f"Apakah anda yakin ingin menghapus jin dengan username {username} (Y/N)? ").upper()
        if not (confirmation == "Y" or confirmation == "N"):
            print("Pilihan yang dimasukkan tidak valid.")

    # Jika user memilih untuk menghapus jin
    if confirmation == "Y":
        # Memasukkan data jin yang telah dihapus ke sebuah array untuk dapat diundo
        deleted_jin:List = recursion.appends(deleted_jin,jin_list[jin_index] )
        # Menghapus users jin dari list users
        users:List = recursion.removes(users, jin_list[jin_index], length_jin_list+2)
        # Menghapus jin dari jin_list dengan mengubah nilai menjadi None bukan menghilangkan dari list
        jin_list[jin_index]: Union[List, None] = None
        recursion.shiftToEnd(jin_list, jin_index, length_jin_list)

        # Menghapus candi yang dibuat oleh jin tersebut dari candi_list
        for i in range(recursion.length(candi_list)):
            if candi_list[i] != None and candi_list[i][1] == username:
                # Menambahkan data candi yang telah dibuat jin yang terhapus ke deleted_candi
                deleted_candi:List = recursion.appends(deleted_candi,candi_list[i])
                # Menghapus candi dari candi_list
                candi_list:List = recursion.removes(candi_list, candi_list[i],length_candi_list)
        print("Jin telah berhasil dihapus dari alam gaib.")
        return jin_list,users, candi_list, deleted_jin, deleted_candi
    elif confirmation == "N":
        return jin_list,users, candi_list, deleted_jin, deleted_candi


# skema penggunaan
# jin_list, users,candi_list, deleted_jin, deleted_candi = hilangkanjin(
#     jin_list,users, candi_list, deleted_jin, deleted_candi)
# jin_list,users, candi_list, deleted_jin, deleted_candi = hilangkanjin(
#     jin_list,users, candi_list, deleted_jin, deleted_candi)
# print("jin:", jin_list)
# print("deleted jin:", deleted_jin)
# print("candi:", candi_list)
# print("deleted candi:", deleted_candi)
# print(users)


def ubahtipejin(jin_list: List, users:List) -> Tuple[List, List]:
    import recursion
    username: str = input("Masukkan username jin : ")
    length_jin_list: int = recursion.length(jin_list)
    # Mencari jin dengan username yang diinputkan
    found: bool = False
    for i in range(length_jin_list):
        if jin_list[i] and jin_list[i][0] == username:
            tipe_baru: str = "jin_pembangun" if jin_list[i][2] == "jin_pengumpul" else "jin_pengumpul"
            confirm: str = input(f"Jin ini bertipe “{recursion.outputtipejin(jin_list[i][2])}”. Yakin ingin mengubah ke tipe “{recursion.outputtipejin(tipe_baru)}” (Y/N)? ")
            if confirm == "y" or confirm == "Y":
                jin_list[i][2]: str = tipe_baru
                users[i+2][2]: str = tipe_baru
                print("Jin telah berhasil diubah.")
            found = True
    if not found:
        print("Tidak ada jin dengan username tersebut.")
    return jin_list, users

# jin_list, users=ubahtipejin(jin_list, users)
# print(jin_list, users)

# jin_list = [["jin1", "laslkdujalkd", "jin_pembangun"], ["jin2", "laslkdujalkd",
#                                                         "jin_pengumpul"], ["jin3", "laslkdujalkd",
#                                                                            "jin_pengumpul"],  ["jin4", "laslkdujalkd",
#                                                                                                "jin_pengumpul"], ["jin5cls", "laslkdujalkd", "jin_pembangun"], None]
# bahan_bangunan = [20, 20, 21]
# candi_list = [None for i in range(1)]
# id =0

# jin_list = [["jin1", "laslkdujalkd", "jin_pembangun"], ["jin2", "laslkdujalkd",
#                                                         "jin_pengumpul"], ["jin3", "laslkdujalkd",
#                                                                            "jin_pengumpul"],  ["jin4", "laslkdujalkd",
#                                                                                                "jin_pengumpul"], ["jin5cls", "laslkdujalkd", "jin_pembangun"], None]
# bahan_bangunan = [20, 20, 21]
# candi_list = [None for i in range(1)]
# id = 0


def batchkumpul(jin_list: List, bahan_bangunan: List) -> Tuple[int,List, List]:
    import recursion
    import jin
    # Cari jumlah jin pengumpul
    pengumpul_exist: int = 0
    total_terkumpul:List = [0, 0, 0]
    for i in range(recursion.length(jin_list)):
        if jin_list[i] != None:
            if jin_list[i][2] == "jin_pengumpul":
                pengumpul_exist += 1
    # Aksi ketika jin pengumpul tidak ada
    if pengumpul_exist <= 0:
        print("Kumpul gagal. Anda tidak punya jin pengumpul. Silahkan summon terlebih dahulu.")
    # Aksi ketika jumlah jin pengumpul >=0
    else:
        print(f"Mengerahkan {pengumpul_exist} jin untuk mengumpulkan bahan.")
        # Memerintahkan semua jin pengumpul untuk mengumpulkan material
        for j in range(recursion.length(jin_list)):
            if jin_list[j] != None and jin_list[j][2] == "jin_pengumpul":
                    jin_list[j], bahan_bangunan, terkumpul = jin.kumpul(jin_list[j], bahan_bangunan, False)
                    for i in range(3):
                        total_terkumpul[i] += terkumpul[i]
        print(f"Jin menemukan total {total_terkumpul[0]} pasir, {total_terkumpul[1]} batu, dan {total_terkumpul[2]} air.")
    return jin_list, bahan_bangunan
# jin_list, bahan_bangunan=batchkumpul(jin_list, bahan_bangunan)
# print(jin_list, bahan_bangunan)

def batchbangun(bahan_bangunan: List, jin_list: List, candi_list: List, id: int) -> Tuple[List, List, List, int]:
    import recursion
    import jin
    harga_candi_total:List = [0, 0, 0]
    # Cek apakah ada jin pembangun dan hitung jumlah jin pembangun
    pembangun_exist:int = 0
    for i in range(recursion.length(jin_list)):
        if jin_list[i] != None:
            if jin_list[i][2] == 'jin_pembangun':
                pembangun_exist += 1
    # Aksi ketika kekurangan jin
    if pembangun_exist <= 0:
        print("Bangun gagal. Anda tidak punya jin pembangun. Silahkan summon terlebih dahulu.")
    else:
        # Wadah untuk harga_candi hasil generate yang perlu dibuat oleh masing-masing jin
        temp_candi_generate = [None for i in range(recursion.length(jin_list))]
        print(f"Mengerahkan {pembangun_exist} jin untuk membangun candi dengan total bahan {bahan_bangunan[0]} pasir, {bahan_bangunan[1]} batu, dan {bahan_bangunan[2]} air.")
        for j in range(recursion.length(jin_list)):
            if jin_list[j] != None and jin_list[j][2] == "jin_pembangun":
                # Memasukkan hasil generate bahan_bangunan yang diperlukan masing-masing jin  pembangun saat pembuatan candi
                temp_candi_generate[j] = rng.rng(3, 1, 5)
                for h in range(3):
                    harga_candi_total[h] += temp_candi_generate[j][h]

        # Cek apakah bahan bangunan mencukupi
        mencukupi:bool = True
        for i in range(3):
            if harga_candi_total[i] > bahan_bangunan[i]:
                mencukupi = False
                break

        # Jika mencukupi, bangun candi
        if mencukupi:
            for s in range(recursion.length(jin_list)):
                if jin_list[s] != None and jin_list[s][2] == "jin_pembangun":
                    # mulai bangun candi
                    bahan_bangunan, jin_list[s], candi_list, harga, id = jin.bangun(bahan_bangunan, jin_list[s], candi_list, temp_candi_generate[s], False, id)
            print("Jin berhasil membangun total", pembangun_exist, "candi.")
        # Jika tidak mencukupi, tampilkan pesan gagal
        else:
            print("Bangun gagal. Kurang", (harga_candi_total[0]-bahan_bangunan[0]) if (harga_candi_total[0]-bahan_bangunan[0]) > 0 else 0, "pasir,",(harga_candi_total[1]-bahan_bangunan[1]) if (harga_candi_total[1]-bahan_bangunan[1]) > 0 else 0, "batu, dan", (harga_candi_total[2]-bahan_bangunan[2]) if (harga_candi_total[2]-bahan_bangunan[2]) > 0 else 0, "air.")
            print("Candi yang terbangun 0")

    return bahan_bangunan, jin_list, candi_list, id
# skema penggunaan fungsi
# bahan_bangunan, jin_list, candi_list, id = batchbangun(bahan_bangunan, jin_list, candi_list, id)
# print(bahan_bangunan, candi_list)
