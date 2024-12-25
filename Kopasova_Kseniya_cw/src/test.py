import time
import random
import matplotlib.pyplot as plt
from collections import deque
from bin_heap import BinaryHeap

# определяю написанный класс Graph, но без визуализации для быстрого выполнения тестов
class Graph:
    def __init__(self):
        self.edges = {}  

    def add_edge(self, start, end, weight):
        """Добавляет ребро в граф."""
        start, end = start.strip(), end.strip() 
        if start not in self.edges:
            self.edges[start] = []
        if end not in self.edges:
            self.edges[end] = []
        self.edges[start].append((end, weight))
        self.edges[end].append((start, weight))

    def algorithm_Dijkstra(self, start, end):
        """Поиск кратчайшего пути от вершины start до вершины end с использованием бинарной кучи"""
        if start not in self.edges or end not in self.edges:
            raise ValueError(f"Одна или обе вершины ({start}, {end}) отсутствуют в графе")

        # расстояния от начальной вершины до всех других
        distances = {vertex: float('inf') for vertex in self.edges}
        distances[start] = 0

        # предыдущие вершины для восстановления пути
        previous = {vertex: None for vertex in self.edges}

        # инициализация бинарной кучи
        priority_queue = BinaryHeap()
        priority_queue.push(0, start)

        while not priority_queue.is_empty():
            # извлекаем вершину с минимальным накопленным весом
            current_distance, current_vertex = priority_queue.pop()

            # если извлечённое расстояние больше, чем текущее, пропускаем (устаревший элемент)
            if current_distance > distances[current_vertex]:
                continue

            # если достигли конечной вершины, завершаем
            if current_vertex == end:
                break

            # обрабатываем всех соседей
            for neighbor, weight in self.edges[current_vertex]:
                distance = current_distance + weight

                # если нашли более короткий путь к соседу
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    previous[neighbor] = current_vertex
                    priority_queue.push(distance, neighbor)

        # восстановление пути
        path = []
        current = end
        while current is not None:
            path.append(current)
            current = previous[current]
        
        # если путь невозможен, возвращаем пустой список и бесконечную длину
        if distances[end] == float('inf'):
            return [], float('inf')

        # визуализация пути
        path = path[::-1]  # переворачиваем путь
        # возвращаем путь 
        return path, distances[end]

def find_furthest_vertices(graph, start_vertex):
    """Находит вершину, наиболее удалённую от start_vertex, с помощью BFS"""
    # проверяем, есть ли начальная вершина в графе
    if start_vertex not in graph.edges:
        raise ValueError(f"Вершина {start_vertex} отсутствует в графе.")
    
    # используем очередь для BFS
    queue = deque([(start_vertex, 0)])  # храним вершину и расстояние до неё
    visited = set()  # множество посещённых вершин
    furthest_vertex = start_vertex
    max_distance = 0

    while queue:
        current, distance = queue.popleft()

        # если вершина уже посещена, пропускаем её
        if current in visited:
            continue

        # отмечаем вершину как посещённую
        visited.add(current)

        # обновляем наиболее удалённую вершину
        if distance > max_distance:
            max_distance = distance
            furthest_vertex = current

        # добавляем соседей в очередь
        for neighbor, _ in graph.edges[current]:
            if neighbor not in visited:
                queue.append((neighbor, distance + 1))

    return furthest_vertex

def measure_performance(num_vertices, num_edges):
    graph = Graph()
    
    # генерация случайных рёбер
    vertices = [str(i) for i in range(num_vertices)]
    
    for _ in range(num_edges):
        u, v = random.sample(vertices, 2)
        weight = random.randint(1, 10)
        graph.add_edge(u, v, weight)
    
    # выбираем случайную начальную вершину
    start_vertex = random.choice(vertices)
    # находим самую удалённую вершину от начальной
    end_vertex = find_furthest_vertices(graph, start_vertex)
    
    print(f"Удалённые вершины: {start_vertex} -> {end_vertex}")
    
    # измерение времени выполнения алгоритма Дейкстры
    start_time = time.time()
    path, total_distance = graph.algorithm_Dijkstra(start_vertex, end_vertex)
    end_time = time.time()
    
    elapsed_time = end_time - start_time
    
    print(f"Время выполнения для {num_vertices} вершин и {num_edges} рёбер: {elapsed_time:.6f} секунд")
    print(f"Кратчайший путь: {' -> '.join(path)}")
    print(f"Общая длина пути: {total_distance}")
    return elapsed_time

# пример использования: измерение времени для графов разного размера
sizes = [(500, 500), (1000, 1000), (1500, 1500), (2000, 2000), (2500, 2500), (3000, 3000), (3500, 3500), (4000, 4000), ()]
times = []

for num_vertices, num_edges in sizes:
    elapsed_time = measure_performance(num_vertices, num_edges)
    times.append(elapsed_time)

# построение графика зависимости времени от числа рёбер
plt.plot([x[1] for x in sizes], times, marker='o')
plt.xlabel('Число рёбер')
plt.ylabel('Время выполнения (сек)')
plt.title('Зависимость времени выполнения от числа рёбер')
plt.grid(True)
plt.show()
