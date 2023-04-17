from typing import List
bahan_bangunan = [5, 5, 4]  # bahan_bangunan = [<pasir>, <batu>, <air>]
candi_list = [None for i in range(1)]
user = ["jin1", "pass123", "jin_pengumpul"]


def bangun(bahan_bangunan, user, candi_list):
    import rng
    import recursion
    if (user[2] == "jin_pembangun"):
        mencukupi = True
        # generate bahan bangunan yang dibutuhkan
        harga_candi = rng.rng(3, 1, 5)
        print(harga_candi)
        # checking id berdasarkan bahan 3 bahan bangunan
        for i in range(3):
            if (harga_candi[i] > bahan_bangunan[i]):
                mencukupi = False
        # aksi ketika bahan bangunan cukup
        if (mencukupi):
            # Menambah candi
            # Menyiapkan waday tambahan array
            temp_new_candi = [None for i in range(
                recursion.length(candi_list)+2)]
            # copy data dari candi_list sebelumnya
            for i in range(recursion.length(candi_list)):
                temp_new_candi[i] = candi_list[i]
            # Copy data baru dengan mark baru ke candi_list sebelumnya
            empty_index_array_temp_candi = recursion.findEmptyArrayIndex(
                temp_new_candi)
            temp_new_candi[empty_index_array_temp_candi] = [
                i, user[0], harga_candi[0], harga_candi[1], harga_candi[2]]
            # Kembalikan ke candi_list dengan data yang sudah update
            candi_list = temp_new_candi

            # Mengurangi bahan bangunan
            for i in range(3):
                bahan_bangunan[i] -= harga_candi[i]

            # Setelah Candi terbangun, harga_Candi baru akan digenerate

            print("Candi berhasil dibangun.")
            banyakCandi = 0
            for i in range(recursion.length(candi_list)):
                if (candi_list[i] != None):
                    banyakCandi += 1

            if banyakCandi < 100:
                print("Sisa candi yang perlu dibangun : " + str(100-banyakCandi))
            else:
                print("100 Candi sudah terbangun")

        else:
            print("Bahan bangunan tidak mencukupi.")
            print("Candi tidak bisa dibangun!")
    else:
        print("Hanya jin pembangun yang dapat menjalankan fungsi bangun")
    return bahan_bangunan, user, candi_list

# bahan_bangunan, user, candi_list = bangun(bahan_bangunan, user, candi_list)
# print(bahan_bangunan, user, candi_list)


def kumpul(user: List[str], bahan_bangunan: List[int]):
    import rng
    if (user[2] == "jin_pengumpul"):
        terkumpul = rng.rng(3, 1, 5)
        for i in range(3):
            bahan_bangunan[i] += terkumpul[i]
        print("Jin menemukan "+str(terkumpul[0])+" pasir, " +
              str(terkumpul[1])+" batu, "+str(terkumpul[2])+" air.")
    else:
        print("Hanya jin pengumpul yang dapat menjalankan fungsi kumpul")
    return user, bahan_bangunan
# user, bahan_bangunan = kumpul(user, bahan_bangunan)
# print(bahan_bangunan, user, candi_list)
