"""Реализация алгоритма Рабина-Карпа"""

def polynomial_hash(input_string, base=26, mod=1_000_000_007):
    """Вычисление полиномиального хэша строки."""
    hash_value = 0
    for char in input_string:
        hash_value = (hash_value * base + ord(char)) % mod
    return hash_value

def cmp(str1, str2):
    """Сравнение двух строк"""
    counter = 0
    for val1, val2 in zip(str1, str2):
        if val1 == val2:
            counter += 1
        else:
            return False

    if counter == len(str1):
        return True

def get_sub_string_RK(pattern, text):
    """Алгоритм Рабина-Карпа"""
    len_pattern = len(pattern)
    len_text = len(text)
    hash_pattern = polynomial_hash(pattern)

    index = []
    for i in range(len_text-len_pattern+1):
        if polynomial_hash(text[i:i+len_pattern]) == hash_pattern:
            # посимвольное сравнение
            if cmp(text[i:i+len_pattern], pattern):
                index.append(i)
    res = [str(i) for i in index]
    return " ".join(res)

def main():
    """Головная функция"""
    pattern = input()
    text = input()
    print(get_sub_string_RK(pattern, text))

main()