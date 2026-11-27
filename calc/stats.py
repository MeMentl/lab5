import math

MAX_COUNT = 20
MAX_VALUE = 10_000

def stats_check(values):
    if len(values) == 0:
        raise ValueError("Пустая последовательность")
    if len(values) > MAX_COUNT:
        raise ValueError(f"Чесел больше чем {MAX_COUNT}")
    for value in values:
        if not math.isfinite(value):
            raise ValueError(f"{value} не является конечным числом")
        if abs(value) > MAX_VALUE:
            raise ValueError(f"{value} вне допустимого диапазона")

def count(values):
    return len(values)

def total(values):
    rez = 0
    for value in values:
        rez += value
    return rez

def mean(values):
    return total(values)/len(values)

def sq_sum(values):
    rez = 0
    for value in values:
        rez = rez + value ** 2
    return rez

def root_mean_sq(values):
    return math.sqrt(sq_sum(values) / len(values))

def sq_sum_dev(values):
    M = mean(values)
    rez = 0
    for value in values:
        rez = rez + (value - M)**2
    return rez

def st_dev(values):
    if len(values)<2:
        return None
    return math.sqrt(sq_sum_dev(values)/(len(values)-1))

def disp(values):
    return sq_sum_dev(values)/len(values)

def sko(values):
    return math.sqrt(disp(values))

def min_val(values):
    rez = values[0]
    for value in values:
        if rez > value:
            rez = value
    return rez

def max_val(values):
    rez = values[0]
    for value in values:
        if rez < value:
            rez = value
    return rez

def neg_count(values):
    rez = 0
    for value in values:
        if value < 0:
            rez += 1
    return rez

def pos_count(values):
    rez = 0
    for value in values:
        if value > 0:
            rez += 1
    return rez

REPORT = [
    ("Количество",    count,        "d"),
    ("Сумма",         total,        ".3f"),
    ("Ср. арифм.",    mean,         ".3f"),
    ("Сумма кв.",     sq_sum,       ".3f"),
    ("Ср. кв.",       root_mean_sq, ".3f"),
    ("Дисперсия",     disp,         ".3f"),
    ("СКО",           sko,          ".3f"),
    ("Станд. откл.",  st_dev,       ".3f"),
    ("Наименьшее",    min_val,      ".3f"),
    ("Наибольшее",    max_val,      ".3f"),
    ("Положительных", pos_count,    "d"),
    ("Отрицательных", neg_count,    "d")
]
