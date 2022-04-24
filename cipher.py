from module import *
Arr = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 
    'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 
    'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 
    'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 
    'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '!', '"', '#', 
    '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', 
    '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', 
    '^', '_', '`', '{', '|', '}', '~',' ']

def findOrd(char,Arr):

    for i in range (length(Arr)):
        if char == Arr[i]:
            return i

def findChar(ord,Arr):

    idx = ord % length(Arr)
    return Arr[idx]

def encrypt(word,n,x):

    global Arr
    newArr = Arr[n%length(Arr):length(Arr)]+Arr[:n%length(Arr)]
    ord = []
    for i in range (length(word)):
        ord += [int(x) * i + findOrd(word[i],newArr)]
    
    newWord = ''
    for i in ord: 
        newWord += findChar(i,Arr)
    newWord = newWord[n%length(newWord):length(newWord)] + newWord[:n%length(newWord)]
    return newWord

def decrypt(word,n,x): 

    global Arr
    newArr = Arr[n%length(Arr):length(Arr)]+Arr[:n%length(Arr)]
    word = word[length(word)-n%length(word):length(word)] + word[:length(word)-n%length(word)]
    ord = []
    for i in range (length(word)) : 
        ord+= [findOrd(word[i],Arr) - int(x) * i ]

    newWord = ""
    for i in ord: 
        newWord += findChar(i,newArr) 
    return newWord

