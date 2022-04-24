import module

def games_user_bought(store_mtrx, ownership_mtrx, user_id):

    store_length = module.length(store_mtrx)
    user_game_id = []

    for games in ownership_mtrx:
        if games[1] == user_id:
            for store_idx in range(store_length):
                if store_mtrx[store_idx][0] == games[0]:
                    user_game_id += [store_idx]
                    store_idx = store_length
  
    bought_game_by_user = []
    for store_idx in user_game_id:
        bought_game_by_user += [[store_mtrx[store_idx][0],store_mtrx[store_idx][1],store_mtrx[store_idx][2],store_mtrx[store_idx][3],store_mtrx[store_idx][4]]]
    
    return bought_game_by_user

def list_game(store_mtrx, ownership_mtrx, user_id):

    bought_game = games_user_bought(store_mtrx, ownership_mtrx, user_id)
    bought_game_length = module.length(bought_game)

    if bought_game_length == 0:
        print('Maaf, kamu belum membeli game. Ketik perintah beli_game untuk beli.')
    else:    
        print('Daftar game:',end='')
        module.matrix_print(bought_game, [0,1,2,3,4])