# import modules (jin, proses, bondowoso, dst)
import jin
import bondowoso
import proses
import jin
import roro
import rng, laporan
import recursion
import akun, undo
from typing import List

# Array of user ([username, password, role])
users = [None]
candi_list = [None]
deleted_jin: List = [None]
deleted_candi: List = [None]
bahan_bangunan = [0, 0, 0]
harga_candi = [0, 0, 0]
jin_list = [None for i in range(101)]
material = [None]
id = 1

def main_program(username):
    global users, candi_list, deleted_candi, deleted_jin, bahan_bangunan, harga_candi, jin_list, id
    # Pengecekan jika admin atau user biasa
    global jin_list
    # Validasi role
    for i in range(recursion.length(users)):
        if username == users[i][0]:
            role = users[i][2]
            password = users[i][1]
            break
    while True:
        print()
        print(users, candi_list, material, bahan_bangunan)
        command: str = input("Masukkan perintah: ")
        # Bondowoso only commands
        if command.lower() == "login":  # F2
            username = akun.login(users, username)
        elif command.lower() == "summonjin":  # F2
            if role == "bandung_bondowoso":
                jin_list, users, deleted_jin = bondowoso.summonjin(jin_list, users,deleted_jin, 100)
            else:
                print("Perintah ini hanya bisa diakses oleh Bondowoso.")
        elif command.lower() == "hilangkanjin":  # F4
            if role == "bandung_bondowoso":
                jin_list, users, candi_list, deleted_jin, deleted_candi = bondowoso.hilangkanjin(jin_list,users, candi_list, deleted_jin, deleted_candi)
            else:
                print("Perintah ini hanya bisa diakses oleh Bondowoso.")
        elif command.lower() == "ubahtipejin":  # F5
            if role == "bandung_bondowoso":
                jin_list, users = bondowoso.ubahtipejin(jin_list, users)
            else:
                print("Perintah ini hanya bisa diakses oleh Bondowoso.")
        elif command.lower() == "bangun":  # F6
            if role == "jin_pembangun":
                bahan_bangunan, [username, password, role], candi_list, harga_candi, id = jin.bangun(bahan_bangunan, [username, password, role], candi_list, rng.rng(3, 1, 5), True, id)
            else:
                print("Perintah ini hanya bisa diakses oleh Jin Pembangun.")
        elif command.lower() == "kumpul":  # F12
            if role == "jin_pengumpul":
                [username, password, role], bahan_bangunan, terkumpul = jin.kumpul([username, password, role], bahan_bangunan, True)
            else:
                print("Perintah ini hanya bisa diakses oleh Jin Pengumpul.")
        elif command.lower() == "batchkumpul":  # F8
            if role == "bandung_bondowoso":
                jin_list, bahan_bangunan = bondowoso.batchkumpul(jin_list, bahan_bangunan)
            else:
                print("Perintah ini hanya bisa diakses oleh Bondowoso.")
        elif command.lower() == "batchbangun":  # F8
            if role == "bandung_bondowoso":
                bahan_bangunan, jin_list, candi_list, id = bondowoso.batchbangun(bahan_bangunan, jin_list, candi_list, id)
            else:
                print("Perintah ini hanya bisa diakses oleh Bondowoso.")
        elif command.lower() == "ambillaporanjin":  # F9
            if role == "bandung_bondowoso":
                laporan.laporanjin(candi_list, jin_list, bahan_bangunan)
            else:
                print("Perintah ini hanya bisa diakses oleh Bondowoso.")
        elif command.lower() == "ambillaporancandi":  # F10
            if role == "bandung_bondowoso":
                laporan.laporancandi(candi_list)
            else:
                print("Perintah ini hanya bisa diakses oleh Bondowoso.")
        elif command.lower() == "undo":  # B04
            if role == "bandung_bondowoso":
                users, jin_list, candi_list, deleted_jin, deleted_candi = undo.undo(users, jin_list, candi_list, deleted_jin, deleted_candi)
            else:
                print("Perintah ini hanya bisa diakses oleh Bondowoso.")
        elif command.lower() == "hancurkancandi":  # F11
            if role == "roro_jonggrang":
                candi_list = roro.hancurkancandi(candi_list)
            else:
                print("Perintah ini hanya bisa diakses oleh Roro.")
        elif command.lower() == "ayamberkokok":  # F13
            if role == "roro_jonggrang":
                roro.ayamberkokok(candi_list)
            else:
                print("Perintah ini hanya bisa diakses oleh Roro.")
        elif command.lower() == "logout":
            username = akun.logout(username)
            if username ==None:
                recursion.delay(0.6)
                print("Selamat datang di “Manajerial Candi”")
                return main_menu(users, candi_list, material, bahan_bangunan)
        elif command.lower() == "help":  # F14
            proses.help(role)
        elif command.lower() == "save":  # F16
            proses.save(users, candi_list, bahan_bangunan, material)
        elif command.lower() == "exit":
            return proses.exit_program(users, candi_list, bahan_bangunan, material)
        else:
            print("Perintah tidak dikenal. Ketik \"help\" untuk list semua perintah yang dikenal.")
    
def main_menu(users, candi_list, material, bahan_bangunan, username=None):  # validasi nama file
    recursion.delay(0.6)
    while True:
        cmd: str = input("Masukkan perintah: ")
        recursion.delay(0.2)
        if cmd.lower() == "login":  # F3
            # validasi user yang login
            username = akun.login(users, username)
            if username != None:
                return main_program(username)  # masuk ke menu main_menu
        elif cmd.lower() == "logout":
            username = akun.logout(username)
        elif cmd.lower() == "help":  # F14  # masuk help program
            proses.help(username)
        elif cmd.lower() == "exit":  # F17  # keluar program
            proses.exit_program(users, candi_list, bahan_bangunan, material)
        else:               # handle input tidak valid
            print("Perintah tidak dikenal. Ketik \"help\" untuk list semua perintah yang dikenal.")
# Memastikan fungsi package file lain hanya diakses oleh main.py
users, candi_list, material, bahan_bangunan, jin_list = proses.load(users, candi_list, material, bahan_bangunan, jin_list)  # fungsi untuk load
id = recursion.findId(id, candi_list)
main_menu(users, candi_list, material, bahan_bangunan)
