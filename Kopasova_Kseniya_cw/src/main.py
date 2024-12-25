from bin_heap import BinaryHeap
import matplotlib.pyplot as plt
import networkx as nx

class Graph:
    def __init__(self):
        self.edges = {}  # {вершина: [(сосед, вес), ...]} - формат графа
        self.graph_nx = nx.Graph()  # для визуализации
        self.pos = None # позиция узла

    def add_edge(self, start, end, weight):
        """Добавление ребра в граф"""
        # убираем лишние пробелы
        start, end = start.strip(), end.strip()
        # если вершина страт/енд еще не была добавлена, то добавляем 
        if start not in self.edges:
            self.edges[start] = []
        if end not in self.edges:
            self.edges[end] = []
        # добавляем для обеих вершин сосдей и вес ребра между ними 
        self.edges[start].append((end, weight))
        self.edges[end].append((start, weight))
        # добавляем вершины и ребро для отрисовки
        self.graph_nx.add_edge(start, end, weight=weight)
        # пересчитываем координаты у узлов для правильной визуализации
        self.pos = nx.spring_layout(self.graph_nx)
    
    # можем удалять ребра и вершины и программа на это реагирует
    # удаление и новый путь (динамический граф)

    # удаление вершины 
    def remove_vertex(self, start):
        """Удаление вершины"""
        if start in self.edges:
            # удалям у всех вершин удаленную вершину
            for neighbor, _ in self.edges[start]:
                self.edges[neighbor] = [(v, w) for v, w in self.edges[neighbor] if v != start]
            # удаляем саму вершинку
            self.edges.pop(start)
        # удаляем вершину из визуала
        self.graph_nx.remove_node(start)
        
    def draw_graph(self, path=None, highlight_edges=None, distances=None, title="Граф"):
        """Визуализация графа"""
        # очищаем прошлую визуализацию
        plt.clf()
        # меняем заголовок визуализации
        plt.title(title)

        # используем кругового размещения для отображения вершин
        self.pos = nx.circular_layout(self.graph_nx)
        # отображаем вершины и ребра
        nx.draw(self.graph_nx, self.pos, with_labels=True, node_color="lightblue", node_size=500, font_size=10, font_weight="bold")
        # отображаем метки весов на ребрах графа
        nx.draw_networkx_edge_labels(self.graph_nx, self.pos, edge_labels={(u, v): d['weight'] for u, v, d in self.graph_nx.edges(data=True)})

        # смещение координат для отображения меток выше вершин
        offset_pos = {node: (x, y + 0.15) for node, (x, y) in self.pos.items()}
        # рисуем значения над вершинами (расстояния)
        if distances:
            nx.draw_networkx_labels(self.graph_nx, offset_pos, labels=distances, font_size=12, font_color="red", font_weight="bold")

        # рисуем короткий путь зеленым
        if path:
            # преобразуем список узлов кратчайшего пути из [a, b, c] в [(a, b), (b, c)]
            path_edges = list(zip(path[:-1], path[1:]))
            nx.draw_networkx_edges(self.graph_nx, self.pos, edgelist=path_edges, edge_color="green", width=2)

        # рисуем проходку по путям красным если они заданы
        if highlight_edges:
            nx.draw_networkx_edges(
                self.graph_nx,
                self.pos,
                edgelist=highlight_edges,
                edge_color="red",
                width=2.5,
                label="Обрабатываемое ребро",
            )

        # масштабирование для корректного вывода изображения
        plt.axis("equal")
        # пауза для того, чтобы успеть разглядеть график
        plt.pause(1.3)

    def algorithm_Dijkstra(self, start, end):
        """Поиск кратчайшего пути от вершины start до вершины end с использованием двоичной кучи"""
        
        # если стартовой/конечной вершины нет в графе, выводим исключение
        if start not in self.edges or end not in self.edges:
            raise ValueError(f"Одна или обе вершины ({start}, {end}) отсутствуют в графе")

        # словарь, где ключ = вершине, а значение - расстояние от стартовой вершины
        # всем вершишнам присваивается inf(бесконечность), а стартовой вершине - 0
        distances = {vertex: float('inf') for vertex in self.edges}
        distances[start] = 0
        previous = {vertex: None for vertex in self.edges}

        # инициализация двоичной кучи для поиска узла с минимальным расстоянием
        priority_heap = BinaryHeap()
        # первый элемент кучи - стартовая вершина
        priority_heap.push(0, start)

        # пока двоичная куча не пустая
        while not priority_heap.is_empty():
            # извлекаем вершину с минимальным весом
            current_distance, current_vertex = priority_heap.pop()

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
                    # обновляем значение расстояния до соседа на меньшее
                    distances[neighbor] = distance
                    # сохраняем текущую вершину для соседа
                    previous[neighbor] = current_vertex
                    # добвляем соседа в кучу с новым расстоянием и приоритетом
                    priority_heap.push(distance, neighbor)

                    # визуализируем выделение рёбер 
                    self.draw_graph(
                        highlight_edges=[(current_vertex, neighbor)],
                        title=f"Обработка ребра {current_vertex} -> {neighbor}",
                        distances=distances  # передаем словарь с расстояниями
                    )

        # восстановление пути от конечного значения до стартового
        path = []
        current = end
        while current is not None:
            # идем назад по цепочке предыдущих вершин
            path.append(current)
            current = previous[current]
        
        # если путь невозможен, возвращаем пустой список и бесконечную длину
        if distances[end] == float('inf'):
            self.draw_graph(path=[], title="Путь недостижим")
            return [], float('inf')

        path = path[::-1]  # переворачиваем путь
        path_edges = [(path[i], path[i+1]) for i in range(len(path)-1)]
        # визуализация красным цветом
        self.draw_graph(path=path, highlight_edges=path_edges, title="Кратчайший путь")
        # итоговая визуализация зеленым цветом
        self.draw_graph(path=path, title="Кратчайший путь")
        # возвращаем путь и минимальный путь
        return path, distances[end]

    def print_graph_state(self):
        """Вывод графа"""
        print("\nТекущие вершины графа:")
        for vertex, neighbors in self.edges.items():
            print(f"{vertex}: {neighbors}")

