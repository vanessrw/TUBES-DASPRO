import module
import list_game

def riwayat(store_mtrx, ownership_mtrx, user_id, history_mtrx):

    bought_games = list_game.games_user_bought(store_mtrx, ownership_mtrx, user_id)

    user_buy_history = []
    
    for games in bought_games:
        for histories in history_mtrx:
            if games[0] == histories[0] and user_id == histories[3]:
                user_buy_history += [[histories[0],histories[1],histories[2], '', histories[4]]]
    
    if user_buy_history == []:
        print('Maaf, kamu tidak ada riwayat pembelian game. Ketik perintah beli_game untuk membeli.')
    else:
        print(user_buy_history)
        print('Daftar game:',end='')
        module.matrix_print(user_buy_history,[0,1,2,4])