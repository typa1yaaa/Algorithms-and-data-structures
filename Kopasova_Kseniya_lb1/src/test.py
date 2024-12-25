import time
import random
import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from main import UnrolledLinkedList, calculate_optimal_node_size

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# Односвязный список       
class LinkedList:
    def __init__(self):
        self.head = None 
        
    # Поиск 
    def search(self, search_value):  
        current = self.head

        while current:
            if current.value == search_value:
                return True
            current = current.next
        return False
    
    # Удаление
    def delete(self, delete_value):  
        current = self.head
        
        if current and current.value == delete_value:
            self.head = current.next
            return

        prev = None
        while current and current.value != delete_value:
            prev = current
            current = current.next
        
        if current is None:
            return
        
        prev.next = current.next

    # Добавление элемента в начало
    def prepend(self, value):  
        new_value = Node(value)
        new_value.next = self.head
        self.head = new_value 

    # Вставка в середину
    def insert_middle(self, value):
        new_value = Node(value)
        
        if not self.head:  # Если список пуст, добавляем элемент в начало
            self.head = new_value
            return
        
        slow = self.head
        fast = self.head
        
        # Находим средний узел
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Вставляем новый узел после среднего узла
        new_value.next = slow.next
        slow.next = new_value

    # Вставка в конец
    def append(self, value):
        new_value = Node(value)
        if self.head is None:
            self.head = new_value
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_value

    def clear(self):
        self.head = None

    # Вывод списка 
    def print_list(self): 
        current = self.head
        result = []
        while current:
            result.append(current.value)
            current = current.next
        print(" ".join(map(str, result)))

# Функция проверки затраченного времени у массива на вставку/поиск/удаление в начало
def array_elapsed_time_ins_ser_del_begin():
    result_time_array_ins_ser_del_begin = [[], [], []]
    #100 элементов
    array_1 = np.random.randint(1, 100, 100)
    working_array = []
    time_start_array_1 = time.time()
    #вставка в начало массива
    for i in array_1:
        working_array.insert(0,int(i))
    time_end_array_1 = time.time()
    result_time_array_ins_ser_del_begin[0].append(time_end_array_1 - time_start_array_1)
    #поиск в начале массива
    time_start_array_1 = time.time()
    for i in array_1[::-1]:
        for j in working_array:
            if j == i:
                continue
    time_end_array_1 = time.time()
    result_time_array_ins_ser_del_begin[1].append(time_end_array_1 - time_start_array_1)
    #удаление в начале массива
    time_start_array_1 = time.time()
    while working_array:
        working_array.pop(0)
    time_end_array_1 = time.time()
    result_time_array_ins_ser_del_begin[2].append(time_end_array_1 - time_start_array_1)
    
    #10к элементов
    array_2 = np.random.randint(1, 1000, 1000)
    time_start_array_2 = time.time()
    #вставка в начало массива
    for i in array_2:
        working_array.insert(0, int(i))
    time_end_array_2 = time.time()
    result_time_array_ins_ser_del_begin[0].append(time_end_array_2 - time_start_array_2)
    #поиск в начале массива
    time_start_array_2 = time.time()
    for i in array_2[::-1]:
        for j in working_array:
            if j == i:
                continue
    time_end_array_2 = time.time()
    result_time_array_ins_ser_del_begin[1].append(time_end_array_2 - time_start_array_2)
    #удаление в начале массива
    time_start_array_2 = time.time()
    while working_array:
        working_array.pop(0)
    time_end_array_2 = time.time()
    result_time_array_ins_ser_del_begin[2].append(time_end_array_2 - time_start_array_2)
    

    #100к элементов
    array_3 = np.random.randint(1, 10000, 10000)
    time_start_array_3 = time.time()
    #вставка в начало массива
    for i in array_3:
        working_array.insert(0, int(i))
    time_end_array_3 = time.time()
    result_time_array_ins_ser_del_begin[0].append(time_end_array_3 - time_start_array_3)
    #поиск в начале массива
    time_start_array_3 = time.time() #тоже ну оооочень долго :(
    for i in array_3[::-1]:
        for j in working_array:
            if j == i:
                continue
    time_end_array_3 = time.time()
    result_time_array_ins_ser_del_begin[1].append(time_end_array_3 - time_start_array_3)
    #удаление в начале массива
    time_start_array_3 = time.time()
    while working_array:
        working_array.pop(0)
    time_end_array_3 = time.time()
    result_time_array_ins_ser_del_begin[2].append(time_end_array_3 - time_start_array_3)
    
    return result_time_array_ins_ser_del_begin

