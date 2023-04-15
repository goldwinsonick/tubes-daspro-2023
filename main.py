# import modules (jin, proses, bondowoso, dst)
import jin

users = [None for i in range(102)] # Array of user ([username, password, role])
# Panjang array 102 (bodowoso, roro, dan 100 jin)
candi = [None for i in range(100)]  # Array of candi ([id, pembuat, pasir, batu, air])
# Panjang array 100 (banyak candi maks)
bahan_bangunan = [0,0,0] # bahan_bangunan = [<pasir>, <batu>, <air>]
harga_candi = [0,0,0] # harga_candi = [<pasir>, <batu>, <air>]
user = ["","",""] # user ([username, password, role])

# CONTOH untuk JIN PEMBANGUN
user = ["jin1", "pass123", "jin_pembangun"]
bahan_bangunan = [4,5,4]
harga_candi = [1,2,3]
# CONTOH untuk JIN PENGUMPUL
user = ["jin1", "pass123", "jin_pengumpul"]
bahan_bangunan = [4,5,4]
harga_candi = [1,2,3]

# Tolong buatkan fungsi load
# proses.load("saves/user.csv", users)
# proses.load("saves/candi.csv", candi)
# proses.load("saves/bahan_bangunan.csv", bahan_bangunan)

while(True):
    inp = input(">>> ")
    # Memanggil fungsi di file lain berdasar inputan user
    if(inp == "bangun"):
        jin.bangun() 
    elif(inp == "kumpul"):
        jin.kumpul()
    elif(inp == "exit"):
        break
    # dst...

