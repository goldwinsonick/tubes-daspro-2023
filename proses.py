
from typing import Union, List, Tuple
# user = [['Bondowoso', 'cintaroro', 'bandung_bondowoso'],
#         ['Roro', 'gasukabondo', 'roro_jonggrag'], None]
# candi = [[1, "skjhd", 2, 3, 4], None]
# material = [['pasir', 'bahan bangunan pasir', '0'], ['batu', 'bahan bangunan batu', '0'], ['air', 'bahan bangunan air', '0'], None]
# bahan_bangunan = [3,2,1]
# user = [None]
# candi = [None]
# material = [None]
# bahan_bangunan = [None, None, None]


def load(users: List, candi: List, material: List, bahan_bangunan: List) -> Tuple[List, List, List]:
    import argparse
    import os
    import recursion
    # parsing argumen
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
        users = recursion.read_csv(parents_path + "\\user.csv")
        candi = recursion.read_csv(parents_path + "\\candi.csv")
        material = recursion.read_csv(parents_path + "\\bahan_bangunan.csv")
        for i in range(3):
            bahan_bangunan[i] = material[i][2]
        # bahan_bangunan = [<pasir>,<batu>,<air>]
        # Menyesuaikan dengan data yang telah kita bentuk pada awal
        print("Selamat datang di “Manajerial Candi”")

        # Aksi ketika nama folder yang dicari tidak ada
    else:
        print(f'Folder "{directory}" tidak ditemukan.')
        exit(1)
    return users, candi, material, bahan_bangunan

# user, candi,material, bahan_bangunan = load(user, candi,material, bahan_bangunan)
# print(user, candi, material,bahan_bangunan)


def save(user: List = [None], candi: List = [None], bahan_bangunan: List = [None], material: List = [None]) -> None:
    import os
    import recursion
    folder: str = input("Masukkan nama folder: ")
    abs_path: str = os.getcwd() + "\save\\" + folder
    # ** Mekanisme simpan dalam folder spesifik
    folder_path: str = os.path.join("save", folder)
    print("Saving...")
    # Validasi apakah folder save sudah ada
    if not os.path.exists('save'):
        print(f"Membuat folder save...")
        os.makedirs('save')
    # Validasi apakah subfolder nama_folder ada didalam save
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print(f"Membuat folder {folder_path}...")
    print("Berhasil menyimpan data di folder " + folder_path + "!")
    # ** Mekanisme convert list into csv
    if user != [None]:
        user_csv: List = recursion.appends(user, ["username", "password", "role"], True)
        recursion.write_csv(abs_path + "\\user.csv", user_csv, 3)
    if candi != [None]:
        candi_csv: List = recursion.appends(candi, ["id", "pembuat", "pasir", "batu", "air"], True)
        recursion.write_csv(abs_path + "\\candi.csv", candi_csv, 4)
    if bahan_bangunan != [None] and material != [None]:
        for i in range(3):
            material[i][2] = bahan_bangunan[i]
        recursion.write_csv(abs_path + "\\bahan_bangunan.csv", material,3)
# save(user, candi, bahan_bangunan, material)


def help(role: Union[str, None]) -> None:
    print("=========== HELP ===========")
    if role == None:
        print("1. login")
        print("   Untuk masuk menggunakan akun")
        print("2. exit")
        print("   Untuk keluar dari program dan kembali ke terminal")
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
        print("9. save")
        print("   Untuk menyimpan semua progress yang telah dilakukan")
        print("10. exit")
        print("   Untuk keluar dari program dan kembali ke terminal")
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
    elif role == "jin_pengumpul":
        print("1. logout")
        print("   Untuk keluar dari akun yang sekarang")
        print("2. kumpul")
        print("   Untuk mengumpulkan material bahan bangunan candi")
        print("3. save")
        print("   Untuk menyimpan semua progress yang telah dilakukan")
        print("4. exit")
        print("   Untuk keluar dari program dan kembali ke terminal")
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
# contoh tes penggunaan
# help("bandung_bondowoso")

def exit_program(user: List = [None], candi: List = [None], bahan_bangunan: List = [None], material: List = [None]) -> None:
    ask: str = input(
        "Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n): ")
    # Validasi input
    if ask == "y" or ask == "Y":
        save(user, candi, bahan_bangunan, material)
        exit(1)
    elif ask == "n" or ask == "N":
        exit(1)
    else:
        while ask != "y" or ask != "Y" or ask != "n" or ask != "N":
            ask = input(
                "Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n): ")
# contoh tes penggunaan
exit_program(user, candi, bahan_bangunan, material)