# Функция проверки затраченного времени у массива на вставку/поиск/удаление в середину
def array_elapsed_time_ins_ser_del_middle():
    result_time_array_ins_ser_del_middle = [[], [], []]
    #100 элементов
    array_1 = np.random.randint(1, 100, 100)
    working_array = []
    time_start_array_1 = time.time()
    #вставка в середину массива
    for i in array_1:
        working_array.insert(int(len(working_array)/2),int(i))
    time_end_array_1 = time.time()
    result_time_array_ins_ser_del_middle[0].append(time_end_array_1 - time_start_array_1)
    #поиск в середине массива
    time_start_array_1 = time.time()
    for i in range(int(len(array_1)/2), len(array_1) + len(array_1)%2):
        for j in range(0, int(len(working_array)/2 + len(working_array)%2)):
            if j == i:
                continue
    for i in range(0, int(len(array_1)+len(array_1)%2)):
        for j in range(int(len(working_array)/2), len(working_array)+len(working_array)%2):
            if j == i:
                continue
    time_end_array_1 = time.time()
    result_time_array_ins_ser_del_middle[1].append(time_end_array_1 - time_start_array_1)

    #удаление в середине массива
    time_start_array_1 = time.time()
    while working_array:
        working_array.pop(int(len(working_array)/2))
    time_end_array_1 = time.time()
    result_time_array_ins_ser_del_middle[2].append(time_end_array_1 - time_start_array_1)
    

    #10к элементов
    array_2 = np.random.randint(1, 1000, 1000)
    time_start_array_2 = time.time()
    #вставка в середину массива
    for i in array_2:
        working_array.insert(int(len(working_array)/2), int(i))
    time_end_array_2 = time.time()
    result_time_array_ins_ser_del_middle[0].append(time_end_array_2 - time_start_array_2)
    
    #поиск в середине массива
    time_start_array_2 = time.time()
    for i in range(int(len(array_2)/2), len(array_2) + len(array_2)%2):
        for j in range(0, int(len(working_array)/2 + len(working_array)%2)):
            if j == i:
                continue
    for i in range(0, int(len(array_2)+len(array_2)%2)):
        for j in range(int(len(working_array)/2), len(working_array)+len(working_array)%2):
            if j == i:
                continue
    time_end_array_2 = time.time()
    result_time_array_ins_ser_del_middle[1].append(time_end_array_2 - time_start_array_2)

    #удаление в середине массива
    time_start_array_2 = time.time()
    while working_array:
        working_array.pop(int(len(working_array)/2))
    time_end_array_2 = time.time()
    result_time_array_ins_ser_del_middle[2].append(time_end_array_2 - time_start_array_2)

    #100к элементов
    array_3 = np.random.randint(1, 10000, 10000)
    time_start_array_3 = time.time()
    #вставка в середину массива
    for i in array_3:
        working_array.insert(int(len(working_array)/2), int(i))
    time_end_array_3 = time.time()
    result_time_array_ins_ser_del_middle[0].append(time_end_array_3 - time_start_array_3)
    #поиск в середине массива
    time_start_array_3 = time.time()
    for i in range(int(len(array_3)/2), len(array_3) + len(array_3)%2):
        for j in range(0, int(len(working_array)/2 + len(working_array)%2)):
            if j == i:
                continue
    for i in range(0, int(len(array_3)+len(array_3)%2)):
        for j in range(int(len(working_array)/2), len(working_array)+len(working_array)%2):
            if j == i:
                continue
    time_end_array_3 = time.time()
    result_time_array_ins_ser_del_middle[1].append(time_end_array_3 - time_start_array_3)

    #удаление в середине массива
    time_start_array_3 = time.time()
    while working_array:
        working_array.pop(int(len(working_array)/2))
    time_end_array_3 = time.time()
    result_time_array_ins_ser_del_middle[2].append(time_end_array_3 - time_start_array_3)
    
    return result_time_array_ins_ser_del_middle

