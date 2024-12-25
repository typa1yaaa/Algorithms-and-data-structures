import time
import random
import pandas as pd
import matplotlib.pyplot as plt
from main import AVLTree  

def data_generation_avl():
    # данные отсортированы
    easy_arrs = [
        list(range(1, 11)),
        list(range(1, 101)),
        list(range(1, 1001)),
        list(range(1, 10001)),
        list(range(1, 100001))
    ]
    # данные случайные
    normal_arrs = [
        [random.randint(0, 10000) for _ in range(10)],
        [random.randint(0, 10000) for _ in range(100)],
        [random.randint(0, 10000) for _ in range(1000)],
        [random.randint(0, 10000) for _ in range(10000)],
        [random.randint(0, 10000) for _ in range(100000)]
    ]
    # данные отсортированы в обратном порядке
    hard_arrs = [
        list(range(10, 0, -1)),
        list(range(100, 0, -1)),
        list(range(1000, 0, -1)),
        list(range(10000, 0, -1)),
        list(range(100000, 0, -1))
    ]

    easy_insert_times, normal_insert_times, hard_insert_times = [], [], []
    easy_remove_times, normal_remove_times, hard_remove_times = [], [], []

    # измерение времени для вставки и удаления элементов (простой случай)
    for arr in easy_arrs:
        avl_tree = AVLTree()
        
        # вставка
        start_time = time.time()
        for value in arr:
            avl_tree.insert(value)
        easy_insert_times.append(time.time() - start_time)
        
        # удаление
        start_time = time.time()
        for value in arr:
            avl_tree.remove(value)
        easy_remove_times.append(time.time() - start_time)

    # измерение времени для вставки и удаления элементов (средний случай)
    for arr in normal_arrs:
        avl_tree = AVLTree()
        
        # вставка
        start_time = time.time()
        for value in arr:
            avl_tree.insert(value)
        normal_insert_times.append(time.time() - start_time)
        
        # удаление
        start_time = time.time()
        for value in arr:
            avl_tree.remove(value)
        normal_remove_times.append(time.time() - start_time)

    # измерение времени для вставки и удаления элементов (сложный случай)
    for arr in hard_arrs:
        avl_tree = AVLTree()
        
        # вставка
        start_time = time.time()
        for value in arr:
            avl_tree.insert(value)
        hard_insert_times.append(time.time() - start_time)

        # удаление
        start_time = time.time()
        for value in arr:
            avl_tree.remove(value)
        hard_remove_times.append(time.time() - start_time)

    sizes = [10, 100, 1000, 10000, 100000]
    data = {
        'size': sizes * 6,
        'case': ['Легкий случай (вставка)'] * 5 + ['Средний случай (вставка)'] * 5 + ['Сложный случай (вставка)'] * 5 +
                ['Легкий случай (удаление)'] * 5 + ['Средний случай (удаление)'] * 5 + ['Сложный случай (удаление)'] * 5,
        'time': easy_insert_times + normal_insert_times + hard_insert_times +
                easy_remove_times + normal_remove_times + hard_remove_times
    }

    df = pd.DataFrame(data)

    # построение графика для вставки
    plt.figure(figsize=(10, 6))
    insert_df = df[df['case'].str.contains("вставка")]
    for case_label in insert_df['case'].unique():
        subset = insert_df[insert_df['case'] == case_label]
        plt.plot(subset['size'], subset['time'], marker='o', label=case_label)
    
    plt.xlabel('Размер данных')
    plt.ylabel('Время выполнения (сек)')
    plt.title('Время выполнения операции вставки в АВЛ-дереве')
    plt.xscale('log')
    plt.xticks(sizes, sizes)
    plt.legend()
    plt.tight_layout()
    plt.show()

    # построение графика для удаления
    plt.figure(figsize=(10, 6))
    remove_df = df[df['case'].str.contains("удаление")]
    for case_label in remove_df['case'].unique():
        subset = remove_df[remove_df['case'] == case_label]
        plt.plot(subset['size'], subset['time'], marker='o', label=case_label)
    
    plt.xlabel('Размер данных')
    plt.ylabel('Время выполнения (сек)')
    plt.title('Время выполнения операции удаления в АВЛ-дереве')
    plt.xscale('log')
    plt.xticks(sizes, sizes)
    plt.legend()
    plt.tight_layout()
    plt.show()

data_generation_avl()
