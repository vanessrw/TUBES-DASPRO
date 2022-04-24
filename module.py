def isInArr(elm,Arr):
    for element in Arr:
        if element == elm: return True
    return False

def findMax(arr):
    max = arr[0]
    for i in arr:
        if i>max:
         max = i 
    return max 

def findMin(arr):
    min = arr[0]
    for i in arr:
        if i<min:
            min = i
    return min

def length(string) :
    length = 0
    for i in string :
        length += 1
    return length 

def isInWord(string,word):
    for start in range (length(word)):
        newWord = ""
        for idx in range (start,length(word)):
                newWord += word[idx]
                if string == newWord: return True
    return False


def read(file):
    dataset= open(str(file)+".csv").readlines()
    matrix = []
    for row in dataset:
        arr = []
        word = ''
        for letter in row:
            if letter != '"':
                if letter != ';':
                    word += letter
                else:
                    arr += [word]
                    word = ''
        matrix += [arr]
    return 

def ascend_sort(my_mtrx,data_idx):

    mtrx_length = length(my_mtrx)
    temp_mtrx = my_mtrx
    if mtrx_length > 1:
        check = 0
        any_swap = True

        while check < mtrx_length and any_swap:
            any_swap = False
            for idx in range(mtrx_length - 1, check, -1):
                if int(temp_mtrx[idx][data_idx]) < int(temp_mtrx[idx - 1][data_idx]):
                    temp_value = temp_mtrx[idx]
                    temp_mtrx[idx] = temp_mtrx[idx - 1]
                    temp_mtrx[idx - 1] = temp_value
                    any_swap = True

                else:
                    continue
            check += 1
    return temp_mtrx

def descend_sort(my_mtrx,data_idx):

    mtrx_length = length(my_mtrx)
    temp_mtrx = my_mtrx
    if mtrx_length > 1:
        check = 0
        any_swap = True

        while check < mtrx_length and any_swap:
            any_swap = False
            for idx in range(mtrx_length - 1, check, -1):
                if int(temp_mtrx[idx][data_idx]) > int(temp_mtrx[idx - 1][data_idx]):
                    temp_value = temp_mtrx[idx]
                    temp_mtrx[idx] = temp_mtrx[idx - 1]
                    temp_mtrx[idx - 1] = temp_value
                    any_swap = True

                else:
                    continue
            check += 1
    return temp_mtrx

def max_length(my_mtrx, header_idx):

    length_bound = 0
    for elements in my_mtrx:
        curr_length = length(elements[header_idx])
        if curr_length > length_bound:
            length_bound = curr_length
    return length_bound

def matrix_print(my_mtrx, header_list):

    category_char = max_length(my_mtrx, 2)  
    price_char = max_length(my_mtrx, 4) 
    mtrx_length = length(my_mtrx)

    for elements_idx in range(mtrx_length):
        space_game_name = ''
        space_category = ''
        space_price = ''

        for i in range(category_char - length(my_mtrx[elements_idx][2])):
            space_category += ' '
        for i in range(price_char - length(my_mtrx[elements_idx][4])):
            space_price += ' '

        print(f'\n{uni(str(elements_idx + 1),3)}. {my_mtrx[elements_idx][header_list[0]]} ', end='')
        for idx in header_list:
            if idx > 0:
                if idx == 1:
                    print(f"| {uni(my_mtrx[elements_idx][idx],40)}", end=" ")
                    print(space_game_name, end='')
                else:
                    print(f'| {my_mtrx[elements_idx][idx]}', end=' ')
                    if idx == 2:
                        print(space_category, end='')
                    elif idx == 4:
                        print(space_price, end='')
    print()

def uni(str,n):

    newStr=""
    if length(str) > n :
        newStr = slice(str,0,n-3) + "..."
    else:
        newStr = str
        for i in range (n-length(str)):
            newStr+=' '
    return newStr

def slice(word,start,end):

    newWord =""
    for idx in range (start,end):
        newWord+=word[idx]
    return newWord