from typing import List
# bahan_bangunan = [5, 5, 4]  # bahan_bangunan = [<pasir>, <batu>, <air>]
# candi_list = [None for i in range(1)]
# user = ["jin1", "pass123", "jin_pembangun"]
# id = 0

def bangun(bahan_bangunan, user, candi_list, harga_candi, output, id):
    import rng
    import recursion
    if (user[2] == "jin_pembangun"):
        mencukupi = True
        # generate bahan bangunan yang dibutuhkan
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
                id, user[0], harga_candi[0], harga_candi[1], harga_candi[2]]
            # Kembalikan ke candi_list dengan data yang sudah update
            candi_list = temp_new_candi

            # Mengurangi bahan bangunan
            for i in range(3):
                bahan_bangunan[i] -= harga_candi[i]

            # Setelah Candi terbangun, harga_Candi baru akan digenerate
            if output == True:
                print("Candi berhasil dibangun.")
            banyakCandi = 0
            for i in range(recursion.length(candi_list)):
                if (candi_list[i] != None):
                    banyakCandi += 1

            if banyakCandi < 100:
                if output == True:

                    print("Sisa candi yang perlu dibangun : " +
                          str(100-banyakCandi))
            else:
                if output == True:

                    print("100 Candi sudah terbangun")

        else:
            if output == True:
                print("Bahan bangunan tidak mencukupi.")
                print("Candi tidak bisa dibangun!")
    else:
        if output == True:
            print("Hanya jin pembangun yang dapat menjalankan fungsi bangun")
    return bahan_bangunan, user, candi_list, harga_candi, id

# bahan_bangunan, user, candi_list, harga_candi, id = bangun(bahan_bangunan, user, candi_list, [2,2,2], True, id)
# print(bahan_bangunan, user, candi_list, id)


def kumpul(user: List[str], bahan_bangunan: List[int], output):
    import rng
    if (user[2] == "jin_pengumpul"):
        terkumpul = rng.rng(3, 1, 5)
        for i in range(3):
            bahan_bangunan[i] += terkumpul[i]
        if output == True:
            print(str(user[0])+" menemukan "+str(terkumpul[0])+" pasir, " +
                  str(terkumpul[1])+" batu, "+str(terkumpul[2])+" air.")
    else:
        if output == True:
            print("Hanya jin pengumpul yang dapat menjalankan fungsi kumpul")
    return user, bahan_bangunan, terkumpul
# user, bahan_bangunan = kumpul(user, bahan_bangunan)
# print(bahan_bangunan, user, candi_list)
