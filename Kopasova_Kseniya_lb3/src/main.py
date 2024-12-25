"""Реализация АВЛ-дерева"""
import graphviz

class Node:
    """Класс для узла АВЛ-дерева"""
    
    def __init__(self, val, left=None, right=None):
        """Конструктор узла АВЛ-дерева."""
        self.val = val
        self.left: Node | None = left
        self.right: Node | None = right
        self.height: int = 1


class AVLTree:
    """Класс для АВЛ-дерева."""
    
    def __init__(self) -> None:
        """Конструктор АВЛ-дерева."""
        self.root = None

    def get_min_val_node(self, node: Node):
        """Поиск узла с минимальным значением."""
        while node.left:
            node = node.left
        return node

    def get_max_val_node(self, node: Node):
        """Поиск узла с максимальным значением."""
        while node.right:
            node = node.right
        return node

    def insert(self, val):
        """Вставка элемента в дерево."""
        if not self.root:
            self.root = Node(val)
        else:
            self.root = self._insert(val, self.root)

    def _insert(self, val, node: Node | None):
        """Рекурсивная вставка и балансировка."""
        if not node:
            return Node(val)

        if val < node.val:
            if node.left:
                node.left = self._insert(val, node.left)
        else:
            if node.right:
                node.right = self._insert(val, node.right)

        update_height(node)
        balance = get_balance(node)

        if balance > 1 and val < node.left.val:
            return mini_right_rotate(node)
        if balance < -1 and val > node.right.val:
            return mini_left_rotate(node)
        if balance > 1 and val > node.left.val:
            return max_left_rotate(node)
        if balance < -1 and val < node.right.val:
            return max_right_rotate(node)

        return node

    def remove(self, val):
        """Удаление элемента из дерева."""
        if self.root:
            self.root = self._remove(val, self.root)

    def _remove(self, val, node: Node | None):
        """Рекурсивное удаление и балансировка дерева."""
        if not node:
            return node

        if val < node.val:
            if node.left:
                node.left = self._remove(val, node.left)
        elif val > node.val:
            if node.right:
                node.right = self._remove(val, node.right)
        else:
            # узел без детей или с одним ребенком
            if not node.left:
                return node.right
            elif not node.right:
                return node.left

            # узел с двумя детьми
            temp = self.get_min_val_node(node.right)
            node.val = temp.val
            node.right = self._remove(temp.val, node.right)

        update_height(node)
        balance = get_balance(node)

        if balance > 1 and get_balance(node.left) >= 0:
            return mini_right_rotate(node)
        if balance < -1 and get_balance(node.right) <= 0:
            return mini_left_rotate(node)
        if balance > 1 and get_balance(node.left) < 0:
            return max_left_rotate(node)
        if balance < -1 and get_balance(node.right) > 0:
            return max_right_rotate(node)

        return node

    def remove_min(self):
        """Удаление узла с минимальным значением."""
        if self.root:
            self.root = self._remove_min(self.root)

    def _remove_min(self, node: Node):
        """Рекурсивное удаление узла с минимальным значением."""
        if not node.left:
            return node.right  # узел с минимальным значением

        node.left = self._remove_min(node.left)
        update_height(node)
        balance = get_balance(node)

        if balance > 1 and get_balance(node.left) >= 0:
            return mini_right_rotate(node)
        if balance < -1 and get_balance(node.right) <= 0:
            return mini_left_rotate(node)
        if balance > 1 and get_balance(node.left) < 0:
            return max_left_rotate(node)
        if balance < -1 and get_balance(node.right) > 0:
            return max_right_rotate(node)

        return node

    def remove_max(self):
        """Удаление узла с максимальным значением."""
        if self.root:
            self.root = self._remove_max(self.root)

    def _remove_max(self, node: Node):
        """Рекурсивное удаление узла с максимальным значением."""
        if not node.right:
            return node.left  # узел с максимальным значением

        node.right = self._remove_max(node.right)
        update_height(node)
        balance = get_balance(node)

        if balance > 1 and get_balance(node.left) >= 0:
            return mini_right_rotate(node)
        if balance < -1 and get_balance(node.right) <= 0:
            return mini_left_rotate(node)
        if balance > 1 and get_balance(node.left) < 0:
            return max_left_rotate(node)
        if balance < -1 and get_balance(node.right) > 0:
            return max_right_rotate(node)

        return node


def mini_right_rotate(b: Node) -> Node:
    """Малый правый поворот."""
    a = b.left
    temp = a.right
    a.right = b
    b.left = temp
    update_height(b)
    update_height(a)
    return a


def mini_left_rotate(a: Node) -> Node:
    """Малый левый поворот."""
    b = a.right
    temp = b.left
    b.left = a
    a.right = temp
    update_height(a)
    update_height(b)
    return b


def max_left_rotate(node: Node) -> Node:
    """Большой левый поворот."""
    node.left = mini_left_rotate(node.left)
    return mini_right_rotate(node)


def max_right_rotate(node: Node) -> Node:
    """Большой правый поворот."""
    node.right = mini_right_rotate(node.right)
    return mini_left_rotate(node)


def get_height(node: Node | None) -> int:
    """Определение высоты узла."""
    return node.height if node else 0


def update_height(node: Node):
    """Обновление высоты после балансировки."""
    node.height = max(get_height(node.left), get_height(node.right)) + 1


def get_balance(node: Node) -> int:
    """Определение разницы высот для балансировки."""
    return get_height(node.left) - get_height(node.right) if node else 0


def breadth_first_search(root, dot, step):
    """Визуализация дерева через Graphviz."""
    queue = [(root, "root")]
    dot.node(f"{step}_{root.val}", label=f"{root.val} ")
    while queue:
        tmp_queue = []
        for element in queue:
            if element[0].left:
                dot.node(f"{step}_{element[0].left.val}", label=str(element[0].left.val))
                dot.edge(f"{step}_{element[0].val}", f"{step}_{element[0].left.val}", label="left")
                tmp_queue.append((element[0].left, "left"))
            if element[0].right:
                dot.node(f"{step}_{element[0].right.val}", label=str(element[0].right.val))
                dot.edge(f"{step}_{element[0].val}", f"{step}_{element[0].right.val}", label="right")
                tmp_queue.append((element[0].right, "right"))
        queue = tmp_queue


def main():
    """Основная функция для вставки и удаления узлов из АВЛ-дерева."""
    avl_tree = AVLTree()
    dot_insert = graphviz.Digraph(comment="AVLTree - Insert")
    dot_remove = graphviz.Digraph(comment="AVLTree - Remove")

    # Вставка узлов
    nodes_add = list(map(int, input().split()))
    for step, node in enumerate(nodes_add, 1):
        avl_tree.insert(node)
        breadth_first_search(avl_tree.root, dot_insert, step)
    dot_insert.render("AddElemToAVLTree", format="pdf", cleanup=True)

    # Удаление узлов
    breadth_first_search(avl_tree.root, dot_remove, "initial")
    nodes_remove = list(map(int, input().split()))
    for step, node in enumerate(nodes_remove, 1):
        avl_tree.remove(node)
        breadth_first_search(avl_tree.root, dot_remove, f"remove_any_{node}")
    dot_remove.render("RemoveElemToAVLTree", format="pdf", cleanup=True)


if __name__ == "__main__":
    main()