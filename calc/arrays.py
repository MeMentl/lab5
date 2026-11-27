import random
MIN_VALUE  = -1000
MAX_VALUE  =  100
MAX_COUNT  = 1_000_000
MAX_SEARCH = 1000


#def check_params():
'''В calc/arrays.py задать MIN_VALUE = -100, MAX_VALUE = 100,
MAX_COUNT = 1_000_000 и MAX_SEARCH = 1000.
Использовать их при проверках и в значениях параметров по умолчанию.'''
# проверка коэфф.
def fill_check(count,low,high,seed):

        if not (1 <= count <= MAX_COUNT):
        #if count < 1 and count > MAX_COUNT:           
            raise ValueError(f"количество элементов {count} вне допустимого диапазона")
        if low is not None:
            if low < MIN_VALUE:
                raise ValueError(f"нижняя граница меньше допустимого значения {MIN_VALUE}")
        if high is not None:
            if high > MAX_VALUE :
                raise ValueError(f"верхняя граница больше допустимого значения {MAX_VALUE}")
        if low is not None and high is not None:
            if low > high:
                raise ValueError(f"нижняя граница {low} больше верхней границы {high}")
        if seed is not None:
            if not (MIN_VALUE <= seed <= MAX_VALUE):
                raise ValueError(f"начальное значение генератора {seed} вне допустимого диапазона")

#fill_check(10,6,5,-2000)

  
# seed=0 - случайные числа, иначе - псевдо     
def fill(count, low, high, seed):
    if low is None:  low = MIN_VALUE
    if high is None: high = MAX_VALUE
    if seed is None: seed = 0 
    
    #print(count, low,high,seed)
    if seed:
        random.seed(seed)
    else:
        random.seed()
        
    ar= []
    for i in range(count):  
        n = random.randint(low, high)  
        ar.append(n)
    return ar

#fill_check(5,-100,100,0)
#a = fill(5,-100,100,0); print(a)
#s = " ".join(str(x) for x in a) + "\n"
#print(s)

def writeFile(fileName,ar):
    try:
      with open(fileName, 'w', encoding="utf-8-sig") as file:
        s = " ".join(str(x) for x in ar) 
        file.write(s + "\n")
##    except PermissionError:
##      raise ValueError("Недостаточно прав для записи в этот файл или папку.")
##    except OSError as e:
##      raise ValueError(f"Произошла системная ошибка при работе с файлом: {e}")
    except Exception as e:
      raise ValueError(f"{e}")
      
#writeFile("..\\small.txt", a)

def shuffle(ar,seed = False):
    rng = random.Random(seed)
    for i in range(len(ar)-1,0,-1):
        j = rng.randint(0,i)
        ar[i],ar[j] = ar[j],ar[i]
    return ar
#ar = [1,2,2,5,6,17,21]
#a = shuffle(ar,2)
#print(a)
