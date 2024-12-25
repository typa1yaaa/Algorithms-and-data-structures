"""
Модуль реализации развернутого связанного списка (Unrolled Linked List).
"""

import math


def calculate_optimal_node_size(num_elements: int) -> int:
    """
    Рассчитывает оптимальный размер узла на основе количества элементов.
    """
    elem_byte = 4
    total_memory_capa = elem_byte * num_elements
    min_cache_line_size = 64
    num_of_cache_lines = math.ceil(total_memory_capa / min_cache_line_size)
    optimal_node_size = num_of_cache_lines + 1
    return optimal_node_size


class NodeForULL:
    """
    Класс, представляющий узел для развернутого связанного списка.
    """

    def __init__(self, size: int):
        """
        Инициализирует узел с указанным размером.
        """
        self.values: list[int] = []
        self.size: int = size
        self.next: 'NodeForULL | None' = None

    def __len__(self) -> int:
        """
        Возвращает количество элементов в узле.
        """
        return len(self.values)

    def __str__(self) -> str:
        """
        Возвращает строковое представление узла.
        """
        return f"Node(size={self.size}, values={self.values})"


class UnrolledLinkedList:
    """
    Класс, представляющий развернутый связанный список.
    """

    def __init__(self, node_capacity: int):
        """
        Инициализирует развернутый связанный список с заданной емкостью узла.
        """
        self.head: 'NodeForULL | None' = None
        self.node_capacity: int = node_capacity

    def prepend(self, new_value: int) -> None:
        """
        Добавляет элемент в начало списка.
        """
        new_node = NodeForULL(self.node_capacity)
        new_node.values.append(new_value)

        if not self.head:
            self.head = new_node
            return

        current = self.head
        if len(current.values) < self.node_capacity:
            new_node.values.extend(current.values)
            new_node.next = current.next
            self.head = new_node
        else:
            new_node.next = current
            self.head = new_node

    def insert_middle(self, new_value: int) -> None:
        """
        Вставляет элемент в середину списка.
        """
        if self.head is None:
            self.head = NodeForULL(self.node_capacity)
            self.head.values.append(new_value)
            return

        slow = self.head
        fast = self.head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        if len(slow.values) < self.node_capacity:
            slow.values.append(new_value)
        else:
            new_node = NodeForULL(self.node_capacity)
            mid_index = len(slow.values) // 2
            new_node.values = slow.values[mid_index:]
            slow.values = slow.values[:mid_index]
            new_node.next = slow.next
            slow.next = new_node
            slow.values.append(new_value)

    def append(self, new_value: int) -> None:
        """
        Добавляет элемент в конец списка.
        """
        if self.head is None:
            self.head = NodeForULL(self.node_capacity)
            self.head.values.append(new_value)
        else:
            current = self.head
            while current.next:
                current = current.next
            if len(current.values) < self.node_capacity:
                current.values.append(new_value)
            else:
                new_node = NodeForULL(self.node_capacity)
                new_node.values.append(new_value)
                current.next = new_node

    def delete(self, delete_value: int) -> None:
        """
        Удаляет указанный элемент из списка.
        """
        current = self.head
        prev = None

        while current:
            if delete_value in current.values:
                current.values.remove(delete_value)
                if not current.values and prev:
                    prev.next = current.next
                return
            prev = current
            current = current.next

    def search(self, search_value: int) -> bool:
        """
        Выполняет поиск элемента в списке.
        """
        current = self.head
        while current:
            if search_value in current.values:
                return True
            current = current.next
        return False

    def clear(self) -> None:
        """
        Очищает весь список.
        """
        self.head = None

    def print_list(self) -> None:
        """
        Выводит содержимое списка.
        """
        current = self.head
        node_index = 0
        while current:
            print(f"Node {node_index}: {' '.join(map(str, current.values))}")
            current = current.next
            node_index += 1


def check(arr_1: list[int], arr_2: list[int], n_array: int | None = None) -> None:
    """
    Проверяет работу развернутого связанного списка:
    добавляет элементы из arr_1 и удаляет те, что есть в arr_2.
    """
    if n_array is None:
        n_array = calculate_optimal_node_size(len(arr_1))

    final_list = UnrolledLinkedList(n_array)

    for elem in arr_1:
        final_list.append(elem)
        final_list.print_list()

    for elem in arr_2:
        if final_list.search(elem):
            final_list.delete(elem)
            final_list.print_list()


if __name__ == "__main__":
    values = list(map(int, input("Введите числа через пробел: ").split()))
    calculated_node_size = calculate_optimal_node_size(len(values))
    unrolled_linked_list = UnrolledLinkedList(calculated_node_size)

    for val in values:
        unrolled_linked_list.append(val)

    unrolled_linked_list.print_list()