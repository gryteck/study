def bubble1(a: list) -> list:  # попарно сравнивает элементы и меняет их при необходимости (с флагом)
    if not a:
        return []
    while True:
        flag = False
        for i in range(len(a) - 1):
            if a[i] > a[i + 1]:
                a[i], a[i + 1] = a[i + 1], a[i]
                flag = True
        if not flag:
            return a


def bubble2(array):  # попарно сравниваем и сортируем (без флага)
    n = len(array)
    for i in range(n):
        for j in range(0, n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array


def selection(a: list) -> list:  # находит минимумы и вставляет их по порядку
    if not a:
        return []
    m = 0
    while m < len(a) - 1:
        flag = False
        min_i = m
        for i in range(m + 1, len(a)):
            if a[i] < a[min_i]:
                min_i = i
                flag = True
        if flag:
            a.insert(m, a.pop(min_i))
        m += 1
    return a


def insertion(a: list) -> list:  # создаем новый список и вставляем в него
    if not a:
        return []
    b = a[:1:]
    for i in range(1, len(a)):
        ind = len(b)
        for j in range(len(b)):
            if b[j] > a[i]:
                ind = j
                break
        b.insert(ind, a[i])
    return b


def quick(a: list) -> list:  # делим список по опорному элементу и рекурсивно сортируем два списка
    if not a or len(a) < 2:
        return a
    pivot = a[0]
    left, right = [], []
    for i in range(1, len(a)):
        if a[i] <= pivot:
            left.append(a[i])
        else:
            right.append(a[i])
    return quick(left) + [pivot] + quick(right)


def hard_quick(a: list) -> list:
    if not a or len(a) < 2:
        return a
    else:
        left, right, pivot = [], [], a[0]
        left = [i for i in a[1:] if i <= pivot]
        right = [i for i in a[1:] if i > pivot]
        return quick(left) + [pivot] + quick(right)


if __name__ == '__main__':
    tests = [
        [5, 2, 9, 0, 11, 3],
        [1, 2, 3, 4, 5, 6],
        [],
        [1, 1, 1, 5, 1]
    ]

    for test in tests:
        print(hard_quick(test))
