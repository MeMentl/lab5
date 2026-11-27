import sys
from cli  import create_parser
from calc import equation
from calc import stats
from calc import series
from calc import arrays
from calc import sorting
from calc import selection

# > solve
# > solve -a 1 -b -3 -c 2
def hand_solve(args):
    ''' Обработчик для команды solve, args - АКС
        Получает коэффициенты из консоли или  АКС
        Проверяет коэффициенты на тип и количество,
        вызывает функцию решения квадратного уравнения
        Выводит результаты'''
    
    arg = [args.a, args.b, args.c]
    cnt = arg.count(None)
    print("Решение квадратного уравнения")
    if cnt == 3:
        try:
            a = int(input("введите А: "))
            b = int(input("введите B: "))
            c = int(input("введите C: "))
        except ValueError:
            raise ValueError("Коэффициент не является целым числом")
    elif cnt == 0:  # АКС
        a, b, c = args.a, args.b, args.c
    else:
        raise ValueError("Укажите три коэффициента или ни одного")

    equation.solve_check({"A": a, "B": b, "C": c})
    kind, d, roots = equation.solve(a, b, c)
    
    print(f"уравнение {kind}")
    if d is not None:
        print(f"дискриминант: {d}")
    if len(roots) == 2:
        print(f"x1 = {roots[0]:.3f}")
        print(f"x2 = {roots[1]:.3f}")
    elif len(roots) == 1:
        print(f"x = {roots[0]:.3f}")
    else:
        print("действительных корней нет")
    return 0

def get_num(source):
    ''' Преобразует числа из source файла в массив (float)'''
    ar = []
    for line in source:
        for word in line.split():
            try:
                ar.append(float(word))
            except ValueError:
                raise ValueError(f"{word} не является числом")
    return ar

# > stats --input numbers.txt 
# > stats (с клавиатуры через cmd ^Z)
# > type numbers.txt | python mathtool.py stats (из конвейера)
def hand_stats(args):
    ''' Обработчик для команды stats, args - АКС
        Получает значения ряда values из stdin или файла, проверяет их,
        и через REPORT выводит результат'''
    if args.input is not None: # из файла
        try:
            with open(args.input, encoding="utf-8-sig") as handle:
                values = get_num(handle)
        except OSError:
            raise OSError(f"Файл {args.input} не открывается")
    else: # из потока
        values = get_num(sys.stdin)

    stats.stats_check(values)

    for label, function, form in stats.REPORT:
        value = function(values)
        if value is None:
            print(f"{label}: НЕ СУЩЕСТВУЕТ")
        else:
            print(f"{label}: {value:{form}}")
    return 0

#> series --func sqplus --terms 6
#> series --func sqplus --eps 0.0001
#> series --func third  --terms 6
#> series --func third  --eps 0.0001
def hand_series(args):
    ''' Обработчик для команды series, 
        Получает формулзначения ряда из args - АКС, проверяет их,
        и через FORMULAS выбирает слагаемое и функцию и выполяет ее,
        выводит результат'''
    series.check_params(args.terms, args.eps)
    
    term, formula = series.FORMULAS[args.func]
    
    if args.terms is not None:
        rez = series.sum_terms(term, args.terms)
        count = args.terms
    else:
        rez, count = series.sum_eps(term, args.eps)
    print(formula)
    print(f"Слагаемых: {count}")
    print(f"Сумма ряда: {rez:.4f}")
    return 0

# > integrate --func ratio --from 0 --to 20 --steps 1000
# > integrate --func root --from -5 --to 5 --steps 1000
def hand_integrate(args):
    ''' Обработчик для команды integrate, 
        Получает формулзначения ряда из args - АКС, проверяет их,
        и через FUNCTIONS выбирает дипазон и функцию и выполяет ее,
        выводит результат'''
    
    integration.check_params(args.func, args.start, args.end, args.steps)

    f, formula, low, high, closed = integration.FUNCTIONS[args.func]

    rez = integration.integrate(f, args.start, args.end, args.steps)

    print(formula)
    print(f"Значение интеграла: {rez:.4f}")
    return 0

import time
import sys
def timer(sortName, operation, params):
   
    #print(params)
    #print(*params)
    start = time.perf_counter()    
    ar = operation(*params)
    
    extime = time.perf_counter() - start
    print(f"Операция {sortName} выполнена за {extime:.6f} сек.", file=sys.stderr)
    return ar


#> fill -c 20 --min -10 --max 10 --seed 1 -o small.txt 
#> fill --count 20 --min -10 --max 10 --seed 1 --output small.txt 
def hand_fill(args):
    ''' Обработчик для команды hand, args - АКС
        Получает коэффициенты из консоли или  АКС
        Проверяет коэффициенты на тип и количество,
        вызывает функцию заполнения массива случайными числами
        Выводит результаты'''
    print(args)
    print("Генерация списка")
    if args.c is None: cnt = args.count
    else: cnt = args.c

    fileName=None
    if args.o is None and args.output is not None:
        fileName = args.output
    elif args.o is not None and args.output is  None:
        fileName = args.o
    
    #print(fileName)
    arrays.fill_check(cnt,args.min,args.max,args.seed)
    a = arrays.fill(cnt,args.min,args.max,args.seed)
    if fileName is None:
        print(a)
    else:
        arrays.writeFile(fileName,a)
    return 0

