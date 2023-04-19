# import modules (jin, proses, bondowoso, dst)
import jin
import bondowoso
import jin
import roro
import rng
import recursion
import batch
import akun
from typing import Union, List

# Array of user ([username, password, role])
users = [["Bondowoso","cintaroro", "bandung_bondowoso"],["Roro","gasukabondo","roro_jonggrang"]]+[None for i in range(101)]
# Panjang array 102 (bodowoso, roro, dan 100 jin)
# Array of candi ([id, pembuat, pasir, batu, air])
candi_list = [None for i in range(1)]
# Array akan otomatis diiterasi dengan skema pada fungsi hapusJin
deleted_jin: List = [None for i in range(1)]
# Array akan otomatis diiterasi dengan skema pada fungsi hapusJin
deleted_candi: List = [None for i in range(1)]
# Panjang array 100 (banyak candi maks)
bahan_bangunan = [0, 0, 0]  # bahan_bangunan = [<pasir>, <batu>, <air>]
harga_candi = [0, 0, 0]
jin_list = [None for i in range(101)]
status_login = True
id = 0


def main_menu(username):
    global users, candi_list, deleted_candi,deleted_jin, bahan_bangunan, harga_candi, jin_list, status_login, id
    # Pengecekan jika admin atau user biasa
    global jin_list
    role: str = username
    # Validasi user lagi
    for i in range(recursion.length(users)):
        if username == users[i][0]:
            role = users[i][2]
            break
    print("Selamat datang di love story Bandung Bondowoso dan Riri Jonggrang!")

    while True:
        print()
        command: str = input("Masukkan perintah: ")
        # Bondowoso only commands
        if command.lower() == "summonjin":  # F2
            if role == "bandung_bondowoso":
                jin_list, users = bondowoso.summonJin(jin_list, users)                
            else:
                print("Perintah ini hanya bisa diakses oleh Bondowoso.")
        elif command.lower() == "hapusjin":  # F4
            if role == "bandung_bondowoso":
                jin_list, candi_list, deleted_jin, deleted_candi, users = bondowoso.hapusJin(
                    jin_list, candi_list, deleted_jin, deleted_candi, users)
            else:
                print("Perintah ini hanya bisa diakses oleh Bondowoso.")
        elif command.lower() == "ubahtipejin":  # F5
            if role == "bandung_bondowoso":
                jin_list, users = bondowoso.ubahJin(jin_list, users)
            else:
                print("Perintah ini hanya bisa diakses oleh Bondowoso.")
        elif command.lower() == "bangun":  # F6
            if role == "jin_pembangun":
                bahan_bangunan, role, candi_list, harga_candi, id = jin.bangun(
                    bahan_bangunan, role, candi_list, harga_candi, True, id)
            else:
                print("Perintah ini hanya bisa diakses oleh Jin Pembangun.")
        elif command.lower() == "kumpul":  # F12
            if role == "jin_pengumpul":
                role, bahan_bangunan, terkumpul = jin.kumpul(
                    role, bahan_bangunan, True)
            else:
                print("Perintah ini hanya bisa diakses oleh Jin Pengumpul.")
        # # User only commands
        elif command.lower() == "batchkumpul":  # F8
            if role == "bandung_bondowoso":
                id, jin_list, bahan_bangunan = batch.batchkumpul(
                    id, jin_list, bahan_bangunan)
            else:
                print("Perintah ini hanya bisa diakses oleh user.")
        elif command.lower() == "batchbangun":  # F8
            if role == "bandung_bondowoso":
                bahan_bangunan, jin_list, candi_list,id= batch.batchbangun(
                    bahan_bangunan, jin_list, candi_list, id)
            else:
                print("Perintah ini hanya bisa diakses oleh user.")
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
        elif command.lower() == "hancurkancandi":  # F11
            if role == "roro_jonggrang":
                candi_list = roro.hancurkancandi(candi_list)
            else:
                print("Perintah ini hanya bisa diakses oleh Roro.")
        elif command.lower() == "ayamberkokok":  # F13
            if role == "Roro":
                roro.ayamBerkokok(candi_list)
            else:
                print("Perintah ini hanya bisa diakses oleh Roro.")
        # Role-agnostic commands
        elif command.lower() == "logout":
            akun.logout(status_login, username)
        # elif command.lower() == "help":  # F14
        #     proses.help()
        # elif command.lower() == "save":  # F16
        #     proses.save()
        # elif command.lower() == "exit":
        #     proses.exit()
        else:
            print(
                "Perintah tidak dikenal. Ketik \"help\" untuk list semua perintah yang dikenal.")
        print(users)



def utama(status_login):  # validasi nama file
    # F15.load() #fungsi untuk load
    print()
    print("WELCOME TO RORO AND BONDOWOSO LOVE STORY")
    print()
    while True:
        cmd: str = input("Masukkan perintah: ")
        username: Union[str, None] = None
        if cmd.lower() == "login":  # F3
            username = akun.login(F15.user)  # validasi user yang login
            if username != None:
                main_menu(username)  # masuk ke menu utama
        #         break
        # elif cmd.lower() == "help":  # F14  # masuk help program
        #     # proses.help(username, F15.user)
        # elif cmd.lower() == "exit":  # F17  # keluar program
        #     # proses.exit_program(None)
        else:               # handle input tidak valid
            print(
                "Perintah tidak dikenal. Ketik \"help\" untuk list semua perintah yang dikenal.")
        print()

main_menu("Bondowoso")