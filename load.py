import argparse
import os
import sys
from cipher import *
from module import *


def read(file):

    dataset= open(str(file)+".csv").readlines()
    matrix = []
    for row in dataset:
        arr = []
        word = ''
        for letter in row:
            if letter != ';':
                word += letter
            else:
                arr += [word]
                word = ''
        if arr!=[]: matrix += [arr]
    return matrix

def load():

    parser = argparse.ArgumentParser()
    parser.add_argument("dir", help="Directory name")
    if length(sys.argv) == 1:
        print('Tidak ada nama folder yang diberikan!')
    dir = parser.parse_args().dir
    path = str(os.getcwd()) + "/" + dir
    if os.path.exists(dir):
        os.chdir(path)
        print("Loading...")

        # Loading file di selected directory
        userDs = read("user")
        gameDs = read("game")
        riwayatDs = read("riwayat")
        kepemilikanDs = read("kepemilikan")
        for i in range (length(userDs)) :  userDs[i][3] = decrypt(userDs[i][3],3,7) # decrypting
        print("Selamat datang di antarmuka \"Binomo\"")
        os.chdir("..")
    else:
        print("Folder \""+ str(dir) +"\" tidak ditemukan.")
    return (userDs,gameDs,riwayatDs,kepemilikanDs)

if __name__ == "__main__":
    load()