# Spesifikasi Program F08 - Membeli Game
import module
from datetime import date

def buy_game(store_mtrx, ownership_mtrx, user_mtrx, history_mtrx, user_id):

    current_year = str(date.today().year)
    game_in_store = False

    game_bought = input('Masukkan ID Game: ')   # ID Game yang dibeli
    
    for games in store_mtrx:
        if games[0] == game_bought:
            print()
            game_in_store = True
            break
    if game_in_store:
        found = False
        ownership_idx = 0
        store_length = module.length(store_mtrx)
        ownership_length = module.length(ownership_mtrx)
        user_length = module.length(user_mtrx)

        # Searching for specified games index in the store_mtrx
        for games_idx in range(store_length):
            if store_mtrx[games_idx][0] == game_bought:
                chosen_game_idx = games_idx
                break    # Terminate loop
        
        # Searching if user already have the game or not
        while not found and ownership_idx < ownership_length:
            if ownership_mtrx[ownership_idx][0] == game_bought and ownership_mtrx[ownership_idx][1] == user_id:
                found = True
            ownership_idx += 1

        # Searching for specified user index in the user_mtrx
        for users_idx in range(user_length):
            if user_mtrx[users_idx][0] == user_id:
                chosen_user_idx = users_idx
                break

        if found:
            print('Anda sudah memiliki Game tersebut')
        else:
            if int(store_mtrx[chosen_game_idx][5]) == 0:
                print('Stok game sedang habis!')
            else:
                if int(store_mtrx[chosen_game_idx][4]) <= int(user_mtrx[chosen_user_idx][5]):
                    saldo = int(user_mtrx[chosen_user_idx][5])
                    harga = int(store_mtrx[chosen_game_idx][4])
                    print(f'Game \"{store_mtrx[chosen_game_idx][1]}\" berhasil dibeli!')
                    print("Saldo sekarang:", saldo - harga)

                    ownership_mtrx += [[store_mtrx[chosen_game_idx][0],user_mtrx[chosen_user_idx][0]]]
                    history_mtrx += [[store_mtrx[chosen_game_idx][0],store_mtrx[chosen_game_idx][1],store_mtrx[chosen_game_idx][4],user_mtrx[chosen_user_idx][0],current_year]]
                    store_mtrx[chosen_game_idx][5] = str(int(store_mtrx[chosen_game_idx][5]) - 1)
                    user_mtrx[chosen_user_idx][5] = str(int(user_mtrx[chosen_user_idx][5]) - int(store_mtrx[chosen_game_idx][4]))
                else:
                    print('Saldo tidak cukup, gagal membeli game.')

    else:
        print('ID Game tidak ditemukan. Ketik \"list_game_toko\" untuk melihat list game yang ada.\n')

    return (user_mtrx,ownership_mtrx,history_mtrx)