from sympy import *
init_printing()

def increasing_decreasing_function(y, x, y1, x1): 
    result = [y1, x1] 
    result[1:1] = solve (diff(y), x) 
    result
    res_increase = []
    res_decrease = []
    for i in range(1, len(result)):
        if is_increasing(y, Interval.open(result[i-1], result[i])):
            res_increase.append(f'{result[i-1]}, {result[i]}')
        else:
            res_decrease.append(f'{result[i-1]}, {result[i]}')
    return print(f'Ф-я убывает {res_decrease}'), print(f'Ф-я возрастает {res_increase}')

def extremum_of_the_function(z, x):
    result_funk = solve (diff(z), x)
    for i in result_funk:
        num = z.subs(x, i)  
        if num > 0:
            return print(f'{num} точка минимум от {i}')
        elif num < 0:
            return print(f'{num} точка максимум от {i}')
        else:
            return print(f'{num} находится на оси х')