
from typing import Union, List, Tuple
import argparse
import os
import recursion

# Fungsi load untuk mengambil data dari csv pertama kali
def load(users: List, candi: List, material: List, bahan_bangunan: List, jin_list: List) -> Tuple[List, List, List]:
    # Parsing argumen
    parser: argparse.ArgumentParser = argparse.ArgumentParser()
    parser.add_argument("nama_folder", type=str, nargs="?", const="", help="Usage: python main.py <nama_folder>")
    args: argparse.Namespace = parser.parse_args()
    directory: Union[None, str] = args.nama_folder
    # Aksi ketika tidak ada nama file yang diberikan
    if directory is None:
        print("Tidak ada nama folder yang diberikan")
        print("Usage: python main.py <nama_folder>")
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
        print("Selamat datang di “Manajerial Candi”")

        # Aksi ketika nama folder yang dicari tidak ada
    else:
        print(f'Folder "{directory}" tidak ditemukan.')
        exit(1)
    return users, candi, material, bahan_bangunan, jin_list

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
    print("Berhasil menyimpan data di folder " + folder_path + "!")
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

#  Fungsi help untuk bantuan command yang dapat memandu perintah input dari user
def help(role: Union[str, None]) -> None:
    recursion.delay(0.5)
    print("=========== HELP ===========")
    # Halaman Utama
    if role == None:
        print("1. login")
        print("   Untuk masuk menggunakan akun")
        print("2. exit")
        print("   Untuk keluar dari program dan kembali ke terminal")
    # Bandung Bondowoso
    elif role == "bandung_bondowoso":
        print("1. logout")
        print("   Untuk keluar dari akun yang digunakan sekarang")
        print("2. summonjin")
        print("   Untuk memanggil jin")
        print("3. hilangkanjin")
        print("   Untuk menghapus jin yang telah disummon")
        print("4. ubahtipejin")
        print("   Untuk mengubah tipe jin yang telah disummon")
        print("5. batchkumpul")
        print("   Untuk memerintahkan jin tipe pengumpul mengumpulkan bahan bangunan candi")
        print("6. batchbangun")
        print("   Untuk memerintahkan jin tipe pembangun membangun candi dengan bahan yang tersedia")
        print("7. ambillaporanjin")
        print("   Untuk mengambil laporan progress jin")
        print("8. ambillaporancandi")
        print("   Untuk mengambil laporan progress candi")
        print("9. load")
        print("   Untuk memanggil kembali jin yang telah dihapus")
        print("10. save")
        print("   Untuk menyimpan semua progress yang telah dilakukan")
        print("11. exit")
        print("   Untuk keluar dari program dan kembali ke terminal")
    # Roro Jonggrang
    elif role == "roro_jonggrang":
        print("1. logout")
        print("   Untuk keluar dari akun yang sekarang")
        print("2. hancurkancandi")
        print("   Untuk menghancurkan candi spesifik yang telah dibuat oleh jin tertentu")
        print("3. ayamberkokok")
        print("   Untuk mendeklarasikan hasil akhir")
        print("4. save")
        print("   Untuk menyimpan semua progress yang telah dilakukan")
        print("5. exit")
        print("   Untuk keluar dari program dan kembali ke terminal")
    # Jin Pengumpul
    elif role == "jin_pengumpul":
        print("1. logout")
        print("   Untuk keluar dari akun yang sekarang")
        print("2. kumpul")
        print("   Untuk mengumpulkan material bahan bangunan candi")
        print("3. save")
        print("   Untuk menyimpan semua progress yang telah dilakukan")
        print("4. exit")
        print("   Untuk keluar dari program dan kembali ke terminal")
    # Jin Pembangun
    elif role == "jin_pembangun":
        print("1. logout")
        print("   Untuk keluar dari akun yang sekarang")
        print("2. bangun")
        print("   Untuk membangun candi")
        print("3. save")
        print("   Untuk menyimpan semua progress yang telah dilakukan")
        print("4. exit")
        print("   Untuk keluar dari program dan kembali ke terminal")
    else:
        print("Role not found")

# Fungsi exit_program untuk keluar dari program
def exit_program(user: List = [None], candi: List = [None], bahan_bangunan: List = [None], material: List = [None]) -> None:
    recursion.delay(0.7)
    ask: str = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n): ")
    # Validasi input
    if ask == "y" or ask == "Y":
        save(user, candi, bahan_bangunan, material)
        exit(1)
    elif ask == "n" or ask == "N":
        exit(1)
    else:
        while ask != "y" or ask != "Y" or ask != "n" or ask != "N":
            ask = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n): ")