# Функция проверки затраченного времени у массива на вставку/поиск/удаление в конец
def array_elapsed_time_ins_ser_del_end():
    result_time_array_ins_ser_del_end = [[], [], []]
    #100 элементов
    array_1 = np.random.randint(1, 100, 100)
    working_array = []
    time_start_array_1 = time.time()
    #вставка в конец массива
    for i in array_1:
        working_array.append(int(i))
    time_end_array_1 = time.time()
    result_time_array_ins_ser_del_end[0].append(time_end_array_1 - time_start_array_1)
    #поиск в конце массива
    time_start_array_1 = time.time()
    for i in array_1:
        for j in working_array:
            if j == i:
                continue
    time_end_array_1 = time.time()
    result_time_array_ins_ser_del_end[1].append(time_end_array_1 - time_start_array_1)
    #удаление в конце массива
    time_start_array_1 = time.time()
    while working_array:
        working_array.pop()
    time_end_array_1 = time.time()
    result_time_array_ins_ser_del_end[2].append(time_end_array_1 - time_start_array_1)
    
    #10к элементов
    array_2 = np.random.randint(1, 1000, 1000)
    time_start_array_2 = time.time()
    #вставка в конец массива
    for i in array_2:
        working_array.append(int(i))
    time_end_array_2 = time.time()
    result_time_array_ins_ser_del_end[0].append(time_end_array_2 - time_start_array_2)
     #поиск в конце массива
    time_start_array_2 = time.time()
    for i in array_2:
        for j in working_array:
            if j == i:
                continue
    time_end_array_2 = time.time()
    result_time_array_ins_ser_del_end[1].append(time_end_array_2 - time_start_array_2)
    #удаление в конце массива
    time_start_array_2 = time.time()
    while working_array:
        working_array.pop()
    time_end_array_2 = time.time()
    result_time_array_ins_ser_del_end[2].append(time_end_array_2 - time_start_array_2)

    #100к элементов
    array_3 = np.random.randint(1, 10000, 10000)
    time_start_array_3 = time.time()
    #вставка в конец массива
    for i in array_3:
        working_array.append(int(i))
    time_end_array_3 = time.time()
    result_time_array_ins_ser_del_end[0].append(time_end_array_3 - time_start_array_3)
     #поиск в конце массива
    time_start_array_3 = time.time()
    for i in array_3:
        for j in working_array:
            if j == i:
                continue
    time_end_array_3 = time.time()
    result_time_array_ins_ser_del_end[1].append(time_end_array_3 - time_start_array_3)
    #удаление в конце массива
    time_start_array_3 = time.time()
    while working_array:
        working_array.pop()
    time_end_array_3 = time.time()
    result_time_array_ins_ser_del_end[2].append(time_end_array_3 - time_start_array_3)
    
    return result_time_array_ins_ser_del_end

# Функция проверки затраченного времени у односвязанного списка на вставку/поиск/удаление в начало
def linkedlist_elapsed_time_ins_ser_del_begin():
    result_time_LL_ins_ser_del_begin = [[], [], []]
    worked_LinkedList = LinkedList()
    #100 элементов
    array_1 = np.random.randint(1, 100, 100)
    time_start_LL_1 = time.time()
    #вставка в начало односвязного списка
    for i in array_1:
        worked_LinkedList.prepend(i)
    time_end_LL_1 = time.time()
    result_time_LL_ins_ser_del_begin[0].append(time_end_LL_1 - time_start_LL_1)
   #поиск в начале односвязного списка
    time_start_array_1 = time.time()
    for i in array_1[::-1]:
        worked_LinkedList.search(i)
    time_end_array_1 = time.time()
    result_time_LL_ins_ser_del_begin[1].append(time_end_array_1 - time_start_array_1)
    #удаление в начале односвязного списка
    time_start_array_1 = time.time()
    for i in array_1[::-1]:
        worked_LinkedList.delete(i)
    time_end_array_1 = time.time()
    result_time_LL_ins_ser_del_begin[2].append(time_end_array_1 - time_start_array_1)

   #10к элементов
    array_2 = np.random.randint(1, 1000, 1000)
    time_start_LL_2 = time.time()
    #вставка в начало односвязного списка
    for i in array_2:
        worked_LinkedList.prepend(i)
    time_end_LL_2 = time.time()
    worked_LinkedList.clear()
    result_time_LL_ins_ser_del_begin[0].append(time_end_LL_2 - time_start_LL_2)
    #поиск в начале односвязного списка
    time_start_array_2 = time.time()
    for i in array_2[::-1]:
        worked_LinkedList.search(i)
    time_end_array_2 = time.time()
    result_time_LL_ins_ser_del_begin[1].append(time_end_array_2 - time_start_array_2)
    #поиск в начале односвязного списка
    time_start_array_2 = time.time()
    for i in array_2[::-1]:
        worked_LinkedList.delete(i)
    time_end_array_2 = time.time()
    result_time_LL_ins_ser_del_begin[2].append(time_end_array_2 - time_start_array_2)

    #100к элементов
    array_3 = np.random.randint(1, 10000, 10000)
    time_start_LL_3 = time.time()
    #вставка в начало односвязного списка
    for i in array_3:
        worked_LinkedList.prepend(i)
    time_end_LL_3 = time.time()
    worked_LinkedList.clear()
    result_time_LL_ins_ser_del_begin[0].append(time_end_LL_3 - time_start_LL_3)
    #поиск в начале односвязного списка
    time_start_array_3 = time.time()
    for i in array_3[::-1]:
        worked_LinkedList.search(i)
    time_end_array_3 = time.time()
    result_time_LL_ins_ser_del_begin[1].append(time_end_array_3 - time_start_array_3)
    #поиск в начале односвязного списка
    time_start_array_3 = time.time()
    for i in array_3[::-1]:
        worked_LinkedList.delete(i)
    time_end_array_3 = time.time()
    result_time_LL_ins_ser_del_begin[2].append(time_end_array_3 - time_start_array_3)

    return result_time_LL_ins_ser_del_begin

# Функция проверки затраченного времени у односвязанного списка на вставку/поиск/удаление в середину
def linkedlist_elapsed_time_ins_ser_del_middle():
    result_time_LL_ins_ser_del_middle = [[], [], []]
    worked_LinkedList = LinkedList()
    #100 элементов
    array_1 = np.random.randint(1, 100, 100)
    time_start_LL_1 = time.time()
    #вставка в середину односвязного списка
    for i in array_1:
        worked_LinkedList.insert_middle(i)
    time_end_LL_1 = time.time()
    worked_LinkedList.clear()
    result_time_LL_ins_ser_del_middle[0].append(time_end_LL_1 - time_start_LL_1)
    #поиск в середине односвязного списка
    time_start_array_1 = time.time()
    for i in range(0, int(len(array_1)+len(array_1)%2)):
        worked_LinkedList.search(i)
    for i in range(int(len(array_1)/2), len(array_1) + len(array_1)%2):
        worked_LinkedList.search(i)
    time_end_array_1 = time.time()
    result_time_LL_ins_ser_del_middle[1].append(time_end_array_1 - time_start_array_1)
    #удаление в середине односвязного списка
    time_start_array_1 = time.time()
    for i in range(0, int(len(array_1)+len(array_1)%2)):
        worked_LinkedList.delete(i)
    for i in range(int(len(array_1)/2), len(array_1) + len(array_1)%2):
        worked_LinkedList.delete(i)
    time_end_array_1 = time.time()
    result_time_LL_ins_ser_del_middle[2].append(time_end_array_1 - time_start_array_1)
 
   #10к элементов
    array_2 = np.random.randint(1, 1000, 1000)
    time_start_LL_2 = time.time()
    #вставка в середину односвязного списка
    for i in array_2:
         worked_LinkedList.insert_middle(i)
    time_end_LL_2 = time.time()
    result_time_LL_ins_ser_del_middle[0].append(time_end_LL_2 - time_start_LL_2)
    #поиск в середине односвязного списка
    time_start_array_2 = time.time()
    for i in range(0, int(len(array_2)+len(array_2)%2)):
        worked_LinkedList.search(i)
    for i in range(int(len(array_2)/2), len(array_2) + len(array_2)%2):
        worked_LinkedList.search(i)
    time_end_array_2 = time.time()
    result_time_LL_ins_ser_del_middle[1].append(time_end_array_2 - time_start_array_2)

    #удаление в середине односвязного списка
    time_start_array_2 = time.time()
    for i in range(0, int(len(array_2)+len(array_2)%2)):
        worked_LinkedList.delete(i)
    for i in range(int(len(array_2)/2), len(array_2) + len(array_2)%2):
        worked_LinkedList.delete(i)
    time_end_array_2 = time.time()
    result_time_LL_ins_ser_del_middle[2].append(time_end_array_2 - time_start_array_2)

    #100к элементов
    array_3 = np.random.randint(1, 10000, 10000)#ооочень долго :(
    time_start_LL_3 = time.time()
    #вставка в середину односвязного списка
    for i in array_3:
        worked_LinkedList.insert_middle(i)
    time_end_LL_3 = time.time()
    result_time_LL_ins_ser_del_middle[0].append(time_end_LL_3 - time_start_LL_3)
     #поиск в середине односвязного списка
    time_start_array_3 = time.time()
    for i in range(0, int(len(array_3)+len(array_3)%2)):
        worked_LinkedList.search(i)
    for i in range(int(len(array_3)/2), len(array_3) + len(array_3)%2):
        worked_LinkedList.search(i)
    time_end_array_3 = time.time()
    result_time_LL_ins_ser_del_middle[1].append(time_end_array_3 - time_start_array_3)
    #удаление в середине односвязного списка
    time_start_array_3 = time.time()
    for i in range(0, int(len(array_3)+len(array_3)%2)):
        worked_LinkedList.delete(i)
    for i in range(int(len(array_3)/2), len(array_3) + len(array_3)%2):
        worked_LinkedList.delete(i)
    time_end_array_3 = time.time()
    result_time_LL_ins_ser_del_middle[2].append(time_end_array_3 - time_start_array_3)

    return result_time_LL_ins_ser_del_middle

