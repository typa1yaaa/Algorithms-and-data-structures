import time
import random
import string
import matplotlib.pyplot as plt
from main1 import get_sub_string_RK

def generate_random_string(length):
    return ''.join(random.choices(string.ascii_lowercase, k=length))

def data_generation_test():
    n = [10, 100, 1000, 10000, 100000] 
    pattern_length = random.randint(1, 10)  
    all_time = []

    for size in n:
        text = generate_random_string(size)
        pattern = generate_random_string(pattern_length)
        
        start = time.time()
        result = get_sub_string_RK(pattern, text)
        end = time.time()
        
        all_time.append(end - start)

    plt.figure(figsize=(12, 8))
    plt.plot(n, all_time, linestyle='-', color='black', marker='o')
    plt.title("Зависимость времени работы от размера данных (алгоритм Рабина-Карпа)")
    plt.xlabel('Длина строки')
    plt.ylabel('Затраченное время')
    plt.grid(True)
    plt.show()

data_generation_test()