#>sort -m bubble --order asc -i small.txt -o kapycta.txt
def hand_sort(args):
    filenamei = None
    if args.i is not None:
        filenamei = args.i
    elif args.input is not None:
        filenamei = args.input
    filenameo = None
    if args.o is not None:
        filenameo = args.o
    elif args.output is not None:
        filenameo = args.output
    if args.m is None:
        sortname = args.method
    else:
        sortname = args.m
    descending = 0 #по умолчанию - по возрастанию
    if args.order is not None:
        if args.order == 'desc':
            descending = 1 # по убыванию
    
    ar = sorting.read_arr(None,"small.txt")
    oper = sorting.METHODS[sortname] 
    ar = oper(ar,descending)
    arrays.writeFile(filenameo,ar)
    #a= timer(sortName,oper,[ar,descending])
    #print(f"Отсортированный массив: {sar}")
    print("Сортировка успешно завершена!")
    timer(sortname,oper,[ar,descending])
    return 0

#>search -v --value -i --input
def hand_search(args):
    #value,ar
    print(args)
    print("поиск значения")
    if args.v is None:
        value = args.value
    else:
        value = args.v
    filename = None
    if args.i is not None:
        filename = args.i
    elif args.input is not None:
        filename = args.input
    print(value,filename)

    if abs(value) > arrays.MAX_SEARCH:
        raise ValueError(f"модуль искомого не больше {arrays.MAX_SEARCH}")
    
    # прочитать_массив(--input)
    ar = sorting.read_arr(None, filename)
    print(len(ar))
      #ar = [1,2,3,4,5,6,7,8,9,10]
    for i in range(1,len(ar)):
        if ar[i-1] > ar[i]:
            raise ValueError("массив не упорядочен по возрастанию")
    print("sorted ok")
    
    ind = sorting.search(ar,value)
    if ind is None:
        raise ValueError(f"Значение {value} не найдено.")
        return 1 # ?
    else:
        print(f"Значение {value} имеет элемент с индексом {ind + 1}")
        return 0

#python mathtool.py select -k 4 -i small.txt --seed 1
def hand_select(args):
    filenamei = None
    if args.i is not None:
        filenamei = args.i
    elif args.input is not None:
        filenamei = args.input
    if args.k is None:
        k = args.rank
    else:
        k = args.k
    if args.seed is not None:
        seed = args.seed
    else:
        seed = 0
     
    ar = sorting.read_arr(None,filenamei)
    print('Значение порядковой статистики',selection.statistic(ar,k,seed)) 
    return 0

#python mathtool.py shuffle -i kapycta.txt --seed 1 -o shuffled.txt
def hand_shuffle(args):
    filenamei = None
    if args.i is not None:
        filenamei = args.i
    elif args.input is not None:
        filenamei = args.input
    filenameo = None
    if args.o is not None:
        filenameo = args.o
    elif args.output is not None:
        filenameo = args.output
    if args.seed is not None:
        seed = args.seed
    else:
        seed = 0
     
    ar = sorting.read_arr(None,filenamei)
    print(args)
    ar = arrays.shuffle(ar,seed)
    if filenameo is not None:
        arrays.writeFile(filenameo,ar)
        print('Массив перемешан и записан в файл', filenameo)
    else:
        print('Массив перемешан',ar[:20]) 
    return 0

''' Сопоставить каждой команде соответствующий обработчик '''
HANDLERS = {
    "solve":     hand_solve,
    "stats":     hand_stats,
    "series":    hand_series,
    "integrate": hand_integrate,
    "fill":      hand_fill,
    "sort":      hand_sort,
    "search":    hand_search,
    "select":    hand_select,
    "shuffle":   hand_shuffle
}

def main(argv):
    ''' Разобрать аргументы командной строки (АКС).
        По команде вызвать соответствующий обработчик функции '''   
    parser = create_parser()
    args = parser.parse_args(argv)
    if args.command is None:
        parser.print_help()
        return 0
    try:
        return HANDLERS[args.command](args)
    except (ValueError, OSError) as error:
        print(f"ОШИБКА: {error}", file=sys.stderr)
        return 1
    
if __name__ == "__main__":
    ''' вызвать функцию main как единственную точку входа в программу,
        вернуть код ошибки,
        отладочная печать для теста'''
    #print('Test ')
    print(f"Команда: ", ' '.join(sys.argv[1:]))
    #print('stdin: ', '<пусто>')
    #print('stdout: ', '')  
    code = main(sys.argv[1:])
    #print('stderr: ', '<пусто>')
    print('Код возврата: ',code)
    sys.exit(code)
    
    # sys.exit(main(sys.argv[1:]))
