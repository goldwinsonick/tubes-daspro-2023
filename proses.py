def load(data):
    import argparse, os
    parser = argparse.ArgumentParser()
    parser.add_argument("path", type = str, nargs="?", const="")
    args = parser.parse_args()
    folder = input("Masukkan nama folder penyimpanan: ")
    parents_path = os.getcwd() + "\\" + folder
    print(args.path)
    if not args.path:
        print("Masukkan folder yang ingin dibuka!")
    elif os.path.exists(f"{parents_path}{args.path}"):
        path_data_user = f"{parents_path}{args.path}\\user.csv"
        path_data_candi = f"{parents_path}{args.path}\\candi.csv"
        path_data_bahan_bangunan = f"{parents_path}{args.path}\\bahan_bangunan.csv"
    else:
        print(f"Folder ,\"{args.path}\" tidak ditemukan.")

def save(user=None, candi=None, bahan_bangunan=None):
    import os, recursion
    folder = input("Masukkan nama folder penyimpanan: ")
    abs_path = os.getcwd() + "\\" + folder
    print("Saving...")

    if not os.path.exists(abs_path):
        os.makedirs(abs_path)
    if user is not None:
        recursion.write_csv(abs_path + "\\user.csv", user)
    if candi is not None:
        recursion.write_csv(abs_path + "\\candi.csv", candi)
    if bahan_bangunan is not None:
        recursion.write_csv(abs_path + "\\bahan_bangunan.csv", bahan_bangunan)
    print("Data telah disimpan di " + folder + "!")

def help():
    print("=========== HELP ===========\n1. login\n   Untuk masuk menggunakan akun\n2. exit\n   Untuk keluar dari program dan kembali ke terminal\n>>>")
    print("=========== HELP ===========\n1. logout\n   Untuk keluar dari akun yang digunakan sekarang\n2. summonjin\n   Untuk memanggil jin\n>>>")
    print("=========== HELP ===========\n1. logout\n   Untuk keluar dari akun yang digunakan sekarang\n2. hancurkancandi\n   Untuk menghancurkan candi yang tersedia\n>>>")
    print("=========== HELP ===========\n1. logout\n   Untuk keluar dari akun yang digunakan sekarang\n2. kumpul\n   Untuk mengumpulkan resource candi\n>>>")
    print("=========== HELP ===========\n1. logout\n   Untuk keluar dari akun yang digunakan sekarang\n2. bangun\n   Untuk membangun candi\n>>>")

def exit_program(user=None, candi=None, bahan_bangunan=None, username=None):
    ask = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ")
    if ask == "y" or ask == "Y":
        save(user, candi, bahan_bangunan)
        exit()
    elif ask == "n" or ask == "N":
        exit()
    else:
        while ask != "y" or ask != "Y" or ask != "n" or ask != "N":
            ask = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ")