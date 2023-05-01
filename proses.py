
from typing import Union, List, Tuple
import argparse
import os
import recursion

# F13 - Load
# Fungsi load untuk mengambil data dari csv pertama kali
def load(users: List, candi: List, material: List, bahan_bangunan: List, jin_list: List) -> Tuple[List, List, List]:
    # Parsing argumen
    parser: argparse.ArgumentParser = argparse.ArgumentParser()
    parser.add_argument("nama_folder", type=str, nargs="?", const="", help="Usage: python main.py <nama_folder>")
    args: argparse.Namespace = parser.parse_args()
    directory: Union[None, str] = args.nama_folder
    # Aksi ketika tidak ada nama file yang diberikan
    if directory is None:
        print("\033[31mTidak ada nama folder yang diberikan\033[0m")
        print("\033[33mUsage: python main.py <nama_folder>\033[0m")
        exit(1)

    parents_path = os.getcwd() + "\\" + directory
    # Validasi ketika ditemukan nama folder terkait
    if os.path.isdir(parents_path):
        print("Loading...")
        recursion.clear()
        # Mekanisme convert data users dari csv ke array dengan mark
        users = recursion.read_csv(parents_path + "\\user.csv")
        # Menyalin data jin dari users ke jin_list
        if recursion.length(users) > 2:
            for i in range(2, recursion.length(users)):
                jin_list[i-2] = users[i]
        # Mekanisme convert data candi dari csv ke array dengan mark
        candi = recursion.read_csv(parents_path + "\\candi.csv")
        for i in range(recursion.length(candi)):
            for j in range(5):
                if j != 1:
                    candi[i][j] = int(candi[i][j])
        # Mekanisme convert data bahan bangunan dari csv ke array dengan mark
        material = recursion.read_csv(parents_path + "\\bahan_bangunan.csv")
        # Menyesuaikan dengan mekanisme data yang telah kita bentuk pada awal untuk memudahkan operasi bahan_bangunan
        for i in range(3):
            bahan_bangunan[i] = int(material[i][2])
        # bahan_bangunan = [<pasir>,<batu>,<air>]
        print("\033[35mSelamat datang di “Manajerial Candi”\033[0m")

        # Aksi ketika nama folder yang dicari tidak ada
    else:
        print(f'\033[31mFolder "{directory}" tidak ditemukan.\033[0m')
        exit(1)
    return users, candi, material, bahan_bangunan, jin_list

# F14 - Save
# Fungsi save untuk menyimpan perubahan yang dilakukan dalam program ke data csv baru
def save(user: List = [None], candi: List = [None], bahan_bangunan: List = [None], material: List = [None]) -> None:
    recursion.delay(0.5)
    folder: str = input("Masukkan nama folder: ")
    abs_path: str = os.getcwd() + "\save\\" + folder
    # Mekanisme simpan dalam folder spesifik berdasarkan input user
    folder_path: str = os.path.join("save", folder)
    print("Saving...")
    recursion.delay(1)
    # Validasi apakah folder save sudah ada
    if not os.path.exists('save'):
        print(f"Membuat folder save...")
        os.makedirs('save')
    # Validasi apakah subfolder nama_folder ada didalam save
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print(f"Membuat folder {folder_path}...")
    print("\033[32mBerhasil menyimpan data di folder " + folder_path + "!\033[0m")
    #  Mekanisme convert data list ke csv
    if user != [None]:
        # Menambahkan title pada index awal array atau baris pertama csv
        user_csv: List = recursion.appends(user, ["username", "password", "role"], True)
        recursion.write_csv(abs_path + "\\user.csv", user_csv, 3)
    if candi != [None]:
        # Menambahkan title pada index awal array atau baris pertama csv
        candi_csv: List = recursion.appends(candi, ["id", "pembuat", "pasir", "batu", "air"], True)
        recursion.write_csv(abs_path + "\\candi.csv", candi_csv, 5)
    if bahan_bangunan != [None]:
        # Memindahkan data bahan_bangunan yang merupakan array of integer ke array material
        for j in range(3):
            material[j][2] = bahan_bangunan[j]
        # Menambahkan title pada index awal array atau baris pertama csv
        material_csv: List = recursion.appends(material, ["nama", "deskripsi", "jumlah"], True)
        recursion.write_csv(abs_path + "\\bahan_bangunan.csv", material_csv, 3)\

