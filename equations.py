"""
===============================================================
This is a python script containing various utilities for school
Made by Elijah Lopez
===============================================================
"""
import math
import molar_mass
import tvm
import sys


def quadratics():
    a = b = d = -1
    while d < 0:
        try:
            a, b, c = (float(x) for x in input('Enter values a b c : ').split())
            d = (b * b - 4 * a * c)
            if d < 0: print('Those roots are Invalid, please try again')
        except ValueError:
            print('Invalid input, please try again')
    bot, top_1, top_2 = 2 * a, math.sqrt(d) - b, -b - math.sqrt(d)
    top_1, top_2 = top_1 / bot, top_2 / bot
    if top_1 > 0: msg_1 = f'(x - {top_1})'
    elif top_1 < 0: msg_1 = f'(x + {-1 * top_1})'
    else: msg_1 = 'x'
    if top_2 > 0: msg_2 = f'(x - {top_2})'
    elif top_2 < 0: msg_2 = f'(x + {-1 * top_2})'
    else: msg_2 = 'x'
    if msg_1 == msg_2: msg_1, msg_2 = msg_1 + '^2', ''
    print(f'y = {msg_1}{msg_2}')
    print(f'x = {top_1} or {top_2}')


def roots(a, b, c):
    d = (b * b - 4 * a * c)
    bot, top_1, top_2 = 2 * a, math.sqrt(d) - b, -b - math.sqrt(d)
    top_1, top_2 = top_1 / bot, top_2 / bot
    return top_1, top_2


def kinematics():
    SIG_FIGS = 3
    print(f"""
    VARIABLES
    u: initial velocity (metres/second)
    v: final velocity (metres/second)
    a: acceleration (metres/second^2)
    s: distance (metres)
    t: time (seconds)

    Answers are rounded to {SIG_FIGS} significant figured. Override in code.
    """)
    print('Units are metres and seconds and rounds to 3 sig figs')
    unknown = input('Enter the variable to be calculated: ')
    print('What variables are known? e.g: u v a')
    known_variables = input('    ').split()
    variables = ['u', 'v', 'a', 's', 't']
    variables.remove(unknown)
    variable_list = {'u': None, 'v': None, 'a': None, 's': None, 't': None}
    units = {'u': 'm/s', 'v': 'm/s', 'a': 'm/s^2', 's': 'm', 't': 's'}
    for variable in known_variables:
        user_input = input(f'Enter {variable}: ')
        variable_list[variable] = float(user_input)
        variables.remove(variable)
    u, v, a, s, t = tuple(variable_list.values())
    unneeded = variables.pop()
    if unneeded == 'u':
        if unknown == 'v': answer = s / t + a / 2 * t
        elif unknown == 'a': answer = (s - v * t) * -2 / t ** 2
        elif unknown == 's': answer = v * t - a / 2 * t ** 2
        else: answer = max(roots(-a / 2, v, -s))
    elif unneeded == 'v':
        if unknown == 'u': answer = s / t - a / 2 * t
        elif unknown == 'a': answer = (s - u * t) * 2 / t ** 2
        elif unknown == 's': answer = u * t + 0.5 * a * t ** 2
        else: answer = max(roots(a / 2, a, -s))
    elif unneeded == 'a':
        if unknown == 'u': answer = 2 * s / t - v
        elif unknown == 'v': answer = 2 * s / t - u
        elif unknown == 's': answer = (v + u) / 2 * t
        else: answer = 2 * s / (v + u)
    elif unneeded == 's':
        if unknown == 'u': answer = v - a * t
        elif unknown == 'v': answer = u + a * t
        elif unknown == 'a': answer = (v - u) / t
        else: answer = (v - u) / a
    else:  # uneeded == 't'
        if unknown == 'u': answer = math.sqrt(v ** 2 - 2 * a * s)
        elif unknown == 'v': answer = math.sqrt(u ** 2 + 2 * a * s)
        elif unknown == 'a': answer = (v ** 2 - u ** 2) / 2 / s
        else: answer = (v ** 2 - u ** 2) / 2 / a
    unit = units[unknown]
    print(unknown, ' = ', round(answer, SIG_FIGS-len(str(int(answer)))), unit, sep='')


def midpoint():
    print('Enter x1 y1')
    x1, y1 = (int(x) for x in input().split())
    print('Enter x2 y2')
    x2, y2 = (int(x) for x in input().split())
    x = x1 + x2
    y = y1 + y2
    print('mp = (', x / 2, ', ', y / 2, ')', sep='')


