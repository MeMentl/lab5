from calc import arrays

# descending = 1 - по убыванию,
# descending = 0 - по возрастанию
def isNotSorted(a,b,descending):
    '''нужно менять или нет пару значений'''
    if descending:
        return a<b #1 - надо менять
    else:
        return a>b #1 - надо менять
    
def b4(a,b,descending):
    if descending:
        return a>b 
    else:
        return a<b 

def quick(ar,descending = 0):
    arrange(ar,0,len(ar)-1,descending)
    return ar

def arrange(ar,lt,rt,descending):
    if lt >= rt:
        return
    base = ar[(lt + rt) // 2]
    i = lt; j = rt
    while i <= j:
        while b4(ar[i],base,descending): i += 1
        while b4(base,ar[j],descending): j -= 1
        if i <= j:
            ar[i],ar[j] = ar[j], ar[i]
            i += 1; j -= 1
    arrange(ar,lt,j,descending)
    arrange(ar,i,rt,descending)

def merge(ar,descending = 0):
    arrmerge(ar,0,len(ar) - 1,descending)
    return ar

def arrmerge(ar,lt,rt,descending):
    if lt >= rt: return
    mid = (lt + rt) // 2
    arrmerge(ar,lt,mid,descending)
    arrmerge(ar,mid + 1,rt,descending)
    drain(ar,lt,mid,rt,descending)

def drain(ar,lt,mid,rt,descending):
    rez = []
    i = lt; j = mid + 1
    while i <= mid and j <= rt:
        if b4(ar[j],ar[i],descending):
            rez.append(ar[j]); j += 1
        else:
            rez.append(ar[i]); i += 1
    rez = rez + ar[i:mid+1]
    rez = rez + ar[j:rt+1]
    ar[lt:rt+1] = rez

def sift(ar,i,size,descending):
    while True:
        chosen = i
        for c in [2 * i + 1, 2 * i + 2]:
            if c < size:
                if b4(ar[chosen],ar[c],descending):
                    chosen = c
        if chosen == i: return
        ar[i],ar[chosen] = ar[chosen],ar[i]
        i = chosen

def heap(ar,descending = False):
    n = len(ar)
    for i in range(n//2-1,-1,-1):
        sift(ar, i, n, descending)
    for kon in range(n-1,0,-1):
        ar[0],ar[kon] = ar[kon],ar[0]
        sift(ar,0,kon,descending) 
    return ar

#a = [4 ,8 ,6, 7, 3, 9, 6, 9 , 4, 1]
#merge(a,1)
#quick(a,1)
#heap(a,1)
#print(a)

def bubble(a, descending=0): #des 0 - по возрастанию
    n = len(a)
    for i in range(n - 1):
        swapped = 0  # нет обменов    
        for j in range(n - 1 - i):
             if isNotSorted( a[j],a[j+1],descending):
                 a[j], a[j + 1] = a[j + 1], a[j]
                 swapped = 1 # есть обмен        
        # Если ни одного обмена не произошло, массив уже отсортирован
        if swapped == 0:
            break
            
    return a


##print(a)
##ar = bubble(a, descending=1)
##print(ar)


def selection(ar,descending=0):
    n = len(ar)
    for i in range(0, n - 1):
        best = i
        for j in range(i+1, n):
            if isNotSorted( ar[best],ar[j],descending): #выплюнула 1 - меняем
                best = j
        ar[i], ar[best] = ar[best],ar[i]
    return ar
##print(len(a))
##print(len(selection(a,1)))

def insertion(ar,descending = 0):
    n = len(ar)
    for i in range(1, n):
        cur = ar[i]
        j = i
        while j > 0 and isNotSorted(ar[j-1],cur,descending):
            ar[j] = ar[j-1]
            j = j-1
        ar[j] = cur
    return ar
'''print(insertion(a,0))'''

def counting(ar,descending = 0):
    min_value = min(ar)
    max_value = max(ar)
    counters = [0] * (max_value - min_value + 1)
    for n in ar:
        counters[n - min_value] += 1
    k = 0
    for i in range(len(counters)):
        while counters[i] > 0:
            ar[k] = i + min_value
            k += 1
            counters[i] -= 1
    return ar
 
#ar = counting(a)
#print(ar)
 
def search(ar,n):
    lt = 0
    rt = len(ar) - 1
    while lt <= rt:
        mid = (lt + rt) // 2
        if ar[mid] == n:
            return mid
        if ar[mid] < n:
            lt = mid+1
        else:
            rt = mid-1
    return None

               
METHODS = {
    "bubble":     bubble,
    "insertion":   insertion,
    "selection":  selection,
    "counting":   counting,
    "quick":  quick,
    "merge":  merge,
    "heap": heap 
}

##print(a)
##b=a.copy(); ar = METHODS["bubble"](b);
##print(ar)
####print(search(b,6))
##
##print(hand_search(7,b))


def read_arr(line, fileName=None):
    ''' Преобразует числа из файла в массив int, если указан FileName,
        иначе из line (клавиатура stdin)'''
    ar = []
    if fileName is not None:
        try:
            with open(fileName, 'r', encoding="utf-8-sig") as file:
                line= file.readline()
        except Exception as e:
                raise ValueError(f"{e}")
    
            
    for word in line.split():
        try:
            n = int(word)
            if  n < arrays.MIN_VALUE  or n > arrays.MAX_VALUE:
                raise ValueError(f"значение вне диапазона {MIN_VALUE} {MAX_VALUE}")
            ar.append(n)
        except ValueError:
            raise ValueError(f"{word} не является числом")
    #ar = [0]*(MAX_COUNT +1)    
    if len(ar) > arrays.MAX_COUNT:
                raise ValueError(f"количество значений больше допустимого {MAX_COUNT}")    
    return ar

##line ="-51 12 23 56 84"
##ar = read_arr(line)
##print(ar)

##ar = read_arr(None,"..\\small.txt")
#print(ar)




#hand_sort(None)
