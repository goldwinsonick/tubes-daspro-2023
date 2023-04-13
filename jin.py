def bangun():
    import main
    import rng
    if(main.user[2] == "jin_pembangun"):
        flag = False
        for i in range(3):
            if(main.harga_candi[i] >= main.bahan_bangunan[i]):
                flag = True
        if(flag):
            # Menambah candi
            for i in range(100):
                if(main.candi[i] ==  None):
                    main.candi[i] = [i, main.user[0], main.harga_candi[0], main.harga_candi[1], main.harga_candi[2]]
                    break
            # jika dari index 0 dan 99 tidak ditemukan slot kosong, maka kode tetap jalan dan tidak menambah candi
            # sesuai dengan spesifikasi

            # Mengurangi bahan bangunan
            for i in range(3):
                main.bahan_bangunan[i] -= main.harga_candi[i]

            # Setelah Candi terbangun, harga_Candi baru akan digenerate
            for i in range(3):
                main.harga_candi[i] = rng(1,5)
            print("Candi berhasil dibangun.")
            banyakCandi = 0
            for i in range(100):
                if(main.candi[i] != None):
                    banyakCandi+=1
            print("Sisa candi yang perlu dibangun : " + str(100-banyakCandi))
            
        else:
            print("Bahan bangunan tidak mencukupi.")
            print("Candi tidak bisa dibangun!")
    else:
        print("Hanya jin pembangun yang dapat menjalankan fungsi bangun")

def kumpul():
    import main
    import rng
    if(main.user[2] == "jin_pengumpul"):
        terkumpul = [rng.rng(0,5), rng.rng(0,5), rng.rng(0,5)]
        for i in range(3):
            main.bahan_bangunan[i] += terkumpul[i]
        print("Jin menemukan "+str(terkumpul[0])+" pasir, "+str(terkumpul[1])+" batu, "+str(terkumpul[2])+" air.")))
    else:
        print("Hanya jin pengumpul yang dapat menjalankan fungsi kumpul")