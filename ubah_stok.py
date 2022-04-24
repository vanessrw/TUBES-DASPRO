import module

def ubah_stok(arr):
    id_input = input("Masukkan ID game: ")
    ketemu = False
    for line in arr:
        if (line[0] == id_input):
            ketemu = True
            stok_barang = int(line[5])
            nama_game = line[1]
            id_game = line[0]
            break
    if (ketemu == True):
        for line in arr:
            if (line[0] == id_input):
                add_stok = int(input("Masukkan jumlah: "))
                stok_now = stok_barang + add_stok
                if add_stok >= 0:
                    line[5] = stok_now
                    print(f"Stok game {nama_game} berhasil ditambahkan. Stok sekarang: {stok_now}")
                    return

                else:
                    if stok_now >= 0:
                        line[5] = stok_now
                        print(f"Stok game {nama_game} berhasil dikurangi. Stok sekarang: {stok_now}")
                        return

                    else:
                        print(f"Stok game kurang, stok {nama_game} gagal dikurangi ! Stok sekarang: {stok_now - add_stok} (< 10)")
    else:
        print("Tidak ada game dengan ID tersebut")