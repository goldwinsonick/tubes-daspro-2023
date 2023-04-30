from typing import List, Tuple
import recursion, rng

def bangun(bahan_bangunan:List, user:List, candi_list:List, harga_candi:List, output:bool, id:int) -> Tuple[List, List, List, List, bool, int]:
    # parameter otput ada agar dapat digunakan kembali oleh fungsi batchbangun
    recursion.delay(0.5)
    if (user[2] == "jin_pembangun"):
        mencukupi:bool = True
        # Checking apakah bahan bangunan mencukupi untuk dibuat candi
        for i in range(3):
            if (harga_candi[i] > bahan_bangunan[i]):
                mencukupi = False
        # aksi ketika bahan bangunan cukup
        if (mencukupi):
            # Menambah candi baru ke list candi
            new_candi:List = [id, user[0], harga_candi[0], harga_candi[1], harga_candi[2]]
            candi_list:List = recursion.appends(candi_list, new_candi)
            id+=1

            # Mengurangi bahan bangunan
            for i in range(3):
                bahan_bangunan[i] -= harga_candi[i]

            # Setelah Candi terbangun, harga_candi baru akan digenerate
            if output == True:
                print("Candi berhasil dibangun.")
            banyakCandi:int = 0
            for i in range(recursion.length(candi_list)):
                if (candi_list[i] != None):
                    banyakCandi += 1
            if banyakCandi < 100:
                if output == True:
                    print("Sisa candi yang perlu dibangun : " + str(100-banyakCandi))
            else:
                if output == True:
                    print("100 Candi sudah terbangun")
        # Kasus tidak cukup bahannya
        else:
            if output == True:
                print("Bahan bangunan tidak mencukupi.")
                print("Candi tidak bisa dibangun!")
    # Kasus bukan jin pembangun
    else:
        if output == True:
            print("Hanya jin pembangun yang dapat menjalankan fungsi bangun")
    return bahan_bangunan, user, candi_list, harga_candi, id

def kumpul(user: List, bahan_bangunan: List, output:bool) -> Tuple[List, List, bool]:
    recursion.delay(0.5)
    terkumpul = [0,0,0]
    if (user[2] == "jin_pengumpul"):
        terkumpul = rng.rng(3, 1, 5)
        for i in range(3):
            bahan_bangunan[i] += terkumpul[i]
        if output == True:
            print(f"{user[0]} menemukan {terkumpul[0]} pasir, {terkumpul[1]} batu, {terkumpul[2]} air.")
    else:
        if output == True:
            print("Hanya jin pengumpul yang dapat menjalankan fungsi kumpul")
    return user, bahan_bangunan, terkumpul