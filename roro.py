def hancurkancandi():
    import main
    inp = input("Masukkan ID candi: ")
    if(not inp.isnumeric()):
        print("Input tidak valid (Inputan harus angka!)")
        return
    inp = int(inp)
    
    if(0 < inp and inp < 100 and main.candi[inp] != None):
        YN = input("Apakah anda yakin ingin menghancurkan candi ID : "+str(inp) + "? (Y/N)")
        if(YN == "Y"):
            main.candi[inp] = None
            print("Candi telah berhasil dihancurkan")
        elif(YN == "N"):
            print("Candi tidak jadi di hancurkan")
        else:
            print("Tidak valid")
    else:
        print("Tidak ada candi dengan ID tersebut.")

