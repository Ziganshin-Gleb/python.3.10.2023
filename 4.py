a = int(input('Входные данные a: '))
b = int(input('Входные данные b: '))
def f(a, b):
    c = 3 * (a + b) ** 3 + 275 * b ** 2 - 127 * a - 41
    print(c)
f(a, b)