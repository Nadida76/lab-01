import math

# print('Equaçao do 2o grau da forma: ax² + bx + c')


try:
    a = int(input('Введите коэффициент a: '))

    if a == 0:
        print(
        'Если a=0, квадратное уравнение не может быть вычислено!')  # Se a=0, equação quadratica não pode ser calculado!
    else:
        b = int(input('Введите коэффициент b: '))
        c = int(input('Введите коэффициент c: '))
        delta = b * b - (4 * a * c)

        if delta < 0:
            print('Дельта меньше 0. Воображаемые корни.')  # Delta é menor que 0. Raízes imaginárias
        elif delta == 0:
            raiz = -b / (2 * a)
            print('Если Дельта = 0, то корень = ', raiz)  # Se for Delta = 0
        else:
            raiz1 = (-b + math.sqrt(delta)) / (2 * a)
            raiz2 = (-b - math.sqrt(delta)) / (2 * a)
            print('Корень: \n Корень-1 =', raiz1, ' \n Корень-2 =', raiz2)
except Exception as e:
    print("Exception (коэффициент a):", e)
    pass
