def laporanjin(user, jin_list, bahan_bangunan):
    if user != "Bandung Bondowoso":
        print("Laporan jin hanya dapat diakses oleh akun Bandung Bondowoso.")
        return
    
    # hitung jumlah jin per tipe
    total_jin = len(jin_list)
    jin_pengumpul = 0
    jin_pembangun = 0
    for jin in jin_list:
        if jin[2] == "jin_pengumpul":
            jin_pengumpul += 1
        elif jin[2] == "jin_pembangun":
            jin_pembangun += 1
    
    # cari jin terajin dan jin termalas
    terajin = max(jin_list, key=lambda jin: jin[3])[0]
    termalas = min(jin_list, key=lambda jin: jin[3])[0]
    for jin in jin_list:
        if jin[3] == terajin[3] and jin[0] < terajin[0]:
            terajin = jin
        elif jin[3] == termalas[3] and jin[0] > termalas[0]:
            termalas = jin
    
    # hitung jumlah material
    pasir = 0
    batu = 0
    air = 0
    for bahan in bahan_bangunan:
        if bahan[0] == "pasir":
            pasir += bahan[1]
        elif bahan[0] == "batu":
            batu += bahan[1]
        elif bahan[0] == "air":
            air += bahan[1]
    
    # tampilkan laporan
    print("> Total Jin:", total_jin)
    print("> Total Jin Pengumpul:", jin_pengumpul)
    print("> Total Jin Pembangun:", jin_pembangun)
    print("> Jin Terajin:", terajin[0] if total_jin > 0 else "-")
    print("> Jin Termalas:", termalas[0] if total_jin > 0 else "-")
    print("> Jumlah Pasir:", pasir, "unit")
    print("> Jumlah Air:", air, "unit")
    print("> Jumlah Batu:", batu, "unit")