# Функция проверки затраченного времени у односвязанного списка на вставку/поиск/удаление в конец
def linkedlist_elapsed_time_ins_ser_del_end():
    result_time_LL_ins_ser_del_end = [[], [], []]
    worked_LinkedList = LinkedList()
    #100 элементов
    array_1 = np.random.randint(1, 100, 100)
    time_start_LL_1 = time.time()
    #вставка в конец односвязного списка
    for i in array_1:
        worked_LinkedList.append(i)
    time_end_LL_1 = time.time()
    result_time_LL_ins_ser_del_end[0].append(time_end_LL_1 - time_start_LL_1)
    #поиск в конце односвязного списка
    time_start_array_1 = time.time()
    for i in array_1:
        worked_LinkedList.search(i)
    time_end_array_1 = time.time()
    result_time_LL_ins_ser_del_end[1].append(time_end_array_1 - time_start_array_1)
    #удаление в конце односвязного списка
    time_start_array_1 = time.time()
    for i in array_1:
        worked_LinkedList.delete(i)
    time_end_array_1 = time.time()
    result_time_LL_ins_ser_del_end[2].append(time_end_array_1 - time_start_array_1)

   #10к элементов
    array_2 = np.random.randint(1, 1000, 1000)
    time_start_LL_2 = time.time()
    #вставка в конец односвязного списка
    for i in array_2:
         worked_LinkedList.append(i)
    time_end_LL_2 = time.time()
    result_time_LL_ins_ser_del_end[0].append(time_end_LL_2 - time_start_LL_2)
    #поиск в конце односвязного списка
    time_start_array_2 = time.time()
    for i in array_2:
        worked_LinkedList.search(i)
    time_end_array_2 = time.time()
    result_time_LL_ins_ser_del_end[1].append(time_end_array_2 - time_start_array_2)
    #удаление в конце односвязного списка
    time_start_array_2 = time.time()
    for i in array_2:
        worked_LinkedList.delete(i)
    time_end_array_2 = time.time()
    result_time_LL_ins_ser_del_end[2].append(time_end_array_2 - time_start_array_2)
    #100к элементов
    array_3 = np.random.randint(1, 10000, 10000)
    time_start_LL_3 = time.time()
    #вставка в конец односвязного списка
    for i in array_3:
        worked_LinkedList.append(i)
    time_end_LL_3 = time.time()
    result_time_LL_ins_ser_del_end[0].append(time_end_LL_3 - time_start_LL_3)
    #поиск в конце односвязного списка
    time_start_array_3 = time.time()
    for i in array_3:
        worked_LinkedList.search(i)
    time_end_array_3 = time.time()
    result_time_LL_ins_ser_del_end[1].append(time_end_array_3 - time_start_array_3)
    #удаление в конце односвязного списка
    time_start_array_3 = time.time()
    for i in array_3:
        worked_LinkedList.delete(i)
    time_end_array_3 = time.time()
    result_time_LL_ins_ser_del_end[2].append(time_end_array_3 - time_start_array_3)
    
    return result_time_LL_ins_ser_del_end

