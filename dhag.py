ask = str(input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) "))
if ask == "y" or ask == "Y":
    save()
    exit()
elif ask == "n" or ask == "N":
    exit()
else:
    while ask != "y" or ask != "Y" or ask != "n" or ask != "N":
        ask = str(input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) "))