def main():
    """Функция для проверки работы программы с вводом вершин"""
    graph = Graph()

    print("Введите вершины и вес ребра в формате 'начало вес конец' (Enter для завершения):")
    while True:
        data = input().strip()
        if data == '':
            break
        try:
            start, weight, end = data.split()
            weight = int(weight)
            graph.add_edge(start, end, weight)
            
        except ValueError:
            print("Ошибка ввода! Формат: 'начало вес конец'")

    # вводим вершины графа
    while True:
        try:
            info = input("Введите начальную и конечную вершины для поиска кратчейшего пути в формате 'начало конец': ").strip()
            start, end = info.split()
            plt.ion()  # включаем интерактивный режим для matplotlib
            path, total_distance = graph.algorithm_Dijkstra(start, end)
            print("\nКратчайший путь:", " -> ".join(path))
            print("Общая длина пути:", total_distance)

            # поиск кратчайшего пути
            plt.ioff()  # выключаем интерактивный режим
            plt.show()  # оставляем финальный граф для просмотра

            break
        except ValueError:
            print("Ошибка ввода! Формат: 'начало конец'")
    
def check_finish_data():
    """Функция работы программы без ввода вершин"""
    g = Graph()
    g.add_edge('a', 'b', 1)
    g.add_edge('b', 'c', 3)
    g.add_edge('a', 'd', 5)
    g.add_edge('d', 'c', 1)
    g.add_edge('c', 'h', 15)
    g.add_edge('h', 'n', 30)
    g.add_edge('h', 'm', 29)
    g.add_edge('n', 'o', 1)
    g.add_edge('m', 'o', 5)

    start = 'a'
    end = 'o'
    print("Изначальные вершины графа")
    g.print_graph_state()

    plt.ion()  
    path, total_distance = g.algorithm_Dijkstra(start, end)
    print("\n1. Кратчайший путь:", " -> ".join(path))
    print("1. Общая длина пути:", total_distance)
    g.draw_graph()

    # удаляем вершину
    rem_ver = 'd'

    g.remove_vertex(rem_ver)
    g.print_graph_state()

    path, total_distance = g.algorithm_Dijkstra(start, end)
    if len(path) == 0:
        print("Путь недостижим :(")
    else:
        print("\n2. Кратчайший путь:", " -> ".join(path))
        
    print("2. Общая длина пути:", total_distance)

    # удаляем вершину
    rem_ver = 'c'

    g.remove_vertex(rem_ver)
    g.print_graph_state()

    path, total_distance = g.algorithm_Dijkstra(start, end)
    if len(path) == 0:
        print("3. Путь недостижим :(")
    else:
        print("\n3. Кратчайший путь:", " -> ".join(path))

    print("3. Общая длина пути:", total_distance)

    plt.ioff()  
    plt.show()  
    pass

check_finish_data()
# main()