from typing import List, Union

def laporanjin(candi_list: List, jin_list: List, bahan_bangunan: List) -> None:
    import recursion
    jumlah_candi: List = [None]
    # Membuat array baru untuk menghitung candi yang telah dibuat oleh jin tertentu
    for i in range(recursion.length(candi_list)):
        if candi_list[i] != None:
            pembuat = candi_list[i][1]
            sudah_tercatat = False
            for j in range(recursion.length(jumlah_candi)+1):
                if jumlah_candi[j] != None and pembuat == jumlah_candi[j][0]:
                    jumlah_candi[j][1] += 1
                    sudah_tercatat = True
                    break
            if not sudah_tercatat:
                jumlah_candi = recursion.appends(jumlah_candi, [pembuat, 1])
    # Menentukan jin termalas dan terajin
    jin_terajin: Union[None, str] = None
    jin_termalas: Union[None, str] = None
    jumlah_tertinggi: int = -1
    jumlah_terendah: int = 1000

    for i in range(recursion.length(jumlah_candi)):
        jin: str = jumlah_candi[i][0]
        jumlah: int = jumlah_candi[i][1]
        # untuk jin terajin
        if jumlah > jumlah_tertinggi:
            jumlah_tertinggi = jumlah
            jin_terajin = jin
        # jika ada kasus jumlah candi yang dibangun sama ambil yang leksiografis rendah
        elif jumlah == jumlah_tertinggi and jin < jin_terajin:
            jin_terajin = jin
        # untuk jin termalas
        if jumlah < jumlah_terendah:
            jumlah_terendah = jumlah
            jin_termalas = jin
        # jika ada kasus jumlah candi yang dibangun sama ambil yang leksiografis tinggi
        elif jumlah == jumlah_terendah and jin > jin_termalas:
            jin_termalas = jin
    # Menentukan jumlah jin pengumpul dan pembangun
    totalpengumpul: int = 0
    totalpembangun: int = 0
    for i in range(recursion.length(jin_list)):
        if jin_list[i] != None and jin_list[i][2] == "jin_pengumpul":
            totalpengumpul += 1
        elif jin_list[i] != None and jin_list[i][2] == "jin_pembangun":
            totalpembangun += 1

    print("> Total Jin: " + str(recursion.length(jin_list)))
    print("> Total Jin Pengumpul: " + str(totalpengumpul))
    print("> Total Jin Pembangun: " + str(totalpembangun))
    print("> Jin Terajin: " + jin_terajin)
    print("> Jin Termalas: " + jin_termalas)
    print("> Jumlah Pasir: " + str(bahan_bangunan[0]) + " unit")
    print("> Jumlah Air: " + str(bahan_bangunan[1]) + " unit")
    print("> Jumlah Batu: " + str(bahan_bangunan[2]) + " unit")

# # contoh penggunaan
# candi_list: List = [
#     [1, "jin1", 2, 4, 3],
#     [2, "jin1", 3, 4, 4],
#     [3, "jin1", 4, 4, 5],
#     [4, "jin2", 5, 4, 6],
#     [5, "jin2", 6, 4, 7],
#     [6, "jin2", 7, 4, 8],
#     None]
# jin_list: List = [
#     ["jin1", "testing1", "jin_pembangun"],
#     ["jin2", "testing2", "jin_pembangun"],
#     ["jin3", "testing3", "jin_pembangun"],
#     ["jin4", "testing4", "jin_pengumpul"],
#     ["jin5", "testing5", "jin_pengumpul"],
#     None
# ]
# bahan_bangunan = [20,21,22]
# laporanjin(candi_list, jin_list, bahan_bangunan)


def laporancandi(candi_list: List) -> None:
    import recursion
    jumlahcandi:int = 0
    jumlahair:int = 0
    jumlahbatu:int = 0
    jumlahpasir:int = 0
    hargacandi:int = 0
    hargacandimaks:int = 0
    hargacandimin:int = 0
    idcanditermahal:int = 0
    idcanditermurah:int = 1
    # menentukan jumlah candi, pasir, batu, dan air
    for i in range(recursion.length(candi_list)):
        if candi_list[i] != None:
            jumlahcandi += 1
            jumlahpasir += candi_list[i][2]
            jumlahbatu += candi_list[i][3]
            jumlahair += candi_list[i][4]
    # menghitung total harga candi
            hargacandi = 10000 * \
                candi_list[i][2] + 15000 * \
                candi_list[i][3] + 7500 * candi_list[i][4]
            # menentukan id candi termahal dan termurah
            if hargacandimaks <= hargacandi:
                hargacandimaks = hargacandi
                idcanditermahal = candi_list[i][0]
            if hargacandimin > hargacandi:
                hargacandimin = hargacandi
                idcanditermurah = candi_list[i][0]
            if hargacandi == 0:
                idcanditermahal = "-"
                idcanditermurah = "-"

    # output
    print("> Total Candi: " + str(jumlahcandi))
    print("> Total Pasir yang digunakan: " + str(jumlahpasir))
    print("> Total Batu yang digunakan: " + str(jumlahbatu))
    print("> Total Air yang digunakan: " + str(jumlahair))
    print("> ID Candi Termahal: " + str(idcanditermahal))
    print("> ID Candi Termurah: " + str(idcanditermurah))

# laporancandi(candi_list)
