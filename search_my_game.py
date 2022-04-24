from module import *

def search_my_game(userArr, kepemilikanDs, gameDs):
    userId = userArr[0]

    gameId = input("Masukkan ID Game: ")
    isNullId = gameId == ""
    gameRls = input("Masukkan Tahun Rilis Game: ")
    isNullRls = gameRls == ""

    # Mencari daftar game yang dimiliki
    owned = []
    for [game_id,user_id] in kepemilikanDs:
        if user_id == userId: owned += [game_id]

    isNothingPrinted = True
    for game_id in owned: 
        index = 1
        for [id,nama,kategori,tahun_rilis,harga,stok] in gameDs:
            if game_id == id: 
                if isNullId : gameId = id
                if isNullRls : gameRls = tahun_rilis
                if gameId == id and gameRls == tahun_rilis:
                    isNothingPrinted = False
                    print(f"{uni(str(index),3)}. {id} | {uni(nama,25)} | {uni(harga,8)} | {uni(kategori,8)} | {uni(tahun_rilis,4)}")
                    index +=1
    if isNothingPrinted :
        print("Tidak ada game pada inventory-mu yang memenuhi kriteria")
    
if __name__ == "__main__":
    search_my_game()