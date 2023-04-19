import main
#Laporan candi hanya dapat diakses oleh akun Bandung Bondowoso.
def laporanjin() :
    totalpengumpul = 0
    totalpembangun = 0
    jinterajin = "-"
    jintermalas = "-"
    totalcandimaks = 0
    totalcandimin = 0
    # menentukan total jin dan total jin dari setiap tipe
    for i in range(102):
        if main.users[i] != None:
            if main.users[i][2] == "jin_pengumpul":
                totalpengumpul += 1
            if main.users[i][2] == "jin_pembangun":
                totalpembangun += 1
            totalcandi = 0
            if main.users[i][2] == "jin_pengumpul" or main.users[i][2] == "jin_pembangun":
                for j in range(100):
                    if main.candi[j] != None:
                        if main.candi[j][1] == main.users[i][0]:
                            totalcandi += 1
                # menentukan jin terajin
                if totalcandimaks < totalcandi: 
                    totalcandimaks = totalcandi
                    jinterajin = main.users[i][0]
                elif totalcandimaks == totalcandi:
                    if main.users[i][0] < jinterajin:
                        jinterajin = main.users[i][0]
                # menentukan jin termalas
                if main.users[i][2] == "jin_pembangun":
                    if totalcandimin > totalcandi:
                        totalcandimin = totalcandi
                        jintermalas = main.users[i][0]
                    elif totalcandimin == totalcandi:
                        if main.users[i][0] < jintermalas:
                            jintermalas = main.users[i][0]
    #Output
    print("> Total Jin: " + str(totalpembangun + totalpengumpul))
    print("> Total Jin Pengumpul: " + str(totalpengumpul))
    print("> Total Jin Pembangun: " + str(totalpembangun))
    print("> Jin Terajin: " + jinterajin)
    print("> Jin Termalas: " + jintermalas)
    print("> Jumlah Pasir: " + str(main.bahan_bangunan[0]) + " unit")
    print("> Jumlah Air: " + str(main.bahan_bangunan[1]) + " unit")
    print("> Jumlah Batu: " + str(main.bahan_bangunan[2]) + " unit")

def laporancandi():
    jumlahcandi = 0
    jumlahair = 0
    jumlahbatu = 0
    jumlahpasir = 0
    i = 0
    hargacandi = 0
    hargacandimaks = 0
    hargacandimin = 0
    idcanditermahal = 0
    idcanditermurah = 0
    # menentukan jumlah candi, pasir, batu, dan air
    for i in range (100):
        if main.candi[i] != None:
            jumlahcandi += 1
            jumlahpasir += main.candi[i][2]
            jumlahbatu += main.candi[i][3]
            jumlahair += main.candi[i][4]
    # menghitung total harga candi
    for i in range(100):
        if main.candi[i] != None:
            hargacandi = 10000 * main.candi[i][2] + 15000 * main.candi[i][3] + 7500 * main.candi[i][4]
            # menentukan id candi termahal dan termurah
            if hargacandimaks <= hargacandi:
                hargacandimaks = hargacandi
                idcanditermahal = main.candi[i][0]
            if hargacandimin > hargacandi:
                hargacandimin = hargacandi
                idcanditermurah = main.candi[i][0]
            if hargacandi == 0:
                idcanditermahal = "-"
                idcanditermurah = "-"
    #output
    print("> Total Candi: " + str(jumlahcandi))
    print("> Total Pasir yang digunakan: " + str(jumlahpasir))
    print("> Total Batu yang digunakan: " + str(jumlahbatu))
    print("> Total Air yang digunakan: " + str(jumlahair))
    print("> ID Candi Termahal: " + str(idcanditermahal))
    print("> ID Candi Termurah: " + str(idcanditermurah))