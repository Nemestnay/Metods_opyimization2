import xlsxwriter
workbook = xlsxwriter.Workbook('КР2_2.xlsx')
worksheet = workbook.add_worksheet()
worksheet.write(0, 1, 'Исключаемая пара (x, p)')
worksheet.write(0, 4, 'Включаемая пара (x, p)')
worksheet.write(1, 0, 'n')
worksheet.write(1, 1, 'x*(n)')
worksheet.write(1, 2, 'p*(n)')
worksheet.write(1, 3, '2L*delta(n)')
worksheet.write(1, 4, "x'(n)")
worksheet.write(1, 5, "x''(n)")
worksheet.write(1, 6, "p(n)")

def func(x):
    return abs(-5 - x) * abs(x - 1) * (3 * abs(x / 4 + 5) + 1) / 36

a = -20
b = 10
L = 18.5
eps = 10 ** (-6)



def metod_lomanix():
    x = (func(a) - func(b) + L * (a + b)) / (2 * L)
    p = (func(a) + func(b) + L * (a - b)) / 2
    i = 2
    f = func(x)
    delta = abs(f - p) / (2 * L)
    tochki = [(x, p)]
    while 2 * L * abs(delta) > eps:
        x1 = x - delta
        x2 = x + delta

        worksheet.write(i, 0, i - 1)
        worksheet.write(i, 1, "{:.8f}".format(x))
        worksheet.write(i, 2, "{:.8f}".format(p))

        tochki.remove((x, p))
        p = (f + p) / 2
        tochki.append((x1, p))
        tochki.append((x2, p))

        worksheet.write(i, 4, "{:.8f}".format(x1))
        worksheet.write(i, 5, "{:.8f}".format(x2))
        worksheet.write(i, 6, "{:.8f}".format(p))

        f1 = func(x1)
        f2 = func(x2)
        if f1 < f2:
            x = x1
            f = f1
        else:
            x = x2
            f = f2
        delta = abs(f - p) / (2 * L)
        worksheet.write(i, 3, "{:.8f}".format(2 * L * delta))
        i += 1


metod_lomanix()
workbook.close()
