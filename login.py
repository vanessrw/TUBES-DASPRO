# F03 - LOGIN
import module as module

binomoAccess = [None, None, None, None, 'guest', None]


def isUsernameAvail(inputUsername, data_user) :

    usernameAvail = 0
    for i in range(module.length(data_user)) :
        if data_user[i][1] == inputUsername :
            usernameAvail += 1
        else :
            pass
        
    # Mengembalikan nilai berupa boolean
    if usernameAvail != 0 :
        return True
    else :
        return False
    
def isPasswordValid(inputUsername, inputPassword, data_user) :

    userTemp = []
    for i in range(module.length(data_user)):
        if (data_user[i][1]) == inputUsername :
            userTemp = data_user[i]
    
    # Mengembalukan nilai berupa boolean
    if (inputPassword == userTemp[3]):
        return True
    else:
        return False
  
def searchLoginId(data_user, inputUsername):

    id = 0
    for i in range(module.length(data_user) ):
        if (inputUsername == data_user[i][1]):
            id = data_user[i][0]
    return int(id)


def login(data_user,binomoAccess) :

    inputUsername = input("Masukkan username : ")
    inputPassword = input("Masukkan password : ")
    
    # Ketika kondisi tidak terpenuhi, ooping untuk melakukan input ulang sampai valid
    while not isUsernameAvail(inputUsername, data_user) or not isPasswordValid(inputUsername, inputPassword, data_user):
        if inputUsername != '' and inputPassword != '' :
            print("Password atau username salah atau tidak ditemukan")
            inputUsername = input("Masukkan username : ")
            inputPassword = input("Masukkan password : ")
        if module.length(inputUsername) == 0 or module.length(inputPassword) == 0 :
            print("Mohon masukkan password dan username Anda")
            inputUsername = input("Masukkan username : ")
            inputPassword = input("Masukkan password : ")

    print(f'Halo {data_user[searchLoginId(data_user, inputUsername)][2]}! Selamat datang di "Binomo".')

    binomoAccess = data_user[searchLoginId(data_user, inputUsername)]
    return binomoAccess