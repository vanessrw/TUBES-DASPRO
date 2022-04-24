import os
from datetime import datetime, date
from module import length
from cipher import encrypt , decrypt

def func(time):
    count = 0
    for let in str(time):
        count+=1 
    if count < 2 :
        return func("0"+str(time))
    else: 
        return str(time)
    
def save(userDs, gameDs, riwayatDs, kepemilikanDs):
    # ALGORITMA
    ds = ["game","kepemilikan","riwayat","user"]

    # input nama directory tempat penyimpanan file
    dir = input("Masukkan nama folder penyimpanan: ")
    # jika input directory kosong, nama file merupakan waktu melakukan pengesavean
    if dir == "":
        dt = datetime.today()
        dir = str(date.today()) + "_" + func(dt.hour) + func(dt.minute) + func(dt.second)
    # jika nama directory belum ada, maka dibuat directorynya
    if not os.path.exists(dir):
        os.makedirs(dir)
        os.chdir(dir)
    # jika directory sudah ada, maka dihapus seluruh file dari save-an sebelumnya
    else:
        os.chdir(dir)
        for type in ds:
            os.remove(type + ".csv")

    # agar estetik
    print("Saving...")
    
    # sebelum di store di file, password di encrypt terlebih dahulu
    for i in range (length(userDs)) :  userDs[i][3] = encrypt(userDs[i][3],3,7)

    # memasukkan setiap data yang masih dalam variabel ke file 
    for type in ds:
        with open(type + ".csv", "x") as f:
            # locals() untuk mengubah string menjadi variable
            matrix = locals()[type + "Ds"]
            for row in matrix:
                string = ""
                for word in row:
                    string += word + ";"
                f.write(string +"\n")
    print(f"Data telah disimpan dalam folder {dir}!")
    os.chdir("..")

    # password pada matrix di decrypt kembali
    for i in range (length(userDs)) :  userDs[i][3] = decrypt(userDs[i][3],3,7)

if __name__ == "__main__":
    save()
        