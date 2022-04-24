def help_(userArr):
    if userArr == []: 
        print("-------------------------------- HELP --------------------------------")
        print("1. login - melakukan login kedalam sistem")
        print("2. help - menampilkan bantuan atau penjelasan terkait command yang ada")
    
    elif userArr[4] == "admin":
        print("-------------------------------- HELP --------------------------------")
        print("1. register - mendaftarkan pengguna baru kedalam sistem")
        print("2. login - melakukan login kedalam sistem")
        print("3. tambah_game - menambahkan game baru kedalam toko")
        print("4. ubah_game - mengubah informasi game yang telah ada di toko")
        print("5. ubah_stok - mengubah stok sebuah game pada toko")
        print("6. list_game_toko - menampilkan data game toko yang telah di sorting")
        print("7. search_game_at_store - mencari game di toko berdasarkan parameter")
        print("8. topup - menambahkan saldo kepada user")
        print("9. help - menampilkan bantuan atau penjelasan terkait command yang ada")
        print("10.save - menyimpan perubahan yang telah dibuat")
        print("11.exit - keluar dari program")
    else: 
        print("-------------------------------- HELP --------------------------------")
        print("1. login - melakukan login kedalam sistem")
        print("2. list_game_toko - menampilkan data game toko yang telah di sorting")
        print("3. buy_game - membeli game yang ada di toko")
        print("4. list_game - melihat game yang dimiliki user")
        print("5. search_my_game - mencari game yang dimiliki dari ID dan tahun rilis")
        print("6. search_game_at_store - mencari game di toko berdasarkan parameter")
        print("7. riwayat - melihat riwayat pembelian")
        print("8. help - menampilkan bantuan atau penjelasan terkait command yang ada")
        print("9. save - menyimpan perubahan yang telah dibuat")
        print("10.exit - keluar dari program")

if __name__ == "__main__":
    help_(userArr)
