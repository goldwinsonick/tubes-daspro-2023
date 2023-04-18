def laporanjin(role, jin_list, bahan_bangunan, candi_list):
    import recursion
    if role != "bandung_bondowoso":
        print("Laporan jin hanya dapat diakses oleh akun Bandung Bondowoso.")
    else:
        # hitung jumlah jin per tipe
        total_jin = recursion.length()
        jin_pengumpul = 0
        jin_pembangun = 0
        for i in range(total_jin):
            if jin_list[i][2] == "jin_pengumpul":
                jin_pengumpul += 1
            elif jin_list[i][2] == "jin_pembangun":
                jin_pembangun += 1
        wadah=[None]
# Hitung jumlah kemunculan setiap nilai pada index ke-1
        count_dict = []
        for data in candi:
            if data[1] not in count_dict:
                count_dict[]data[1] = 1
            else:
                count_dict[data[1]] += 1

        # Pindahkan hasil ke dalam array baru yang sesuai dengan format yang diinginkan
        result = []
        for key, value in count_dict.items():
            result.append([value, key])

        # Cetak hasil
        print(result)

        # cari jin terajin dan jin termalas
        for jin in jin_list:
            if jin[3] == terajin[3] and jin[0] < terajin[0]:
                terajin = jin
            elif jin[3] == termalas[3] and jin[0] > termalas[0]:
                termalas = jin

        # tampilkan laporan
        print("> Total Jin:", total_jin)
        print("> Total Jin Pengumpul:", jin_pengumpul)
        print("> Total Jin Pembangun:", jin_pembangun)
        print("> Jin Terajin:", terajin[0] if total_jin > 0 else "-")
        # print("> Jin Termalas:", termalas[0] if total_jin > 0 else "-")
        print("> Jumlah Pasir:", bahan_bangunan[0], "unit")
        print("> Jumlah Air:", bahan_bangunan[1], "unit")
        print("> Jumlah Batu:", bahan_bangunan[2], "unit")


arr = [
    ["jin1", "sjdkhak", "jin_pembangun"],
    ["jin2", "sjdkhak", "jin_pembangun"],
    ["jin3", "sjdkhak", "jin_pembangun"],
    ["jin4", "sjdkhak", "jin_pembangun"],
    ["jin5", "sjdkhak", "jin_pembangun"],
    ["jin6", "sjdkhak", "jin_pengum"],
    ["jin7", "sjdkhak", "jin_pengum"],
    ["jin8", "sjdkhak", "jin_pengum"],
    ["jin9", "sjdkhak", "jin_pengum"],
    ["jin10", "sjdkhak", "jin_pengum"],
]

candi = [
    [1,"jin1",2,3,4],
    [2,"jin1",2,3,4],
    [3,"jin1",2,3,4],
    [4,"bin1",2,3,4],
    [5,"bin1",2,3,4],
    [6,"bin1",2,3,4],
    [7,"jin2",2,3,4],
    [8,"jin3",2,3,4],
         ]
bahan = [30,30,20]
laporanjin("bandung_bondowoso",arr,bahan, candi)
