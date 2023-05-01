from typing import List, Union, Tuple
import rng, recursion, jin

# F03 - Summon Jin
# Fungsi ini hanya dapat diakses oleh bandung bondowoso untuk melakukan summon terhadap jin dengan validasi ppemeriksaan terhadap data jin_list dan deleted_jin
def summonjin(jin_list: List, users: List, deleted_jin:List, jin_max: int = 100) -> Tuple[List, List]:
    recursion.delay(0.8)
    # Find index yang mau diiisi sama jin baru
    index: int = recursion.findEmptyArrayIndex(jin_list)
    # Aksi ketika tidak ditemukan tempat untuk jin baru alias udah max
    if index == -99:
        print(f"\033[31mJumlah Jin telah maksimal! ({jin_max}). Bandung tidak dapat men-summon lebih dari itu\033[0m")
    # Aksi ketika ditemukan tempat kosong untuk jin baru
    else:
        # Menampilkan daftar jenis jin yang bisa dipanggil
        print("\033[34mJenis jin yang dapat dipanggil: \033[0m")
        print("\033[33m(1)\033[0m \033[36mPengumpul\033[0m - Bertugas mengumpulkan bahan bangunan")
        print("\033[33m(2)\033[0m \033[36mPembangun\033[0m - Bertugas membangun candi")

        jenis_jin: Union[None, str] = None
        # Meminta user memilih jenis jin yang ingin dipanggil
        # Aksi ketika input tidak sesuai
        while not (jenis_jin == "1" or jenis_jin == "2"):
            jenis_jin: str = (input("Masukkan nomor jenis jin yang ingin dipanggil: "))
            typeJenisJin: bool = recursion.isDigit(jenis_jin)
            # Aksi ketika input number tapi buakan 1 atau 2
            if (not (jenis_jin == "1" or jenis_jin == "2")) and typeJenisJin == True:
                print(f'\033[31mTidak ada jenis jin bernomor "{jenis_jin}" !\033[0m')
            # Aksi ketika input adalah string
            elif not typeJenisJin:
                print("\033[31mMasukkan nomor bukan huruf\033[0m")

        # Menampilkan pesan bahwa jin sedang dipilih
        if jenis_jin == "1":
            print("Memilih jin \033[36m'Pengumpul'\033[0m.")
        else:
            print("Memilih jin \033[36m'Pembangun'\033[0m.")

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
        # Aksi ketika sudah terdapat username yang sama pada list jin
            exists: bool = False
            for i in range(recursion.length(existing_usernames)):
                if existing_usernames[i] == username:
                    exists = True
                    break
            if exists:
                print(f'\033[31mUsername "{username}" sudah diambil!\033[0m')
                username = None
            # Aksi ketika sudah terdapat username yang sama pada jin yang sudah terhapus yang kemungkinan bisa diundo
            # Menyimpan username yang sudah ada dalam deleted_jin
            existing_usernames_deleted: List[str] = [None for i in range(recursion.length(deleted_jin)+1)]
            for i in range(recursion.length(deleted_jin)):
                existing_usernames_deleted[i] = deleted_jin[i][0]
                exists_deleted: bool = False
                for i in range(recursion.length(existing_usernames_deleted)):
                    if existing_usernames_deleted[i] == username:
                        exists_deleted = True
                        break
                if exists_deleted:
                    print(f'\033[31mUsername "{username}" sudah pernah anda PHK, silakan undo\033[0m')
                    username = None
        # Validasi password 5-25 character
        while not password or len(password) < 5 or len(password) > 25:
            password = input("Masukkan password jin: ")
            if len(password) < 5 or len(password) > 25:
                print("\033[33mPassword panjangnya harus 5-25 karakter!\033[0m")

        # Menampilkan pesan bahwa jin sedang dipanggil
        recursion.delay(1)
        print("\033[32mMengumpulkan sesajen...\033[0m")
        print("\033[32mMenyerahkan sesajen...\033[0m")
        print("\033[32mMembacakan mantra...\033[0m")
        recursion.delay(1)

        # Menambahkan jin ke dalam daftar jin yang sudah dipanggil
        jin: List = [username, password,'jin_pengumpul' if jenis_jin == "1" else 'jin_pembangun']
        jin_list[index]: List = jin
        # Menambahkan user baru akibat summonjin
        users = recursion.appends(users, jin)

        # Menampilkan pesan bahwa jin berhasil dipanggil
        print(f'\033[32mJin \033[36m"{username}"\033[0m \033[32mberhasil dipanggil!\033[0m')
    return jin_list, users, deleted_jin

