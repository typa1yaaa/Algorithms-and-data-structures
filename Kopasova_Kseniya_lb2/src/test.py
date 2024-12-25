from main import timsort
import time
import random
import pandas as pd
import matplotlib.pyplot as plt

def data_generation():
    easy_arrs = []
    normal_arrs = []
    hard_arrs = []

    # данные уже отсортированы
    easy_arr_10 =  list(range(10, 1, -1))
    easy_arr_1000 = list(range(1000, 1, -1))
    easy_arr_100000 = list(range(100000, 1, -1))
    easy_arrs = [easy_arr_10, easy_arr_1000, easy_arr_100000]
    # данные случайные
    normal_arr_10 = [random.randint(0, 10000) for _ in range(10)]
    normal_arr_1000 = [random.randint(0, 10000) for _ in range(1000)]
    normal_arr_100000 = [random.randint(0, 10000) for _ in range(100000)]
    normal_arrs = [normal_arr_10, normal_arr_1000, normal_arr_100000]
    # данные расположены в обратном порядке
    hard_arr_10 =  list(range(0, 10))
    hard_arr_1000 =  list(range(0, 1000))
    hard_arr_100000 =  list(range(0, 100000))
    hard_arrs = [hard_arr_10, hard_arr_1000, hard_arr_100000]
    print(easy_arr_10)
    easy_time = []
    normal_time = []
    hard_time = []
    # print(easy_arrs)
    #проверка "простого" случая
    for value in easy_arrs:
        start_time = time.time()
        data = timsort(value)
        end_time = time.time()
        easy_time.append(end_time - start_time)

    #проверка "среднего" случая
    for value in normal_arrs:
        start_time = time.time()
        data = timsort(value)
        end_time = time.time()
        normal_time.append(end_time - start_time)

    #проверка "сложного" случая
    for value in hard_arrs:
        start_time = time.time()
        data = timsort(value)
        end_time = time.time()
        hard_time.append(end_time - start_time)

    print(easy_time, normal_time, hard_time)


    # Вывод времени выполнения (опционально)
    print("Время выполнения (сек):")
    print("Легкий случай:", easy_time)
    print("Средний случай:", hard_time)
    print("Сложный случай:", normal_time)

    # Определение размеров данных
    sizes = [10, 1000, 100000]

    # Создание DataFrame для удобства обработки
    data = {
        'size': sizes * 3,
        'case': ['Легкий случай'] * 3 + ['Средний случай'] * 3 + ['Сложный случай'] * 3,
        'time': easy_time + hard_time + normal_time
    }

    df = pd.DataFrame(data)

    # Построение графика времени выполнения
    plt.figure(figsize=(10, 6))
    for case_label in ['Легкий случай', 'Средний случай', 'Сложный случай']:
        subset = df[df['case'] == case_label]
        plt.plot(subset['size'], subset['time'], marker='o', label=case_label)
    
    plt.xlabel('Размер данных')
    plt.ylabel('Время выполнения (сек)')
    plt.title('Время выполнения TimSort для разных типов случаев')
    plt.xscale('log')  # Логарифмическая шкала для оси X
    plt.xticks(sizes, sizes)  # Установка меток по оси X
    plt.legend()
    plt.tight_layout()
    plt.savefig('time_comparison.png')  # Сохранение графика в файл
    plt.show()

data_generation()
