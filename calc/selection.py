import random 
#rng = random.Random(seed)
def partition(ar,lt,rt,rng):
    q = rng.randint(lt,rt)
    #print(q,ar,lt,rt)
    ar[q],ar[rt] = ar[rt],ar[q]
    base = ar[rt]; i = lt
    for j in range(lt,rt):
        #print(j,ar[i],ar[j])
        if ar[j] <= base:
            ar[i],ar[j] = ar[j], ar[i]
            i += 1
    ar[i],ar[rt] = ar[rt],ar[i]
    return i

def statistic(ar,k,seed = False): #по человеческому индексу к ищет значения в массиве ар без сортировки
    #try: k
    #except: ValueError
    rng = random.Random(seed)
    aim = k - 1
    lt = 0; rt = len(ar) - 1
    while lt < rt:
        p = partition(ar,lt,rt,rng)
        if aim == p: return ar[p]
        if aim < p: rt = p - 1
        else: lt = p + 1
    return ar[lt]

#ar = [12, 71, 35, 80, 61, 50, 87, 11, 20]
#print(sorted(ar))
#print(statistic(ar,6,67)) 