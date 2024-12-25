import time
import random
import pandas as pd
import matplotlib.pyplot as plt
from main2 import grahamscan

def data_generation_test():
    n = [10, 100, 1000, 10000, 20000]
    all_time = []
    for i in range(len(n)):
        start = time.time()
        arr_points = []
        for _ in range(n[i]):
            x = random.uniform(-100, 100)
            y = random.uniform(-100, 100)
            arr_points.append([x, y])
        
        true_posled = grahamscan(arr_points, n[i])
        new_arr_points = []
        for i in true_posled:
            new_arr_points.append(arr_points[i])
    
        # print((new_arr_points, square(new_arr_points)))
        # visualization(new_arr_points, arr_points)
    
        end = time.time()
        all_time.append(end-start)
    
    plt.figure(figsize=(10, 6))
    plt.plot(n, all_time, linestyle = '-', color = 'black',  marker='o')
    plt.title("Зависимость размера данных и времени работы (алгоритм Грэхема)")
    plt.xlabel('Количество данных')
    plt.ylabel('Затраченное время')
    plt.grid(True)
    plt.show()

data_generation_test()