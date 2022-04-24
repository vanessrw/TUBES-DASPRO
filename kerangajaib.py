from calendar import c
import time 

def magicConchShell() :
    inputQuestion = input("Tanya kerang ajaib : ")

    a = 1
    c = 1
    m = 5
    x = time.time()
    number = (((a*x) + c) % m)

    randomNumber = number

    if (randomNumber <= 0.5555) :
        print("Ya.")
    elif (0.5555 < randomNumber <= (2*0.5555)) :
        print("Tidak.")
    elif ((2*0.5555) < randomNumber <= (3*0.5555)) :
        print("Bisa Jadi.")
    elif ((3*0.5555) < randomNumber <= (4*0.5555)) :
        print("Mungkin.")
    elif ((4*0.5555) < randomNumber <= (5*0.5555)) :
        print("Tentunya.")
    elif((5*0.5555) < randomNumber <= (6*0.5555)):
        print("Tidak mungkin.")
    else :
        print("Tanya lagi nanti.")
    return number

