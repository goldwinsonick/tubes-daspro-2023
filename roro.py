from typing import List
import recursion, proses

# F11 - Hancurkan Candi
# Fungsi hancurkancandi hanya dapat diakses oleh roro jonggrang akan menghapus candi dari candi_list dengan validasi berdasarkan id dari candi tersebut
def hancurkancandi(candi_list:List) -> List:
    recursion.delay(0.8)
    found:bool = False
    length_candi_list:int = recursion.length(candi_list)
    # Input ID candi
    inp:str = input("Masukkan ID candi: ")
    recursion.delay(0.4)
    # Jika ID adalah string dan bukan number
    if (recursion.isDigit(inp) == False):
        print("\033[31mInput tidak valid (Inputan harus angka!)\033[0m")
        return candi_list
    inp:int = int(inp) 
    # cari candi dengan ID inp
    for i in range(length_candi_list):
        if candi_list[i][0] == inp:
            found = True
            break
    # Peringatan untuk hapus candi
    if (found == True):
        YN = input(f"Apakah anda yakin ingin menghancurkan candi ID : \033[36m{inp}\033[0m ? \033[33m(Y/N)\033[0m ")
        if (YN.upper() == "Y"):
            recursion.delay(0.8)

            # Menghapus candi dengan id inp dari candi_list
            for i in range(recursion.length(candi_list)):
                if candi_list[i] != None and candi_list[i][0] == inp:
                    candi_list:List = recursion.removes(candi_list, candi_list[i],length_candi_list)

            print("\033[32mCandi telah berhasil dihancurkan\033[0m")
        elif (YN.upper() == "N"):
            print("\033[34mCandi tidak jadi di hancurkan\033[0m")
        else:
            print("\033[31mTidak valid\033[0m")
    else:
        print("\033[31mTidak ada candi dengan ID tersebut.\033[0m")
    return candi_list

# F12 - Ayam Berkokok
# Fungsi ayamberkokok hanya dapat diakses oleh roro jonggrang akan mengumumkan pemenang
def ayamberkokok(candi_list:List) -> None:
    recursion.delay(0.8)
    print("\033[34mKukuruyuk.. Kukuruyuk..\033[0m")
    banyakCandi:int = recursion.length(candi_list)
    if (banyakCandi <= 99):
        print("\033[32mSelamat, Roro Jonggrang memenangkan permainan!\033[0m")
        print("\033[31m*Bandung Bondowoso angry noiseee*\033[0m")
        print("\033[33mRoro Jonggrang dikutuk menjadi candi\033[0m")
    else:
        print("\033[32mYah, Bandung Bondowoso memenangkan permainan!\033[0m")
    proses.exit_program(1)
