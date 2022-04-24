from module import length

def list_game_toko(file_game):
    skema_sort = input("Skema sorting : ")
    if (skema_sort == "tahun+" or skema_sort == "tahun-"):
        # Sort game file berdasarkan tahun (ascending atau descending)
        if (skema_sort == "tahun+"):
            sort_game(file_game, "tahun", "Ascending")
        else :
            sort_game(file_game, "tahun", "Descending")
        # Print file game dengan rapi
        for i in range(1, length(file_game)//6):
            print (f"{i}.  ", end="")
            for j in range(6*i, 6*i + 6):
                if (j != 6*i + 5):
                    # Penggunaan (* " ") Hanya untuk visual output
                    if (j == 6*i + 1):
                        print(file_game[j] + (35-length(file_game[j]))*" " + "| ", end="") 
                    elif (j == 6*i + 2):
                        print(file_game[j] + (20-length(file_game[j]))*" " + "| ", end="")
                    elif (j == 6*i + 3):
                        print(file_game[j] + (8-length(file_game[j]))*" " + "| ", end="")
                    else :
                        print(f"{file_game[j]} | ", end="")
                else :
                    print(f"{file_game[j]}\n")
                
    elif (skema_sort == "harga+" or "harga-"):
        # Sort game berdasarkan harga (ascending or descending)
        if (skema_sort == "harga+"):
            sort_game(file_game, "harga", "Ascending")
        else :
            sort_game(file_game, "harga", "Descending")
        # Print file game dengan rapi
        for i in range(1, length(file_game)//6):
            print (f"{i}.  ", end="")
            for j in range(6*i, 6*i + 6):
                if (j != 6*i + 5):
                    # Penggunaan (* " ") Hanya untuk visual output
                    if (j == 6*i + 1):
                        print(file_game[j] + (35-length(file_game[j]))*" " + "| ", end="") 
                    elif (j == 6*i + 2):
                        print(file_game[j] + (20-length(file_game[j]))*" " + "| ", end="")
                    elif (j == 6*i + 3):
                        print(file_game[j] + (8-length(file_game[j]))*" " + "| ", end="")
                    else :
                        print(f"{file_game[j]} | ", end="")
                else :
                    print(f"{file_game[j]}\n")
    else :
        print("Skema sorting tidak valid")

def InsertionSort(starting_index, file_game, urutan):
        temp_array = ["" for i in range(6)]
        for i in range(starting_index, length(file_game), 6): # Akses index data yang akan diurutkan
            current_num = file_game[i]
            # Akses array game dan memasukkan data game pada array temporary
            for k in range(6):
                temp_array[k] = file_game[i+k-(starting_index-12)]
            j = i - 6
            if (urutan == "Ascending"):
                while (j >= 6 and current_num < (file_game[j]) ):
                    for k in range(6):
                        file_game[j+k+(18 - starting_index)] = file_game[j+k-(starting_index - 12)]  
                    j = j - 6
                for k in range(6):    
                    file_game[j+k+(18 - starting_index)] = temp_array[k]

            elif (urutan == "Descending"):
                while (current_num > file_game[j] and j >= 6):
                    for k in range(6):
                        file_game[j+k+(18 - starting_index)] = file_game[j+k-(starting_index - 12)]  
                    j = j - 6
                for k in range(6):    
                    file_game[j+k+(18 - starting_index)] = temp_array[k]
    
def sort_game(file_game, skema_sorting, urutan):
     if (skema_sorting == ""): # Berdasarkan Game ID Ascending
        InsertionSort(12, file_game, urutan)
     elif (skema_sorting == "tahun") :
        InsertionSort(15, file_game, urutan)
     else : # Harga
        for i in range(10, length(file_game), 6): # Ubah data harga ke integer
            file_game[i] = int(file_game[i])

        InsertionSort(16, file_game, urutan)

        for i in range(10, length(file_game), 6): # Ubah data harga kembali ke string
            file_game[i] = str(file_game[i])