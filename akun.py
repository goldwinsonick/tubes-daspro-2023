from typing import List, Union
import time
def login(fileUser: List, username: Union[None, str] = None) -> Union[None, str]:
    import recursion

    # Antisipasi pengguna yang sudah pernah login
    if username != None:
        recursion.delay(0.1)
        print("Login gagal!")
        print(f"Anda telah login dengan username {username}, silahkan lakukan “logout” sebelum melakukan login kembali")

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
            print("Username tidak terdaftar!")
            username = None
        # Ketika username ditemukan tapi password tidak ditemukan
        elif status_username == True and status_password == False:
            username = None
            print("Password salah!")
        # Ketika username dan password ditemukan
        else:
            recursion.clear()
            print(f'Selamat datang, {username}!')
            print()
            print("Masukkan command “help” untuk daftar command yang dapat kamu panggil.")
        return username

def logout(username: Union[str, None]) -> Union[str, None]:
    import recursion
    recursion.delay(1.2)
    if username == None:
        # Validasi belum kondisi login
        print("Logout gagal!")
        print("Anda belum login, silahkan login terlebih dahulu sebelum melakukan logout")
        return username
    else:
        # Validasi kalo username ga boleh None
        while True:
            confirm = input("Apakah Anda benar ingin logout (y/n): ")
            if confirm == "y" or confirm == "Y":
                recursion.clear()
                # Setup ke kondisi unlogin
                username = None
                return username
            elif confirm == "n" or confirm == "N":
                recursion.clear()
                return username
            else:  # tidak akan return atau keluar loop karena input yang tidak valid
                print("Masukkan input yang sesuai")