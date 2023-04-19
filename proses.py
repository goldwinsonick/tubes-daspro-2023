# user = [['username', 'password', 'role'], ['Bondowoso', 'cintaroro', 'bandung_bondowoso'], ['Roro', 'gasukabondo', 'roro_jonggransasdg']]
# candi = [['id', 'pembuat', 'pasir', 'batu', 'air'], [1,"skjhd",2,3,4]]
# bahan_bangunan = [['nama', 'deskripsi', 'jumlah'],["Sadasd","dasdasd",2]]
user = [['Bondowoso', 'cintaroro', 'bandung_bondowoso'],
        ['Roro', 'gasukabondo', 'roro_jonggransasdg'],None]
candi = [[1,"skjhd",2,3,4],None]
# bahan_bangunan = [['nama', 'deskripsi', 'jumlah'],["Sadasd","dasdasd",2]]


def load():
    global user, candi, bahan_bangunan
    import argparse
    import os
    import recursion
    parser = argparse.ArgumentParser()
    parser.add_argument("nama_folder", type=str, nargs="?",
                        const="", help="tulis nama folder yang sudah dibuat")
    args = parser.parse_args()
    folder = input("Masukkan nama folder penyimpanan: ")
    parents_path = os.getcwd() + "\\" + folder
    if os.path.isdir(parents_path):
        print("Loading...")
        user = recursion.read_csv(parents_path + "\\user.csv")
        candi = recursion.read_csv(parents_path + "\\candi.csv")
        bahan_bangunan = recursion.read_csv(
            parents_path + "\\bahan_bangunan.csv")
        print("Selamat datang di antarmuka \"Kisah cinta Bandung Bondowoso\" ")
    else:
        print(f'Folder "{folder}" tidak ditemukan.')
# load()
# print(user, candi, bahan_bangunan)


def save(user=None, candi=None):
    import os
    import recursion
    folder = input("Masukkan nama folder penyimpanan: ")
    abs_path = os.getcwd() + "\\" + folder
    print("Saving...")
    if not os.path.exists(abs_path):
        os.makedirs(abs_path)
    if user is not None:
        user_csv = recursion.appends(user,["username","password","role"],True)
        print(user_csv)
        recursion.write_csv(abs_path + "\\user.csv", user_csv,3)
    if candi is not None:
        candi_csv = recursion.appends(candi,["id","pembuat","pasir","batu","air"],True)
        recursion.write_csv(abs_path + "\\candi.csv", candi_csv,4)
    # if bahan_bangunan is not None:
    #     recursion.write_csv(abs_path + "\\bahan_bangunan.csv", bahan_bangunan)
    print("Data telah disimpan di " + folder + "!")


# save(user, candi,bahan_bangunan)
# TODO: validasi role sama ganti skema ganti line
# save(user, candi)


def help(role):
    print("=========== HELP ===========\n1. login\n   Untuk masuk menggunakan akun\n2. exit\n   Untuk keluar dari program dan kembali ke terminal\n>>>")
    print("=========== HELP ===========\n1. logout\n   Untuk keluar dari akun yang digunakan sekarang\n2. summonjin\n   Untuk memanggil jin\n>>>")
    print("=========== HELP ===========\n1. logout\n   Untuk keluar dari akun yang digunakan sekarang\n2. hancurkancandi\n   Untuk menghancurkan candi yang tersedia\n>>>")
    print("=========== HELP ===========\n1. logout\n   Untuk keluar dari akun yang digunakan sekarang\n2. kumpul\n   Untuk mengumpulkan resource candi\n>>>")
    print("=========== HELP ===========\n1. logout\n   Untuk keluar dari akun yang digunakan sekarang\n2. bangun\n   Untuk membangun candi\n>>>")


def exit_program(user=None, candi=None, bahan_bangunan=None):
    ask = input(
        "Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n)")
    if ask == "y" or ask == "Y":
        save(user, candi, bahan_bangunan)
        exit(1)
    elif ask == "n" or ask == "N":
        exit(1)
    else:
        while ask != "y" or ask != "Y" or ask != "n" or ask != "N":
            ask = input(
                "Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ")
exit_program()

arr = [2, 43, 4, 5, 2]
# copy_candi=  [None for i in range(len(arr)+1)]
# print(copy_candi)
# for i in range(len(arr)):
#     copy_candi[i] = candi[i]
# candi= copy_candi
# print(candi)
# import recursion
# arr = [2, 43, 4, 5, 2]
# copy_candi = [None for i in range(1000)]
# print(copy_candi)
# for i in range(len(arr)):
#     copy_candi[i] = arr[i]
# i = 0


# print(arr)