# F15 - Help
#  Fungsi help untuk bantuan command yang dapat memandu perintah input dari user
def help(role: Union[str, None]) -> None:
    recursion.delay(0.5)
    print("\033[34m=========== HELP ===========\033[0m")
    # Halaman Utama
    if role == None:
        print("1. \033[33mlogin\033[0m")
        print("   Untuk masuk menggunakan akun")
        print("2. \033[33mexit\033[0m")
        print("   Untuk keluar dari program dan kembali ke terminal")
    # Bandung Bondowoso
    elif role == "bandung_bondowoso":
        print("1. \033[33mlogout\033[0m")
        print("   Untuk keluar dari akun yang digunakan sekarang")
        print("2. \033[33msummonjin\033[0m")
        print("   Untuk memanggil jin")
        print("3. \033[33mhapusjin\033[0m")
        print("   Untuk menghapus jin yang telah disummon")
        print("4. \033[33mubahjin\033[0m")
        print("   Untuk mengubah tipe jin yang telah disummon")
        print("5. \033[33mbatchkumpul\033[0m")
        print("   Untuk memerintahkan jin tipe pengumpul mengumpulkan bahan bangunan candi")
        print("6. \033[33mbatchbangun\033[0m")
        print("   Untuk memerintahkan jin tipe pembangun membangun candi dengan bahan yang tersedia")
        print("7. \033[33mlaporanjin\033[0m")
        print("   Untuk mengambil laporan progress jin")
        print("8. \033[33mlaporancandi\033[0m")
        print("   Untuk mengambil laporan progress candi")
        print("9. \033[33mundo\033[0m")
        print("   Untuk mengundo jin dan candi yang sudah dihapus")
        print("10. \033[33mload\033[0m")
        print("   Untuk memanggil kembali jin yang telah dihapus")
        print("11. \033[33msave\033[0m")
        print("   Untuk menyimpan semua progress yang telah dilakukan")
        print("12. \033[33mexit\033[0m")
        print("   Untuk keluar dari program dan kembali ke terminal")
    # Roro Jonggrang
    elif role == "roro_jonggrang":
        print("1. \033[33mlogout\033[0m")
        print("   Untuk keluar dari akun yang sekarang")
        print("2. \033[33mhancurkancandi\033[0m")
        print("   Untuk menghancurkan candi spesifik yang telah dibuat oleh jin tertentu")
        print("3. \033[33mayamberkokok\033[0m")
        print("   Untuk mendeklarasikan hasil akhir")
        print("4. \033[33msave\033[0m")
        print("   Untuk menyimpan semua progress yang telah dilakukan")
        print("5. \033[33mexit\033[0m")
        print("   Untuk keluar dari program dan kembali ke terminal")
    # Jin Pengumpul
    elif role == "jin_pengumpul":
        print("1. \033[33mlogout\033[0m")
        print("   Untuk keluar dari akun yang sekarang")
        print("2. \033[33mkumpul\033[0m")
        print("   Untuk mengumpulkan material bahan bangunan candi")
        print("3. \033[33msave\033[0m")
        print("   Untuk menyimpan semua progress yang telah dilakukan")
        print("4. \033[33mexit\033[0m")
        print("   Untuk keluar dari program dan kembali ke terminal")
    # Jin Pembangun
    elif role == "jin_pembangun":
        print("1. \033[33mlogout\033[0m")
        print("   Untuk keluar dari akun yang sekarang")
        print("2. \033[33mbangun\033[0m")
        print("   Untuk membangun candi")
        print("3. \033[33msave\033[0m")
        print("   Untuk menyimpan semua progress yang telah dilakukan")
        print("4. \033[33mexit\033[0m")
        print("   Untuk keluar dari program dan kembali ke terminal")
    else:
        print("Role not found")

# F16 - Exit
# Fungsi exit_program untuk keluar dari program
def exit_program(user: List = [None], candi: List = [None], bahan_bangunan: List = [None], material: List = [None]) -> None:
    recursion.delay(0.7)
    ask: str = ""
    while (ask == 'y' or ask == 'n'):
        ask: str = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n): ").lower()
        if ask == "y":
            save(user, candi, bahan_bangunan, material)
            exit(1)
        elif ask == "n":
            exit(1)