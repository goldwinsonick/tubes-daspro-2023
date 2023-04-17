from typing import List, Union, Tuple
file = [["Bondowoso", "cintaroro", "bandung_bondowoso"],
        ["Roro", "gasukabondo", "roro_jonggrang"]]


def login(fileUser: List[List[str]], status_login: bool) -> Union[None, str, bool, Tuple[Union[str, None], bool]]:
    import recursion
    # Saat masuk ke dalam aplikasi, pengguna bisa login dengan memasukkan username dan password.
    username: str = input('Masukkan username: ')
    password: str = input('Masukkan password: ')

    # inisialisasi nilai a = 0 agar saat pengondisian menemukan nilai a = 0 berarti username atau password salah
    status_username: bool = False
    status_password: bool = False
    if status_login == True:
        print("Login gagal!")
        print("Anda telah login dengan username Bandung, silahkan lakukan “logout” sebelum melakukan login kembali")
    # Pengecekan data username dan password pada fileUser
    else:
        for i in range(len(fileUser)):
            if fileUser[i][0] == username:
                status_username: bool = True
                break
        for i in range(len(fileUser)):
            if fileUser[i][1] == password and fileUser[i][0] == username:
                status_username: bool = True
                status_password: bool = True
                break

        # Pengondisian nilai dari id yang telah ada di inisialisasi
        if status_username == False:
            print("Username tidak terdaftar!")
            username: None = None
            return username, status_login
        elif status_username == True and status_password == False:
            username: None = None
            print("Password salah!")
            return username, status_login
        else:
            nama: str = fileUser[i][0]
            status_login: bool = True
            print(f'Selamat datang, {nama}!')
            print("Masukkan command “help” untuk daftar command yang dapat kamu panggil.")
            return username, status_login
# while True:
#     login(file)

status_login = True
username = "Bondowoso"
def logout(status_login: bool, username: Union[str, None]) -> Union[bool, str, None, Tuple[bool, Union[str, None]]]:
    if status_login == False:
        # Validasi belum kondisi login
        print("Logout gagal!")
        print("Anda belum login, silahkan login terlebih dahulu sebelum melakukan logout")
        return status_login, username
    else:
        # Validasi kalo username ga boleh None
        if username != None:
            while True:
                confirm = input("Apakah Anda benar ingin logout (y/n): ")
                if confirm.lower() == "y":
                    # Setup ke kondisi unlogin
                    status_login = False
                    username = None
                    return status_login, username
                elif confirm.lower() == "n":
                    return status_login, username
                else: # tidak aakan return atau keluar loop karena input yang tidak valid
                    print("Masukkan input yang sesuai")
        else:
            print("Username Undefined")
            return status_login, username

# status_login, username = logout(status_login, username)
# print(status_login, username)