# Функция проверки затраченного времени у развернутого списка на вставку/поиск/удаление в начало
def ULL_elapsed_time_ins_ser_del_begin():
    result_time_ULL_ins_ser_del_begin = [[],[],[]]
    worked_ULL = UnrolledLinkedList(calculate_optimal_node_size(100))
    #100 элементов
    array_1 = np.random.randint(1, 100, 100)
    time_start_ULL_1 = time.time()
    #вставка в начало развернутого списка
    for i in array_1:
        worked_ULL.prepend(i)
    time_end_ULL_1 = time.time()
    result_time_ULL_ins_ser_del_begin[0].append(time_end_ULL_1 - time_start_ULL_1)
    #поиск в начале развернутого списка
    time_start_array_1 = time.time()
    for i in array_1[::-1]:
        worked_ULL.search(i)
    time_end_array_1 = time.time()
    result_time_ULL_ins_ser_del_begin[1].append(time_end_array_1 - time_start_array_1)
    #удаление в начале развернутого списка
    time_start_array_1 = time.time()
    for i in array_1[::-1]:
        worked_ULL.delete(i)
    time_end_array_1 = time.time()
    result_time_ULL_ins_ser_del_begin[2].append(time_end_array_1 - time_start_array_1)

    worked_ULL = UnrolledLinkedList(calculate_optimal_node_size(10000))
    #10к элементов
    array_2 = np.random.randint(1, 1000, 1000)
    time_start_ULL_2 = time.time()
    #вставка в начало развернутого списка
    for i in array_2:
        worked_ULL.prepend(i)
    time_end_ULL_2 = time.time()
    result_time_ULL_ins_ser_del_begin[0].append(time_end_ULL_2 - time_start_ULL_2)
    #поиск в начале развернутого  списка
    time_start_array_2 = time.time()
    for i in array_2[::-1]:
        worked_ULL.search(i)
    time_end_array_2 = time.time()
    result_time_ULL_ins_ser_del_begin[1].append(time_end_array_2 - time_start_array_2)
    #удаление в начале развернутого  списка
    time_start_array_2 = time.time()
    for i in array_2[::-1]:
        worked_ULL.delete(i)
    time_end_array_2 = time.time()
    result_time_ULL_ins_ser_del_begin[2].append(time_end_array_2 - time_start_array_2)

    worked_ULL = UnrolledLinkedList(calculate_optimal_node_size(100000))
    #100к элементов
    array_3 = np.random.randint(1, 10000, 10000)
    time_start_ULL_3 = time.time()
    #вставка в начало развернутого  списка
    for i in array_3:
        worked_ULL.prepend(i)
    time_end_ULL_3 = time.time()
    result_time_ULL_ins_ser_del_begin[0].append(time_end_ULL_3 - time_start_ULL_3)
    #поиск в начале развернутого  списка
    time_start_array_3 = time.time()
    for i in array_3[::-1]:
        worked_ULL.search(i)
    time_end_array_3 = time.time()
    result_time_ULL_ins_ser_del_begin[1].append(time_end_array_3 - time_start_array_3)
    #удаление в начале односвязного списка
    time_start_array_3 = time.time()
    for i in array_3[::-1]:
        worked_ULL.delete(i)
    time_end_array_3 = time.time()
    result_time_ULL_ins_ser_del_begin[2].append(time_end_array_3 - time_start_array_3)

    return result_time_ULL_ins_ser_del_begin

