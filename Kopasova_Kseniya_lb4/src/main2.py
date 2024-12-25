"""Реализация и визуализация алгоритма Грэхема"""
import matplotlib.pyplot as plt
from math import atan2

def rotate(elem_a, elem_b, elem_c):
    """Функция вычисления ориентации трех точек"""
    return (elem_b[0] - elem_a[0]) * (elem_c[1] - elem_b[1]) - (elem_b[1] - elem_a[1]) * (elem_c[0] - elem_b[0])

def grahamscan(arr_points):
    """Алгоритм Грэхема"""
    n = len(arr_points)
    if n < 3:
        raise ValueError("Выпуклая оболочка невозможна, недостаточно точек")
    
    min_point = min(arr_points, key=lambda p: (p[1], p[0]))
    arr_points.remove(min_point)

    arr_points.sort(key=lambda p: (atan2(p[1] - min_point[1], p[0] - min_point[0]), (p[0] - min_point[0])**2 + (p[1] - min_point[1])**2))
    arr_points.insert(0, min_point)  

    stack = [arr_points[0], arr_points[1]]  # две стартовые точки
    for i in range(2, n):
        while len(stack) > 1 and rotate(stack[-2], stack[-1], arr_points[i]) <= 0:  # убираем правые повороты
            stack.pop()
        stack.append(arr_points[i])

    return stack

def square(arr):
    """Нахождение площади по координатам фигуры"""
    area = 0
    for i in range(len(arr)):
        x1, y1 = arr[i]
        x2, y2 = arr[(i + 1) % len(arr)]
        area += x1 * y2 - y1 * x2
    return abs(area) / 2


def visualization(arr_points_new, arr_points_old):
    """Визуализация минимальной выпуклой области, полученной с помощью алгоритма Грэхема"""
    arr_points_new.append(arr_points_new[0])  # Для замыкания оболочки

    x_points, y_points = zip(*arr_points_new)
    x_poi_old, y_poi_old = zip(*arr_points_old)
    plt.plot(x_points, y_points, marker='o', linestyle='-', color='black', label="Выпуклая оболочка")
    plt.scatter(*zip(*arr_points_old), color='red', label="Все точки")
    
    plt.title("Точки и выпуклая фигура")
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend()
    plt.grid(True)
    plt.show()

def main():
    """Головная функция"""
    # n = int(input())
    # arr_points = []
    arr_points = [[9, 58], [4, -49], [-23, -95], [-2, 43], [40, -34], [45, -58], [-69, 88], [41, -28], [7, 18], [-5, -74], [22, -29], [92, 41], [-13, 100], [-29, -32], [38, 67], [-31, -1], [-10, 50], [-51, 65], [19, 73], [3, 90], [-79, -49], [-25, 13], [63, -50], [-65, -79], [-46, -26], [-59, 91], [-71, 41], [-90, -97], [-94, 54], [31, -29], [93, -39], [51, -35], [7, 54], [31, -35], [-91, 81], [76, 69], [10, -96], [-50, 69], [-71, 68], [36, 82], [11, 30], [93, -93], [6, -40], [-44, 47], [-29, -19], [63, -65], [88, 59], [84, -24], [11, -78], [78, 36], [68, -70], [63, -61], [2, 98], [-58, 41], [-86, 67], [15, 93], [47, 67], [12, 37], [-27, -84], [66, -15], [12, -41], [-11, 27], [-98, 100], [19, -47], [38, -70], [-9, -51], [-92, -17], [35, -12], [67, -53], [-95, 95], [98, -51], [85, 22], [-90, 3], [81, -45], [-61, 66], [-95, -85], [-42, -77], [-49, -72], [-33, -3], [-80, -8], [79, -45], [-5, -15], [59, -48], [-84, 37], [1, 48], [45, -100], [13, -68], [23, 15], [-95, 95], [-93, -45], [31, 86], [68, -43], [49, -89], [14, 84], [-71, 20]]
    n = len(arr_points)
    # for _ in range(n):
    #     x, y = map(int, input().split(', '))
    #     arr_points.append([x, y])

    
    new_arr_points = grahamscan(arr_points.copy())

    print((new_arr_points, square(new_arr_points)))
    visualization(new_arr_points, arr_points)

main()