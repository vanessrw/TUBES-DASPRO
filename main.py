
from tictactoe import tic_tac_toe

def main():  
    from register import register; from login import login; from tambahgame import TambahGame; from ubahgame import changeGame; from ubah_stok import ubah_stok; from list_game_toko import list_game_toko;
    from buy_game import buy_game; from list_game import list_game; from search_my_game import search_my_game; from search_game_at_store import search_game_at_store; from topupsaldo import topUpSaldo
    from riwayat import riwayat; from help import help_; from load import load; from save import save; from exit import exit ; from kerangajaib import magicConchShell

    userDs, gameDs, riwayatDs, kepemilikanDs = load()
    userArr = [None, None, None, None, 'guest', None]
    inpAdmin = ["register","tambah_game","ubah_game","ubah_stok","topup"]
    inpUser = ["buy_game","list_game","search_my_game","riwayat"] 
    inpGuest = ["login","help","tictactoe", "kerangajaib", "exit"]  
    inpAdminAndUser = ["login","list_game_toko","search_game_at_store","help","save","exit"]

    print ('Selamat datang di "Toko Game BNOMO !" ^o^')
    print ("Ketik perintah kamu atau ketik `help` untuk melihat daftar perintah")
    cont = True
    while cont:
        check = False
        print()
        header = ">>> "
        inp = input(header).lower()
        if inp in inpAdmin or inp in inpUser or inp in inpAdminAndUser:
            if userArr[4] == "guest":
                if inp in inpGuest : check = True
                else: 
                    print("Mohon lakukan login terlebih dahulu")


            elif userArr[4] == "user" :
                if (inp in inpUser or inp in inpAdminAndUser):
                    check = True 
                else: 
                    print("Maaf, akses akan perintah tersebut hanya terbatas pada admin. >.<")


            elif userArr[4] == "admin" :
                if (inp in inpAdmin or inp in inpAdminAndUser):
                    check = True
                else: 
                    print("Maaf, akses akan perintah tersebut hanya terbatas pada user. >.<")

            if check: 
                if inp == ("register"):
                    userDs = register(userDs)
                elif inp == ("login"):
                    userArr = login(userDs,userArr) 
                elif inp == ("tambah_game"):
                    gameDs = TambahGame(gameDs)
                elif inp == ("ubah_game"):
                    gameDs = changeGame(gameDs)
                elif inp == ("ubah_stok"):
                    gameDs = ubah_stok(gameDs)
                elif inp == ("list_game_toko") : 
                    list_game_toko(userDs)
                elif inp == ("buy_game"):
                    userDs , kepemilikanDs , riwayatDs = buy_game(gameDs,kepemilikanDs,userDs,riwayatDs,userArr[0])
                elif inp == ("list_game") : 
                    list_game(gameDs,kepemilikanDs,userArr[0])
                elif inp == ("search_my_game") : 
                    search_my_game(userArr,kepemilikanDs,gameDs)  
                elif inp == ("search_game_at_store") : 
                    search_game_at_store(gameDs)
                elif inp == ("topup") : 
                    userDs = topUpSaldo(userDs)
                elif inp == ("riwayat") :
                    riwayat(gameDs, kepemilikanDs, userArr[0], riwayatDs)
                elif inp == ("help") : 
                    help_(userArr)
                elif inp == ("save"):
                    save(userDs, gameDs, riwayatDs, kepemilikanDs)
                elif inp == ("exit"):
                    exit(userDs, gameDs, riwayatDs, kepemilikanDs)
                    check = False
                elif inp == ("kerangajaib"):
                    magicConchShell()
                elif inp == ("tictactoe"):
                    tic_tac_toe()

        else:
            print("Perintah salah, \"help\" untuk lihat daftar perintah.")
    exit(userDs, gameDs, riwayatDs, kepemilikanDs, userArr[4])

if __name__ == "__main__":
    main()

