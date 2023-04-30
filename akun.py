from typing import List, Union
import recursion

# F01 - Login
# Fungsi login memungkinkan user untuk dapat menggunakan fitur sesuai dengan role
def login(fileUser: List, username: Union[None, str] = None) -> Union[None, str]:
    # Antisipasi pengguna yang sudah pernah login
    if username != None:
        recursion.delay(0.1)
        print("\033[31mLogin gagal!\033[0m")
        print(f"Anda telah login dengan username \033[36m{username}\033[0m, silahkan lakukan \033[33m“logout”\033[0m sebelum melakukan login kembali\033[0m")
    # Pengecekan data username dan password pada fileUser
    else:
        # Saat masuk ke dalam aplikasi, pengguna yang belum login dapat memasukkan username dan password.
        username: str = input("Username: ")
        password: str = input("Password: ")
        recursion.delay(0.1)
    # inisialisasi status ditemukannya username dan password
        status_username: bool = False
        status_password: bool = False
        # Proses pencariam username dan password pada fileUser
        for i in range(recursion.length(fileUser)):
            if fileUser[i][0] == username and fileUser[i] != None:
                status_username: bool = True
                break
        for i in range(recursion.length(fileUser)):
            if fileUser[i][1] == password and fileUser[i][0] == username and fileUser[i] != None:
                status_username: bool = True
                status_password: bool = True
                break
        # Ketika username tidak ditemukan
        if status_username == False:
            print("\033[31mUsername tidak terdaftar!\033[0m")
            username = None
        # Ketika username ditemukan tapi password tidak ditemukan
        elif status_username == True and status_password == False:
            username = None
            print("\033[31mPassword salah!\033[0m")
        # Ketika username dan password ditemukan
        else:
            recursion.clear()
            print(f'\033[35mSelamat datang, \033[36m{username}!\033[0m')
            print()
            print("Masukkan command \033[33m“help”\033[0m untuk daftar command yang dapat kamu panggil.")
    return username

# F02 - Logout
# Fungsi Logout menghilangkan akses user terhadap suatu perintah
def logout(username: Union[str, None]) -> Union[str, None]:
    recursion.delay(1.2)
    if username == None:
        # Validasi belum kondisi login
        print("\033[31mLogout gagal!\033[0m")
        print('Anda belum login, silahkan \033[33m"login"\033[0m terlebih dahulu sebelum melakukan logout')
        return username
    else:
        # Validasi kalo username ga boleh None
        while True:
            confirm = input("\033[32mApakah Anda benar ingin logout (y/n): \033[0m")
            if confirm == "y" or confirm == "Y":
                recursion.clear()
                # Setup ke kondisi unlogin
                username = None
                return username
            elif confirm == "n" or confirm == "N":
                recursion.clear()
                return username
            else:  # tidak akan return atau keluar loop karena input yang tidak valid
                print("\033[31mMasukkan input yang sesuai\033[0m")