def two_points():
    print('Enter x1 y1')
    x, y = (int(x) for x in input().split())
    print('Enter x2 y2')
    x2, y2 = (int(x) for x in input().split())
    x, y = x - x2, y - y2
    print(math.sqrt(x ** 2 + y ** 2))


def linear():
    print('Enter x1 y1 total_1')
    x, y, c = (float(x) for x in input().split())
    print('Enter x2 y2 total_2')
    x2, y2, c2 = (float(x) for x in input().split())
    x1 = c / x
    y2 = -y / x * x2 + y2
    x2 = x2 * x1
    y2 = (c2 - x2) / y2
    y = y * y2
    x = (c - y) / x
    print('(', x, ', ', y2, ')', sep='')


def pendulum():
    print('DISCLAIMER: This is in beta, answers may not be True')
    length = float(input('Enter length: '))
    a = float(input('Enter initial angle: '))
    t = int(input('Enter time in seconds: '))
    x = t
    t = 1
    for i in range(0, x):
        r = length * (math.cos(a * (math.cos(t * math.sqrt(9.8 / length)))))
        b = length * (math.cos(a))
        print(t, r - b)
        t += 1


def circle():
    r = int(input('Enter radius: '))
    pi = math.pi
    area = pi * r * r
    circumference = 2 * pi * r
    print(f'Area: {area}\nCircumference: {circumference}')


def pascals_triangle():
    rows = int(input('How many rows: ')) + 1
    row_list = [[1], [1, 1]]
    temp_row, print_row = [1, 1], []
    centre_to = '  '
    for i in range(0, rows - 2):
        print_row.append(1)
        for j in range(len(temp_row) - 1): print_row.append(temp_row[j] + temp_row[j + 1])
        print_row.append(1)
        row_list.append(print_row.copy())
        temp_row, print_row = print_row.copy(), []
        if i == rows - 3:
            for row in temp_row: centre_to += str(row)
    for row in row_list:
        row_to_print = ''
        for number in row: row_to_print += ' ' + str(number)
        print(row_to_print.center(len(centre_to * 2)))


def factors(cont=True, n=None):
    if n is None: n = int(input('Enter number: '))
    x = 1
    length = []
    for i in range(0, n):
        y = n / x
        if x > int(y): break
        if y == int(y):
            y = int(y)
            if cont: print(x, 'x', y, '=', n)
            else:
                length.append(x)
                length.append(y)
        x += 1
    return length


def lcm():
    n = int(input('Enter number: '))
    x = 2
    values = {}
    for i in range(0, n):
        y = n / x
        if y == int(y):
            n = n / x
            if x in values: values[x] += 1
            else: values[x] = 1
        else: x = x + 1
    nox = True
    for x in values:
        if nox:
            if values[x] > 1:
                msg = f'{x}^{values[x]}'
            else:
                msg = x
            print(msg, end=' ')
            nox = False
        else:
            if values[x] > 1: msg = f'x {x}^{values[x]}'
            else: msg = f'x {x}'
            print(msg, end=' ')


def gcf():
    n, n2 = [int(x) for x in input('Enter n1 n2: ').split()]
    if n == n2: print(n)
    else:
        facts = factors(cont=False, n=n)
        facts2 = factors(cont=False, n=n2)
        cross = [x for x in facts if x in facts2]
        print(max(cross))


greeting = """1 for quadratics ax^2+bx+c
2 for kinematics (beta)
3 for midpoint
4 for distance between two points
5 for linear systems x + y = c
6 for pendulum (beta)
7 for circle stuff (in development)
8 for factors of a number
9 for LCM of a number
10 for GCF
11 for pascals triangle triangle
12 for molar mass calculation
13 for Time Value of Money menu
14 to exit"""

print('School utilities by Elijah Lopez')
print(greeting)
funcs = [quadratics, kinematics, midpoint, two_points, linear, pendulum, circle,
         factors, lcm, gcf, pascals_triangle, molar_mass.molar_mass, tvm.main, sys.exit]
while True:
    try:
        choice = int(input())
        if choice == '13':
            tvm.main()
            print(greeting)
        elif len(funcs) + 1 > choice > 0:
            funcs[choice - 1]()
            while True:
                f = input('Would you like to try another? (y/n): ').lower()
                if f == 'y': funcs[choice - 1]()
                else: break
            print('\nYou are at the main menu')
            print(greeting)
        else: print('ERROR: PICK A VALID OPTION')
    except ValueError:
        print('ERROR: INVALID INPUT')
        print('\nYou are at the main menu')
        print(greeting)
