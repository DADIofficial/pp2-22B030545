import random
import numpy as np


def generate_points(x0, y0, b):
    # Создаем пустой массив точек с переменной "busy" равной 0
    points = np.zeros((x0, y0), dtype=[('busy', np.int8)])

    # Генерируем шум Перлина
    for i in range(x0):
        for j in range(y0):
            noise_val = perlin_noise(i / 10, j / 10)
            if noise_val > 0.5:
                points[i, j]['busy'] = 1
    # Выбираем b точек с busy = 1
    busy_points = np.argwhere(points['busy'] == 1)
    if b > len(busy_points):
        b = random.randint(0, len(busy_points))
    selected_points = random.sample(busy_points.tolist(), b)

    # Возвращаем список координат точек с busy = 1
    return selected_points


def perlin_noise(x, y):
    # Инициализируем переменные
    xi = int(x)
    yi = int(y)
    xf = x - int(x)
    yf = y - int(y)
    u = fade(xf)
    v = fade(yf)

    # Извлекаем значения градиентов для каждой из 4 угловых точек квадрата
    a = p[xi] + yi
    aa = p[a]
    ab = p[a+1]
    b = p[xi+1] + yi
    ba = p[b]
    bb = p[b+1]

    # Вычисляем взвешенные средние для каждой точки квадрата
    res = lerp(v, lerp(u, grad(aa, xf, yf), grad(ba, xf-1, yf)),
               lerp(u, grad(ab, xf, yf-1), grad(bb, xf-1, yf-1)))
    return (res + 1) / 2


def fade(t):
    return 6 * t**5 - 15 * t**4 + 10 * t**3


def lerp(t, a, b):
    return a + t * (b - a)


def grad(hash, x, y):
    h = hash & 3
    if h == 0:
        return x + y
    elif h == 1:
        return -x + y
    elif h == 2:
        return x - y
    else:
        return -x - y


# Инициализация пермутационного массива
p = list(range(256))
random.shuffle(p)
p += p