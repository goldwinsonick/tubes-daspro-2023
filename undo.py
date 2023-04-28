from typing import List, Tuple


def undo(users: List, jin_list: List, candi_list: List, deleted_jin: List, deleted_candi: List) -> Tuple[List, List, List, List, List]:
    import recursion
    username: str = input("Masukkan username Jin yang akan di-undo: ")
    found: bool = False
    for i in range(recursion.length(deleted_jin)):
        if deleted_jin[i] and deleted_jin[i][0] == username:
            found = True
            confirmation:str = input(f"Apakah Anda yakin ingin meng-undo {username}? (y/n): ")
            if confirmation.lower() == "y":
                # menambahkan username sesuai ke jin_list
                empty_index:int = recursion.findEmptyArrayIndex(jin_list)
                jin_list[empty_index]:List = deleted_jin[i]
                # Menambahkan username sesuai ke users
                users:List = recursion.appends(users, deleted_jin[i])
                # Jika jin yang akan diundo adalah tipe pembangun, cek candi yang telah dibuat
                if deleted_jin[i] != None and deleted_jin[i][2] == "jin_pembangun":
                    # mekanisme penmindahan data candi dari deleted_candi ke candi_list
                    j:int = 0
                    while j < recursion.length(deleted_candi):
                        if deleted_candi[j] and deleted_candi[j][1] == username:
                            candi_list:List = recursion.appends(candi_list, deleted_candi[j])
                            deleted_candi:List = recursion.removes(deleted_candi, deleted_candi[j], recursion.length(deleted_candi))
                        else:
                            j += 1
                # Menghapus username sesuai dari deleted_jin
                deleted_jin:List = recursion.removes(deleted_jin, deleted_jin[i], recursion.length(deleted_jin))
                print(f"Data Jin {username} berhasil di-undo")
            elif confirmation.lower() == "n":
                print(f"Data Jin {username} tidak jadi di-undo")
            else:
                print("Jawaban tidak valid. Program dihentikan.")
                return users, jin_list, candi_list, deleted_jin, deleted_candi
    if not found:
        print(f"Data Jin {username} tidak ditemukan di dalam deleted_jin")
    return users, jin_list, candi_list, deleted_jin, deleted_candi
