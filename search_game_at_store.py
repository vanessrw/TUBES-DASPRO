from audioop import findmax
from tokenize import String
from cipher import findOrd
from module import *

def search_game_at_store(gameDs):

    gameId = input("Masukkan ID Game: ")
    isNullId = gameId == ""
    gameName = input("Masukkan Nama Game: ")
    isNullName = gameName == ""
    gamePrc = input("Masukkan Harga Game: ")
    isNullPrc = gamePrc == ""
    gameCtg = input("Masukkan Kategori Game: ")
    isNullCtg = gameCtg == ""
    gameRls = input("Masukkan Tahun Rilis Game: ")
    isNullRls = gameRls == ""
    
    isNothingPrinted = True
    for [id,nama,kategori,tahun_rilis,harga,stok] in gameDs:
        if isNullId : gameId = id
        if isNullName  : gameName = nama
        if isNullPrc  : gamePrc = harga
        if isNullCtg  : gameCtg = kategori
        if isNullRls  : gameRls = tahun_rilis

        if gameId.lower() in id.lower() and gameName.lower() in nama.lower() and gamePrc.lower() in harga.lower() and gameCtg.lower() in kategori.lower() and gameRls.lower() in tahun_rilis.lower():
            print(f"{id} | {uni(nama,40)} | {uni(harga,8)} | {uni(kategori,11)} | {uni(tahun_rilis,4)} | {stok}") 
            isNothingPrinted = False
    if isNothingPrinted :
        search(gameName.lower(),[row[1] for row in gameDs] )

def findMax(arr):
    max = arr[0]
    for i in arr:
        if i>max:
         max = i 
    return max 

def findMin(arr):
    min = arr[0]
    for i in arr:
        if i<min:
            min = i
    return min

def isIn(x,arr):
    for i in arr:
        if i == x : return True
    return False

def changeChar(idx,char,string):
    return string[:idx]+str(char)+string[idx+1:]


def search(string,arr):
    scr = [ 0 for i in range (length(arr))]
    for i in range (len(arr)):

        maxwordscore = 0
        for start in range (length(arr[i])-length(string)-1): 
            wordscore = 0
            word  = (arr[i][start:]+arr[i][:start]).lower()
            for count in range (len(string)): 
                if len(word) < len(string) : word +='`'
            
            for x in range (len(string)):
                for y in range (len(word)):
                    if string[x] == word[y] and x == y:  wordscore += 1

            if wordscore > maxwordscore : maxwordscore = wordscore
           
        scr[i] = maxwordscore

    idx = []
    for i in range (len(scr)):
        if scr[i] == findMax(scr): idx += [i]
    
    word = ""
    for i in range (len(idx)):
        if i == len(idx)-1:
            word += arr[idx[i]] 
        else: 
            word += arr[idx[i]] +" atau "

    print(f"Apakah yang anda maksud adalah {word} ?")
            

