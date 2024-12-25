class BinaryHeap:
    def __init__(self):
        self.heap = []

    def push(self, priority, item):
        """Добавлениe элемента с приоритетом в кучу"""
        self.heap.append((priority, item))
        self.move_up(len(self.heap) - 1)

    def pop(self):
        """Удаление и возвращение элемента с минимальным приоритетом"""
        # если куча содержит один элемент - корень - просто возвращаем его
        if len(self.heap) == 1:
            return self.heap.pop()
        root = self.heap[0]
        self.heap[0] = self.heap.pop()  # перемещаем последний элемент в корень
        self.move_down(0)
        return root

    def move_up(self, index):
        """Перемещает элемент вверх для сохранения свойств кучи"""
        parent = (index - 1) // 2
        while index > 0 and self.heap[index][0] < self.heap[parent][0]:
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            index = parent
            parent = (index - 1) // 2

    def move_down(self, index):
        """Перемещает элемент вниз для сохранения свойств кучи"""
        child = 2 * index + 1
        while child < len(self.heap):
            # выбираем меньшего ребёнка
            if child + 1 < len(self.heap) and self.heap[child + 1][0] < self.heap[child][0]:
                child += 1
            # если текущий узел меньше ребёнка, завершить
            if self.heap[index][0] <= self.heap[child][0]:
                break
            # иначе меняем местами
            self.heap[index], self.heap[child] = self.heap[child], self.heap[index]
            index = child
            child = 2 * index + 1

    def is_empty(self):
        """Проверка кучи на пустоту"""
        return not self.heap