# Функция проверки затраченного времени у развернутого списка на вставку/поиск/удаление в середину
def ULL_elapsed_time_ins_ser_del_middle():
    result_time_ULL_ins_ser_del_middle = [[], [], []]
    worked_ULL = UnrolledLinkedList(calculate_optimal_node_size(100))
    #100 элементов
    array_1 = np.random.randint(1, 100, 100)
    time_start_ULL_1 = time.time()
    #вставка в середину развернутого списка
    for i in array_1:
        worked_ULL.insert_middle(i)
    time_end_ULL_1 = time.time()
    result_time_ULL_ins_ser_del_middle[0].append(time_end_ULL_1 - time_start_ULL_1)
    #поиск в середине односвязного списка
    time_start_array_1 = time.time()
    for i in range(0, int(len(array_1)+len(array_1)%2)):
        worked_ULL.search(i)
    for i in range(int(len(array_1)/2), len(array_1) + len(array_1)%2):
        worked_ULL.search(i)
    time_end_array_1 = time.time()
    result_time_ULL_ins_ser_del_middle[1].append(time_end_array_1 - time_start_array_1)
    #удаление в середине односвязного списка
    time_start_array_1 = time.time()
    for i in range(0, int(len(array_1)+len(array_1)%2)):
        worked_ULL.delete(i)
    for i in range(int(len(array_1)/2), len(array_1) + len(array_1)%2):
        worked_ULL.delete(i)
    time_end_array_1 = time.time()
    result_time_ULL_ins_ser_del_middle[2].append(time_end_array_1 - time_start_array_1)

    worked_ULL = UnrolledLinkedList(calculate_optimal_node_size(10000))
    #10к элементов
    array_2 = np.random.randint(1, 1000, 1000)
    time_start_ULL_2 = time.time()
    #вставка в середину развернутого списка
    for i in array_2:
        worked_ULL.insert_middle(i)
    time_end_ULL_2 = time.time()
    result_time_ULL_ins_ser_del_middle[0].append(time_end_ULL_2 - time_start_ULL_2)
#поиск в середине односвязного списка
    time_start_array_2 = time.time()
    for i in range(0, int(len(array_2)+len(array_2)%2)):
        worked_ULL.search(i)
    for i in range(int(len(array_2)/2), len(array_2) + len(array_2)%2):
        worked_ULL.search(i)
    time_end_array_2 = time.time()
    result_time_ULL_ins_ser_del_middle[1].append(time_end_array_2 - time_start_array_2)
    #удаление в середине односвязного списка
    time_start_array_2 = time.time()
    for i in range(0, int(len(array_2)+len(array_2)%2)):
        worked_ULL.delete(i)
    for i in range(int(len(array_2)/2), len(array_2) + len(array_2)%2):
        worked_ULL.delete(i)
    time_end_array_2 = time.time()
    result_time_ULL_ins_ser_del_middle[2].append(time_end_array_2 - time_start_array_2)

    worked_ULL = UnrolledLinkedList(calculate_optimal_node_size(100000))
    #100к элементов
    array_3 = np.random.randint(1, 10000, 10000)
    time_start_ULL_3 = time.time()
    #вставка в середину развернутого списка
    for i in array_3:
        worked_ULL.insert_middle(i)
    time_end_ULL_3 = time.time()
    result_time_ULL_ins_ser_del_middle[0].append(time_end_ULL_3 - time_start_ULL_3)
    #поиск в середине односвязного списка
    time_start_array_3 = time.time()
    for i in range(0, int(len(array_3)+len(array_3)%2)):
        worked_ULL.search(i)
    for i in range(int(len(array_3)/2), len(array_3) + len(array_3)%2):
        worked_ULL.search(i)
    time_end_array_3 = time.time()
    result_time_ULL_ins_ser_del_middle[1].append(time_end_array_3 - time_start_array_3)
    #удаление в середине односвязного списка
    time_start_array_3 = time.time()
    for i in range(0, int(len(array_3)+len(array_3)%2)):
        worked_ULL.delete(i)
    for i in range(int(len(array_3)/2), len(array_3) + len(array_3)%2):
        worked_ULL.delete(i)
    time_end_array_3 = time.time()
    result_time_ULL_ins_ser_del_middle[2].append(time_end_array_3 - time_start_array_3)

    return result_time_ULL_ins_ser_del_middle

