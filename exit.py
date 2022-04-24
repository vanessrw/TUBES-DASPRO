from save import *

def exit(userDs, gameDs, riwayatDs, kepemilikanDs):

    while True: 
        choice = input("Apakah Anda mau melakukan penyimpanan file yang sudah diubah? (y/n) ").lower()
        if choice == 'y' or choice == 'n':
            if choice.lower() == 'y':
                save(userDs, gameDs, riwayatDs, kepemilikanDs)
                print("Data berhasil disimpan, sampai jumpa ! >.<")
            else:
                print("Baik, sampai jumpa ! >.<")
            break
            
if __name__ == "__main__":
    exit()
