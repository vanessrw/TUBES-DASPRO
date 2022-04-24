# F12 - Top Up Saldo

import module as module

def isUsernameAvail(inputUsername, data_user) :

    usernameAvail = 0
    for i in range(module.length(data_user)) :
        if data_user[i][1] == inputUsername :
            usernameAvail += 1
        else :
            pass
    
    if usernameAvail != 0 :
        return True
    else :
        return False


def searchLoginId(data_user, inputUsername):

    id = 0
    for i in range(module.length(data_user) ):
        if (inputUsername == data_user[i][1]):
            id = data_user[i][0]
    return int(id)


def isSaldoValid(inputUsername, inputSaldo, data_user):

    SaldoFinalTemp = int(data_user[searchLoginId(
        data_user, inputUsername)][5]) + inputSaldo
    
    if (SaldoFinalTemp < 0):
        return False
    else:
        return True


def topUpSaldo(data_user): 

    inputUsername = input("Masukkan username : ")
    inputSaldo = int(input("Masukkan saldo : "))
    
    # Apabila username tidak ditemukan
    if (not isUsernameAvail(inputUsername, data_user)):
        print(f'Username "{inputUsername}" tidak ditemukan.')
        return data_user
    
    # Apabila masukan saldo tidak valid
    if (not isSaldoValid(inputUsername, inputSaldo, data_user)):
        print(f"Masukan tidak valid")
        return data_user
    
    # Nilai akhir dari saldo user
    if (inputSaldo >= 0):
        statusTopup = "bertambah"
    else:
        statusTopup = "berkurang"

    data_user[searchLoginId(data_user, inputUsername)][5] = int(
        data_user[searchLoginId(data_user, inputUsername)][5]) + inputSaldo
    print(
        f'Top up berhasil. Saldo {data_user[searchLoginId(data_user, inputUsername)][2]} {statusTopup} menjadi {data_user[searchLoginId(data_user, inputUsername)][5]}.')
    return data_user