# F04 - Hilangkan Jin 
# Fungsi ini hanya dapat diakses oleh bandung bondowoso untuk menghapus jin dari list berdasarkan username jin
def hilangkanjin( jin_list: List,users:List, candi_list: List, deleted_jin: List, deleted_candi: List) -> Tuple[List, List, List, List, List]:
    recursion.delay(0.8)
    # Inisiasi length arary sebelum dihapus
    lengthJin: int = recursion.length(jin_list)
    lengthCandi: int = recursion.length(candi_list)

    # Meminta user memasukkan username jin yang ingin dihapus
    username: str = input("Masukkan username jin yang ingin dihapus: ")
    # Mencari jin dengan username yang sesuai
    jin_index: Union[None, int] = None
    for i in range(lengthJin):
        if jin_list[i] != None and jin_list[i][0] == username:
            jin_index = i
            break

    recursion.delay(0.8)
    # Jika jin tidak ditemukan
    if jin_index == None:
        print("\033[31mTidak ada jin dengan username tersebut.\033[0m")
        return jin_list,users, candi_list, deleted_jin, deleted_candi

    # Meminta konfirmasi dari user untuk menghapus jin
    confirmation: Union[str, None] = None
    while not (confirmation == "Y" or confirmation == "N"):
        confirmation = input(f"Apakah anda yakin ingin menghapus jin dengan username \033[36m{username}\033[0m \033[33m(Y/N)\033[0m? ").upper()
        if not (confirmation == "Y" or confirmation == "N"):
            print("\033[31mPilihan yang dimasukkan tidak valid.\033[0m")

    # Jika user memilih untuk menghapus jin
    if confirmation == "Y":
        # Memasukkan data jin yang telah dihapus ke sebuah array untuk dapat diundo
        deleted_jin:List = recursion.appends(deleted_jin,jin_list[jin_index] )
        # Menghapus users jin dari list users
        users:List = recursion.removes(users, jin_list[jin_index], lengthJin+2)
        # Menghapus jin dari jin_list dengan mengubah nilai menjadi None bukan menghilangkan dari list
        jin_list[jin_index]: Union[List, None] = None
        recursion.shiftToEnd(jin_list, jin_index, lengthJin)
        recursion.delay(0.8)
        # Menghapus candi yang dibuat oleh jin tersebut dari candi_list
        for i in range(recursion.length(candi_list)):
            if candi_list[i] != None and candi_list[i][1] == username:
                # Menambahkan data candi yang telah dibuat jin yang terhapus ke deleted_candi
                deleted_candi:List = recursion.appends(deleted_candi,candi_list[i])
                # Menghapus candi dari candi_list
                candi_list:List = recursion.removes(candi_list, candi_list[i],lengthCandi)
        print("\033[32mJin telah berhasil dihapus dari alam gaib.\033[0m")
        return jin_list,users, candi_list, deleted_jin, deleted_candi
    else: # confirmation == "N":
        return jin_list,users, candi_list, deleted_jin, deleted_candi

# F05 - Hilangkan Jin 
# Fungsi ini hanya dapat diakses oleh bandung bondowoso untuk mengubah tipe jin dari pembangun menjadi pengumpul atau sebaliknya
def ubahtipejin(jin_list: List, users:List) -> Tuple[List, List]:
    recursion.delay(0.8)
    username: str = input("Masukkan username jin : ")
    recursion.delay(0.8)
    lengthJin: int = recursion.length(jin_list)
    # Mencari jin dengan username yang diinputkan
    found: bool = False
    for i in range(lengthJin):
        if jin_list[i] and jin_list[i][0] == username:
            tipe_baru: str = "jin_pembangun" if jin_list[i][2] == "jin_pengumpul" else "jin_pengumpul"
            confirm: str = input(f"Jin ini bertipe \033[36m“{recursion.outputtipejin(jin_list[i][2])}”\033[0m. Yakin ingin mengubah ke tipe \033[36m“{recursion.outputtipejin(tipe_baru)}”\033[0m \033[33m(Y/N)\033[0m? ")
            if confirm == "y" or confirm == "Y":
                recursion.delay(0.8)
                jin_list[i][2]: str = tipe_baru
                users[i+2][2]: str = tipe_baru
                print("Jin telah berhasil diubah.")
            found = True
    if not found:
        print("\033[31mTidak ada jin dengan username tersebut.\033[0m")
    return jin_list, users

