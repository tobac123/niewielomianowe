'''
Tomasz G. 5o

tf
'''


import math
from sympy import symbols, Eq, solve


fodx = []
debugi = None

def TakeAquation():
    print('''
    Podaj osobno części nierówności wielomianowej;
    na początku podaj 'a' a na końcu znak nierówności - zachowaj kolejność zapisu.
    
    wpisz ';' i dostaniesz przykłąd.
    ''')
    while True:
        fxin = str(input("  : "))

        if ";" in fxin:
            print("  : -2 (x-4) (x-7)**2 (x+4) >= 0")
            fodx.extend(["-2", "(x-4)", "(x-7)**2", "(x+4)", ">= 0"])
            return fodx

        fodx.append(fxin)
        if ">" in fxin or "<" in fxin:
            return fodx

'''
-2 (x-4) (x-7)**2 (x+4) >= 0
'''


if __name__ == '__main__':
    TakeAquation()

    fx = {'a': fodx[0], 'f': fodx[-1], 'x': []}

    for i in range(1, len(fodx[1:-1])):
        fx['x'].append(fodx[i])

    if "x" in fx['a']:
        pass

    x = symbols('x')
    equation = Eq("2*x**2 * -2*x * 1", 0)
    solution = solve(equation, x)

    print(fx.items())
    print(solution)