# Функция проверки затраченного времени у развернутого списка на вставку/поиск/удаление в конец
def ULL_elapsed_time_ins_ser_del_end():
    result_time_ULL_ins_ser_del_end = [[],[],[]]
    worked_ULL = UnrolledLinkedList(calculate_optimal_node_size(100))
    #100 элементов
    array_1 = np.random.randint(1, 100, 100)
    time_start_ULL_1 = time.time()
    #вставка в конец развернутого списка
    for i in array_1:
        worked_ULL.append(i)
    time_end_ULL_1 = time.time()
    result_time_ULL_ins_ser_del_end[0].append(time_end_ULL_1 - time_start_ULL_1)
     #поиск в конце односвязного списка
    time_start_array_1 = time.time()
    for i in array_1:
        worked_ULL.search(i)
    time_end_array_1 = time.time()
    result_time_ULL_ins_ser_del_end[1].append(time_end_array_1 - time_start_array_1)
    #удаление в конце односвязного списка
    time_start_array_1 = time.time()
    for i in array_1:
        worked_ULL.delete(i)
    time_end_array_1 = time.time()
    result_time_ULL_ins_ser_del_end[2].append(time_end_array_1 - time_start_array_1)


    worked_ULL = UnrolledLinkedList(calculate_optimal_node_size(10000))
    #10к элементов
    array_2 = np.random.randint(1, 1000, 1000)
    time_start_ULL_2 = time.time()
    #вставка в конец развернутого списка
    for i in array_2:
        worked_ULL.append(i)
    time_end_ULL_2 = time.time()
    result_time_ULL_ins_ser_del_end[0].append(time_end_ULL_2 - time_start_ULL_2)
     #поиск в конце разв списка
    time_start_array_2 = time.time()
    for i in array_2:
        worked_ULL.search(i)
    time_end_array_2 = time.time()
    result_time_ULL_ins_ser_del_end[1].append(time_end_array_2 - time_start_array_2)
    #удаление в конце разв списка
    time_start_array_2 = time.time()
    for i in array_2:
        worked_ULL.delete(i)
    time_end_array_2 = time.time()
    result_time_ULL_ins_ser_del_end[2].append(time_end_array_2 - time_start_array_2)

    worked_ULL = UnrolledLinkedList(calculate_optimal_node_size(100000))
    #100к элементов
    array_3 = np.random.randint(1, 10000, 10000)
    time_start_ULL_3 = time.time()
    #вставка в конец развернутого списка
    for i in array_3:
        worked_ULL.append(i)
    time_end_ULL_3 = time.time()
    result_time_ULL_ins_ser_del_end[0].append(time_end_ULL_3 - time_start_ULL_3)
    #поиск в конце односвязного списка
    time_start_array_3 = time.time()
    for i in array_3:
        worked_ULL.search(i)
    time_end_array_3 = time.time()
    result_time_ULL_ins_ser_del_end[1].append(time_end_array_3 - time_start_array_3)
    #удаление в конце односвязного списка
    time_start_array_3 = time.time()
    for i in array_3:
        worked_ULL.delete(i)
    time_end_array_3 = time.time()
    result_time_ULL_ins_ser_del_end[2].append(time_end_array_3 - time_start_array_3)

    return result_time_ULL_ins_ser_del_end


# Размеры данных
sizes = [100, 10000, 100000]

# Время для массивов
array_times = [
    array_elapsed_time_ins_ser_del_begin(),
    array_elapsed_time_ins_ser_del_middle(),
    array_elapsed_time_ins_ser_del_end(),
]

# Время для односвязных списков
linkedlist_times = [
    linkedlist_elapsed_time_ins_ser_del_begin(),
    linkedlist_elapsed_time_ins_ser_del_middle(),
    linkedlist_elapsed_time_ins_ser_del_end(),
]

# Время для развернутых списков
ULL_times = [
    ULL_elapsed_time_ins_ser_del_begin(),
    ULL_elapsed_time_ins_ser_del_middle(),
    ULL_elapsed_time_ins_ser_del_end(),
]

# Операции
operations = [
    ('Вставка', ['Вставка в начало', 'Вставка в середину', 'Вставка в конец']),
    ('Поиск', ['Поиск в начале', 'Поиск в середине', 'Поиск в конце']),
    ('Удаление', ['Удаление в начале', 'Удаление в середине', 'Удаление в конце'])
]

# Создание графиков
for operation_name, operation_list in operations:
    for i, operation in enumerate(operation_list):
        plt.figure(figsize=(10, 6))
        
        # Время для массивов
        plt.plot(sizes, [array_times[j][i][0] for j in range(len(sizes))], label='Array', marker='o')
        
        # Время для односвязных списков
        plt.plot(sizes, [linkedlist_times[j][i][0] for j in range(len(sizes))], label='Linked List', marker='o')
        
        # Время для развернутых списков
        plt.plot(sizes, [ULL_times[j][i][0] for j in range(len(sizes))], label='Unrolled Linked List', marker='o')
        
        plt.title(f'{operation_name}: {operation}')
        plt.xlabel('Размер структур данных')
        plt.ylabel('Время (секунды)')
        plt.xticks(sizes)
        plt.legend()
        plt.grid()
        plt.show()