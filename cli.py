import argparse
from calc import series
from calc import integration
from calc import equation

def create_parser():
    parser=argparse.ArgumentParser(
        prog="mathtool",
        description="вычисление уравнений и числовых последовательностей",
        allow_abbrev=False)

    commands = parser.add_subparsers(dest="command", title="команды")

    p = commands.add_parser("solve", allow_abbrev=False, help="Решение квадратного уравнения:")
    p.add_argument("-a", type=int, help=f"коэфициент А (целое, по модулю не более {equation.MAX_VALUE})")
    p.add_argument("-b", type=int, help=f"коэфициент B (целое, по модулю не более {equation.MAX_VALUE})")
    p.add_argument("-c", type=int, help=f"коэфициент C (целое, по модулю не более {equation.MAX_VALUE})")

    p = commands.add_parser("stats", allow_abbrev=False, help="Показатели последовательности")
    p.add_argument("--input", help="файл с данными")

    p = commands.add_parser("series", allow_abbrev=False, help="Сумма ряда")
    p.add_argument("--func", required=True, choices=sorted(series.FORMULAS), help="Имя ряда:")
    group = p.add_mutually_exclusive_group(required=True) #  либо term либе eps
    group.add_argument("--terms", type=int, help="количество элементов в последовательности")
    group.add_argument("--eps", type=float, help=f"точность слагаемого (меньше {series.MAX_EPS})")

    p = commands.add_parser("integrate", allow_abbrev=False, help="Нахождение интеграла методом левых прямоугольников")
    p.add_argument("--func", required=True, choices=sorted(integration.FUNCTIONS), help="Выбрать функцию для интегрирования:")
    p.add_argument("--from", dest="start", type=float, required=True, help="нижний предел")
    p.add_argument("--to", dest="end", type=float, required=True, help="верхний предел (больше нижнего)")
    p.add_argument("--steps", type=int, required=True, help="число прямоугольников (целое)")


    p = commands.add_parser("fill", allow_abbrev=False, help="Генерация списка:")
    gr = p.add_mutually_exclusive_group(required=True) #
    gr.add_argument("--count", type=int, help=f"количество элементов, от 1 до 1 000 000")
    gr.add_argument("-c", type=int, help=f"количество элементов, от 1 до 1 000 000")    
    p.add_argument("--min", type=int, help=f"нижняя граница значений")
    p.add_argument("--max", type=int, help=f"верхняя граница значений")   
    p.add_argument("--seed", type=int, help=f"начальное значение генератора")
    gr = p.add_mutually_exclusive_group(required=False) #
    gr.add_argument("--output", type=str, help=f"файл для созданного массива")
    gr.add_argument("-o", type=str, help=f"файл для созданного массива")

    p = commands.add_parser("sort", allow_abbrev=False, help="сортировка массива")
    gr = p.add_mutually_exclusive_group(required=True) #обязательный
    gr.add_argument("--method", type=str, help=f"метод сортировки")
    gr.add_argument("-m", type=str, help=f"метод сортировки")
    p.add_argument("--order", type=str, choices=sorted(['asc','desc']), help=f"порядок сортировки")
    gr = p.add_mutually_exclusive_group(required=False)
    gr.add_argument("--input", type=str, help=f"файл с исходным массивом")
    gr.add_argument("-i", type=str, help=f"файл с исходным массивом")
    gr = p.add_mutually_exclusive_group(required=False)
    gr.add_argument("--output", type=str, help=f"файл для отсортированного массива")
    gr.add_argument("-o", type=str, help=f"файл для отсортированного массива")
    
    p = commands.add_parser("search", allow_abbrev=False, help="Поиск числа в массиве")
    gr = p.add_mutually_exclusive_group(required=True) #
    gr.add_argument("--value", type=int, help=f"искомое значение")
    gr.add_argument("-v", type=int, help=f"искомое значение")
    gr = p.add_mutually_exclusive_group(required=False) #
    gr.add_argument("--input", type=str, help=f"файл с массивом по возрастанию")
    gr.add_argument("-i", type=str, help=f"файл с массивом по возрастанию")


    p = commands.add_parser("select", allow_abbrev=False, help="номер статистики")
    gr = p.add_mutually_exclusive_group(required=True)
    gr.add_argument("-k", type=int, help=f"индекс статистики")
    gr.add_argument("--rank", type=int, help=f"индекс статистики")
    p.add_argument("--seed", type=int, help=f"начальное значение генератора")
    gr = p.add_mutually_exclusive_group(required=True) #обязательный
    gr.add_argument("--input", type=str, help=f"файл с исходным массивом")
    gr.add_argument("-i", type=str, help=f"файл с исходным массивом")
    gr = p.add_mutually_exclusive_group(required=False)
    gr.add_argument("--output", type=str, help=f"файл для отсортированного массива")
    gr.add_argument("-o", type=str, help=f"файл для отсортированного массива")


    p = commands.add_parser("shuffle", allow_abbrev=False, help="взболтать массив")
    p.add_argument("--seed", type=int, help=f"начальное значение генератора")
    gr = p.add_mutually_exclusive_group(required=True) #обязательный
    gr.add_argument("--input", type=str, help=f"файл с исходным массивом")
    gr.add_argument("-i", type=str, help=f"файл с исходным массивом")
    gr = p.add_mutually_exclusive_group(required=False)
    gr.add_argument("--output", type=str, help=f"файл для отсортированного массива")
    gr.add_argument("-o", type=str, help=f"файл для отсортированного массива")
    return parser