# F08 - Batch Kumpul/Bangun
# Fungsi batchkumpul hanya dapat diakses oleh bandung bondowoso untuk memerintahkan semua jin pengumpul untuk mengumpulkan bahan bangunan
def batchkumpul(jin_list: List, bahan_bangunan: List) -> Tuple[int,List, List]:
    recursion.delay(0.8)
    # Cari jumlah jin pengumpul
    pengumpul_exist: int = 0
    total_terkumpul:List = [0, 0, 0]
    for i in range(recursion.length(jin_list)):
        if jin_list[i] != None:
            if jin_list[i][2] == "jin_pengumpul":
                pengumpul_exist += 1
    # Aksi ketika jin pengumpul tidak ada
    if pengumpul_exist <= 0:
        print("\033[31mKumpul gagal. Anda tidak punya jin pengumpul. Silahkan \033[33msummon\033[0m \033[31terlebih dahulu.\033[0m")
    # Aksi ketika jumlah jin pengumpul >=0
    else:
        print(f"\033[32mMengerahkan \033[36m{pengumpul_exist} jin\033[0m \033[32muntuk mengumpulkan bahan.\033[0m")
        # Memerintahkan semua jin pengumpul untuk mengumpulkan material
        for j in range(recursion.length(jin_list)):
            if jin_list[j] != None and jin_list[j][2] == "jin_pengumpul":
                    jin_list[j], bahan_bangunan, terkumpul = jin.kumpul(jin_list[j], bahan_bangunan, False)
                    for i in range(3):
                        total_terkumpul[i] += terkumpul[i]
        recursion.delay(0.5)
        print(f"\033[32mJin menemukan total \033[36m{total_terkumpul[0]} pasir, \033[36m{total_terkumpul[1]} batu, dan \033[36m{total_terkumpul[2]} air.\033[0m")
    return jin_list, bahan_bangunan

# F08 - Batch Kumpul/Bangun
# Fungsi batchbangun hanya dapat diakses oleh bandung bondowoso untuk memerintahkan kepada semua jin_pembangun untuk membangun candi dengan bahan yang tersedia
def batchbangun(bahan_bangunan: List, jin_list: List, candi_list: List, id: int) -> Tuple[List, List, List, int]:
    recursion.delay(0.8)
    harga_candi_total:List = [0, 0, 0]
    # Cek apakah ada jin pembangun dan hitung jumlah jin pembangun
    pembangun_exist:int = 0
    for i in range(recursion.length(jin_list)):
        if jin_list[i] != None:
            if jin_list[i][2] == 'jin_pembangun':
                pembangun_exist += 1
    # Aksi ketika kekurangan jin
    if pembangun_exist <= 0:
        print("\033[31mBangun gagal. Anda tidak punya jin pembangun. Silahkan \033[33msummon\033[0m \033[31terlebih dahulu.\033[0m")
    else:
        # Wadah untuk harga_candi hasil generate yang perlu dibuat oleh masing-masing jin
        temp_candi_generate = [None for i in range(recursion.length(jin_list))]
        for j in range(recursion.length(jin_list)):
            if jin_list[j] != None and jin_list[j][2] == "jin_pembangun":
                # Memasukkan hasil generate bahan_bangunan yang diperlukan masing-masing jin  pembangun saat pembuatan candi
                temp_candi_generate[j] = rng.rng(3, 1, 5)
                for h in range(3):
                    harga_candi_total[h] += temp_candi_generate[j][h]
        print(f"\033[32mMengerahkan \033[36m{pembangun_exist} jin\033[0m \033[32muntuk membangun candi dengan total bahan\033[0m \033[36m{harga_candi_total[0]} pasir, \033[36m{harga_candi_total[1]} batu, dan \033[36m{harga_candi_total[2]} air.\033[0m")

        # Cek apakah bahan bangunan mencukupi
        mencukupi:bool = True
        for i in range(3):
            if harga_candi_total[i] > bahan_bangunan[i]:
                mencukupi = False
                break

        # Jika mencukupi, bangun candi
        recursion.delay(0.5)
        if mencukupi:
            for s in range(recursion.length(jin_list)):
                if jin_list[s] != None and jin_list[s][2] == "jin_pembangun":
                    # mulai bangun candi
                    bahan_bangunan, jin_list[s], candi_list, harga, id = jin.bangun(bahan_bangunan, jin_list[s], candi_list, temp_candi_generate[s], False, id)
            print("\033[32mJin berhasil membangun total \033[36m", pembangun_exist, "candi.\033[0m\033[0m")
        # Jika tidak mencukupi, tampilkan pesan gagal
        else:
            print("\033[31mBangun gagal. Kurang", (harga_candi_total[0]-bahan_bangunan[0]) if (harga_candi_total[0]-bahan_bangunan[0]) > 0 else 0, "pasir,",(harga_candi_total[1]-bahan_bangunan[1]) if (harga_candi_total[1]-bahan_bangunan[1]) > 0 else 0, "batu, dan", (harga_candi_total[2]-bahan_bangunan[2]) if (harga_candi_total[2]-bahan_bangunan[2]) > 0 else 0, "air.\033[0m")
            print("\033[31mCandi yang terbangun 0\033[0m")

    return bahan_bangunan, jin_list, candi_list, id