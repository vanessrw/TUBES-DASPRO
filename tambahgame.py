import module as module

def isAllFilled(parameter) :
    if (module.length(parameter) == 0 ) :
        return False
    else :
        return True

def gameId(idGame) :
    if (idGame // 10 == 0) :
        return ("G00" + str(idGame))
    if (1 <= idGame // 10 <= 9) :
        return ("G0" + str(idGame))
    if (10 <= idGame // 10) :
        return ("G" + str(idGame))

def TambahGame(gameDs) :
    data_game = gameDs
    inputGame = str(input("Masukkan nama game : "))
    inputKategori = str(input("Masukkan kategori : "))
    inputTahunRilis = str(input("Masukkan tahun rilis : "))
    inputHarga = str(input("Masukkan harga : "))
    inputStok = str(input("Masukkan stok awal : "))

    while (isAllFilled(inputGame) == False) or (isAllFilled(inputKategori) == False) or (isAllFilled(inputTahunRilis) == False) or ((isAllFilled(inputHarga) == False)) or (isAllFilled(inputStok) == False) :
        print("Mohon masukkan informasi yang lengkap.")
        inputGame = str(input("Masukkan nama game : "))
        inputKategori = str(input("Masukkan kategori : "))
        inputTahunRilis = str(input("Masukkan tahun rilis : "))
        inputHarga = str(input("Masukkan harga : "))
        inputStok = str(input("Masukkan stok awal : "))

    print("Selamat! Berhasil menambahkan game", inputGame)

    idGame = module.length(data_game)
    idGame = gameId(idGame)

    arrayGame = [" " for i in range (5)]
    for i in range (1) :
        for j in range(1) :
            arrayGame = [idGame, inputGame, inputKategori, inputTahunRilis, inputHarga, inputStok]
    
    data_game += arrayGame
    return gameDs
    
if __name__ == "__main__":
    TambahGame()

