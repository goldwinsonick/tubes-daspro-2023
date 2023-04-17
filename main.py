# import modules (jin, proses, bondowoso, dst)
import jin
import bondowoso
import jin
import roro
import rng
import recursion
from typing import Union, List

# Array of user ([username, password, role])
users = [None for i in range(103)]
# Panjang array 102 (bodowoso, roro, dan 100 jin)
# Array of candi ([id, pembuat, pasir, batu, air])
candi_list = [None for i in range(101)]
# Array akan otomatis diiterasi dengan skema pada fungsi hapusJin
deleted_jin: List = [None for i in range(1)]
# Array akan otomatis diiterasi dengan skema pada fungsi hapusJin
deleted_candi: List = [None for i in range(1)]
# Panjang array 100 (banyak candi maks)
bahan_bangunan = [0, 0, 0]  # bahan_bangunan = [<pasir>, <batu>, <air>]
harga_candi = [0, 0, 0]  # harga_candi = [<pasir>, <batu>, <air>]
user = ["", "", ""]  # user ([username, password, role])
jin_list = [None for i in range(101)]
# CONTOH untuk JIN PEMBANGUN
user = ["jin1", "pass123", "Pembangun"]
bahan_bangunan = [4, 5, 4]
harga_candi = [1, 2, 3]
# CONTOH untuk JIN PENGUMPUL
user = ["jin1", "pass123", "Pengumpul"]
bahan_bangunan = [4, 5, 4]
harga_candi = [1, 2, 3]

# Tolong buatkan fungsi load
# proses.load("saves/user.csv", users)
# proses.load("saves/candi.csv", candi)
# proses.load("saves/bahan_bangunan.csv", bahan_bangunan)


def main_menu(username):
    # Pengecekan jika admin atau user biasa
    global jin_list
    role: str = username
    # Validasi user lagi
    # for i in range(recursion.length(F15.user)):
    #     if username == F15.user[i][1]:
    #         role = F15.user[i][4]
    #         break
    print("Selamat datang di love story Bandung Bondowoso dan Riri Jonggrang!")

    while True:
        print()
        command: str = input("Masukkan perintah: ")
        # Bondowoso only commands
        if command.lower() == "summonjin":  # F2
            if role == "Bondowoso":
                jin_list = bondowoso.summonJin(jin_list)
            else:
                print("Perintah ini hanya bisa diakses oleh Bondowoso.")
        elif command.lower() == "hapusjin":  # F4
            if role == "Bondowoso":
                jin_list, candi_list, deleted_jin, deleted_candi = bondowoso.hapusJin(
                    jin_list, candi_list, deleted_jin, deleted_candi)
            else:
                print("Perintah ini hanya bisa diakses oleh Bondowoso.")
        elif command.lower() == "ubahtipejin":  # F5
            if role == "Bondowoso":
                jin_list = bondowoso.ubahJin(jin_list)
            else:
                print("Perintah ini hanya bisa diakses oleh Bondowoso.")
        # elif command.lower() == "bangun":  # F6
        #     if role == "Jin Pembangun":
        #         jin.bangun(F15.game)
        #     else:
        #         print("Perintah ini hanya bisa diakses oleh Jin Pembangun.")
        # elif command.lower() == "kumpul":  # F12
        #     if role == "Jin Pengumpul":
        #         jin.kumpul(F15.user)
        #     else:
        #         print("Perintah ini hanya bisa diakses oleh Jin Pengumpul.")
        # # User only commands
        # elif command.lower() == "batch":  # F8
        #     if role == "Bondowoso":
        #         candi.batch(username, F15.kepemilikan, F15.user, F15.game, F15.riwayat)
        #     else:
        #         print("Perintah ini hanya bisa diakses oleh user.")
        # elif command.lower() == "laporanjin":  # F9
        #     if role == "Bondowoso":
        #         candi.laporanJin(Bondowosoname, F15.kepemilikan, F15.game)
        #     else:
        #         print("Perintah ini hanya bisa diakses oleh Bondowoso.")
        # elif command.lower() == "laporancandi":  # F10
        #     if role == "Bondowoso":
        #         candi.laporanCandi(F15.game, F15.kepemilikan, username)
        #     else:
        #         print("Perintah ini hanya bisa diakses oleh Bondowoso.")
        # elif command.lower() == "hancurkancandi":  # F11
        #     if role == "Roro":
        #         roro.hancurkanCandi(F15.game)
        #     else:
        #         print("Perintah ini hanya bisa diakses oleh Roro.")
        # elif command.lower() == "ayamberkokok":  # F13
        #     if role == "Roro":
        #         roro.ayamBerkokok(username, F15.riwayat)
        #     else:
        #         print("Perintah ini hanya bisa diakses oleh Roro.")
        # Role-agnostic commands
        # elif command.lower() == "logout":
        #     akun.logout()
        # elif command.lower() == "help":  # F14
        #     proses.help()
        # elif command.lower() == "save":  # F16
        #     proses.save()
        # elif command.lower() == "exit":
        #     proses.exit()
        else:
            print(
                "Perintah tidak dikenal. Ketik \"help\" untuk list semua perintah yang dikenal.")

def initial():
if __name__ == "__main__":      #validasi nama file
    # F15.load() #fungsi untuk load
    print()
    print("WELCOME TO RORO AND BONDOWOSO LOVE STORY")
    print()
    while True:
        cmd:str = input("Masukkan perintah: ")
        username:Union[str, None] = None
        if cmd.lower() == "login": # F3
            # username = F3.login(F15.user)  # validasi user yang login
            if username != None:
                main_menu(username)     #masuk ke menu utama
                break
        elif cmd.lower() == "help":  # F14  # masuk help program
            # proses.help(username, F15.user)
        elif cmd.lower() == "exit":  # F17  # keluar program
            # proses.exit_program(None)
        else:               # handle input tidak valid
            print("Perintah tidak dikenal. Ketik \"help\" untuk list semua perintah yang dikenal.")
        print()
