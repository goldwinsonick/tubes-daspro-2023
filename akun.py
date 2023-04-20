from typing import List, Union, Tuple
user = [['Bondowoso', 'cintaroro', 'bandung_bondowoso'],
        ['Roro', 'gasukabondo', 'roro_jonggransasdg'], None]


def login(fileUser: List, username: Union[None, str] = None) -> Union[None, str]:
    import recursion
    # Antisipasi pengguna yang sudah pernah login
    if username != None:
        print("Login gagal!")
        print(
            f"Anda telah login dengan username {username}, silahkan lakukan “logout” sebelum melakukan login kembali")

    # Pengecekan data username dan password pada fileUser
    else:
        # Saat masuk ke dalam aplikasi, pengguna yang belum login dapat memasukkan username dan password.
        username: str = input("Username: ")
        password: str = input("Password: ")

    # inisialisasi status ditemukannya username dan password
        status_username: bool = False
        status_password: bool = False
        # Proses pencariam username dan password pada fileUser
        for i in range(recursion.length(fileUser)):
            if fileUser[i][0] == username:
                status_username: bool = True
                break
        for i in range(recursion.length(fileUser)):
            if fileUser[i][1] == password and fileUser[i][0] == username:
                status_username: bool = True
                status_password: bool = True
                break
        # Ketika username tidak ditemukan
        if status_username == False:
            print("Username tidak terdaftar!")
            username: None = None
        # Ketika username ditemukan tapi password tidak ditemukan
        elif status_username == True and status_password == False:
            username: None = None
            print("Password salah!")
        # Ketika username dan password ditemukan
        else:
            print(f'Selamat datang, {username}!')
            print("Masukkan command “help” untuk daftar command yang dapat kamu panggil.")
        return username
# username = login(user)
# print(username)


def logout(username: Union[str, None]) -> Union[str, None]:
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
                # Setup ke kondisi unlogin
                username = None
                return username
            elif confirm == "n" or confirm == "N":
                return username
            else:  # tidak akan return atau keluar loop karena input yang tidak valid
                print("Masukkan input yang sesuai")
# username = logout(None)
# print(username)
