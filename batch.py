import rng
from typing import Union, List, Tuple
jin_list = [["jin1", "laslkdujalkd", "jin_pembangun"], ["jin2", "laslkdujalkd",
                                                        "jin_pengumpul"], ["jin3", "laslkdujalkd",
                                                                           "jin_pengumpul"],  ["jin4", "laslkdujalkd",
                                                                                               "jin_pengumpul"], ["jin5cls", "laslkdujalkd", "jin_pembangun"], None]
bahan_bangunan = [20, 20, 21]
candi_list = [None for i in range(1)]
id = 0


def batchkumpul(jin_list: List, bahan_bangunan: List) -> Tuple[int,List, List]:
    import recursion
    import jin
    # Cari jumlah jin pengumpul
    pengumpul_exist: int = 0
    total_terkumpul = [0, 0, 0]
    for i in range(recursion.length(jin_list)):
        if jin_list[i] != None:
            if jin_list[i][2] == "jin_pengumpul":
                pengumpul_exist += 1
    # Aksi ketika jin pengumpul tidak ada
    if pengumpul_exist <= 0:
        print("Kumpul gagal. Anda tidak punya jin pengumpul. Silahkan summon terlebih dahulu.")
    # Aksi ketika jumlah jin pengumpul >=0
    else:
        print(f"Mengerahkan {pengumpul_exist} jin untuk mengumpulkan bahan.")
        # Memerintahkan semua jin pengumpul untuk mengumpulkan material
        for j in range(recursion.length(jin_list)):
            if jin_list[j] != None and jin_list[j][2] == "jin_pengumpul":
                    jin_list[j], bahan_bangunan, terkumpul = jin.kumpul(jin_list[j], bahan_bangunan, False)
                    for i in range(3):
                        total_terkumpul[i] += terkumpul[i]
        print(f"Jin menemukan total {total_terkumpul[0]} pasir, {total_terkumpul[1]} batu, dan {total_terkumpul[2]} air.")
    return jin_list, bahan_bangunan
# jin_list, bahan_bangunan=batchkumpul(jin_list, bahan_bangunan)
# print(jin_list, bahan_bangunan)

def batchbangun(bahan_bangunan: List, jin_list: List, candi_list: List, id: int) -> Tuple[List, List, List, int]:
    import recursion
    import jin
    harga_candi_total = [0, 0, 0]
    # Cek apakah ada jin pembangun dan hitung jumlah jin pembangun
    pembangun_exist = 0
    for i in range(recursion.length(jin_list)):
        if jin_list[i] != None:
            if jin_list[i][2] == 'jin_pembangun':
                pembangun_exist += 1
    # Aksi ketika kekurangan jin
    if pembangun_exist <= 0:
        print("Bangun gagal. Anda tidak punya jin pembangun. Silahkan summon terlebih dahulu.")
    else:
        # Wadah untuk harga_candi hasil generate yang perlu dibuat oleh masing-masing jin
        temp_candi_generate = [None for i in range(recursion.length(jin_list))]
        print(f"Mengerahkan {pembangun_exist} jin untuk membangun candi dengan total bahan {bahan_bangunan[0]} pasir, {bahan_bangunan[1]} batu, dan {bahan_bangunan[2]} air.")
        for j in range(recursion.length(jin_list)):
            if jin_list[j] != None and jin_list[j][2] == "jin_pembangun":
                # Memasukkan hasil generate bahan_bangunan yang diperlukan masing-masing jin  pembangun saat pembuatan candi
                temp_candi_generate[j] = rng.rng(3, 1, 5)
                for h in range(3):
                    harga_candi_total[h] += temp_candi_generate[j][h]

        # Cek apakah bahan bangunan mencukupi
        mencukupi = True
        for i in range(3):
            if harga_candi_total[i] > bahan_bangunan[i]:
                mencukupi = False
                break

        # Jika mencukupi, bangun candi
        if mencukupi:
            for s in range(recursion.length(jin_list)):
                if jin_list[s] != None and jin_list[s][2] == "jin_pembangun":
                    # mulai bangun candi
                    bahan_bangunan, jin_list[s], candi_list, harga, id = jin.bangun(bahan_bangunan, jin_list[s], candi_list, temp_candi_generate[s], False, id)
            print("Jin berhasil membangun total", pembangun_exist, "candi.")
        # Jika tidak mencukupi, tampilkan pesan gagal
        else:
            print("Bangun gagal. Kurang", (harga_candi_total[0]-bahan_bangunan[0]) if (harga_candi_total[0]-bahan_bangunan[0]) > 0 else 0, "pasir,",(harga_candi_total[1]-bahan_bangunan[1]) if (harga_candi_total[1]-bahan_bangunan[1]) > 0 else 0, "batu, dan", (harga_candi_total[2]-bahan_bangunan[2]) if (harga_candi_total[2]-bahan_bangunan[2]) > 0 else 0, "air.")
            print("Candi yang terbangun 0")

    return bahan_bangunan, jin_list, candi_list, id
# skema penggunaan fungsi
# bahan_bangunan, jin_list, candi_list, id = batchbangun(bahan_bangunan, jin_list, candi_list, id)
# print(bahan_bangunan, candi_list)
