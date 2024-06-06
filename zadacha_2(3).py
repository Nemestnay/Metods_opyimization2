import xlsxwriter

workbook = xlsxwriter.Workbook('КР2_3.xlsx')
worksheet = workbook.add_worksheet()
worksheet.write(0, 1, 'Метод Ньютона-Рафсона')
worksheet.write(1, 0, 'n')
worksheet.write(1, 1, 'x(n)')
worksheet.write(1, 2, "f'(x(n))")
worksheet.write(1, 3, "f''(x(n))")
worksheet.write(1, 4, "alfa(n)")

def func(x):
    return x ** 4 + 2 * (x ** 3) - 7 * (x ** 2) + 12 * x + 72

def proizvodnay1(x):
    return 4*(x**3) + 6*(x**2) - 14*x + 12


def proizvodnay2(x):
    return 12*(x**2) + 12*x - 14


def proizvodnay3(x):
    return 24*x + 12

def alfa(x, p):
    e = 1/2
    al=1
    while func(x+ al *p) > func (x) + e * al *proizvodnay1(x) * p:
        al = al/2
    return al


a = -10
b = 10
eps = 10 ** -6


def newton_rafson(eps):
    x = a
    i = 1
    while abs(proizvodnay1(x)) > eps:
        p = - proizvodnay1(x) / proizvodnay2(x)
        al = alfa(x, p)
        worksheet.write(i+1, 0, i)
        worksheet.write(i+1, 1, "{:.7f}".format(x))
        worksheet.write(i+1, 2, "{:.7f}".format(proizvodnay1(x)))
        worksheet.write(i+1, 3, "{:.7f}".format(proizvodnay2(x)))
        worksheet.write(i+1, 4, "{:.8f}".format(al))
        x += al * p
        i += 1


newton_rafson(eps)
workbook.close()
