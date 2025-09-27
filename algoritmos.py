# algoritmos.py
"""Implementa 5 algoritmos de ordenamiento con contador de comparaciones
y búsquedas lineal y binaria. Todas las funciones aceptan `key` opcional.
"""
from typing import Callable, Iterable, List, Tuple


class Counter:
    def __init__(self):
        self.count = 0

    def inc(self, n=1):
        self.count += n


# Cada algoritmo recibe arr (iterable) y key (función) y devuelve (sorted_list, comparisons)


def bubble_sort(arr: Iterable, counter: Counter = None, key: Callable = lambda x: x) -> Tuple[List, int]:
    if counter is None:
        counter = Counter()
    a = list(arr)
    n = len(a)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            counter.inc()
            if key(a[j]) > key(a[j + 1]):
                a[j], a[j + 1] = a[j + 1], a[j]
                swapped = True
        if not swapped:
            break
    return a, counter.count


def insertion_sort(arr: Iterable, counter: Counter = None, key: Callable = lambda x: x) -> Tuple[List, int]:
    if counter is None:
        counter = Counter()
    a = list(arr)
    for i in range(1, len(a)):
        current = a[i]
        j = i - 1
        while j >= 0:
            counter.inc()
            if key(a[j]) > key(current):
                a[j + 1] = a[j]
                j -= 1
            else:
                break
        a[j + 1] = current
    return a, counter.count


def selection_sort(arr: Iterable, counter: Counter = None, key: Callable = lambda x: x) -> Tuple[List, int]:
    if counter is None:
        counter = Counter()
    a = list(arr)
    n = len(a)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            counter.inc()
            if key(a[j]) < key(a[min_idx]):
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
    return a, counter.count


def merge_sort(arr: Iterable, counter: Counter = None, key: Callable = lambda x: x) -> Tuple[List, int]:
    if counter is None:
        counter = Counter()
    a = list(arr)

    def merge(left, right):
        merged = []
        i = j = 0
        while i < len(left) and j < len(right):
            counter.inc()
            if key(left[i]) <= key(right[j]):
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1
        merged.extend(left[i:])
        merged.extend(right[j:])
        return merged

    def msort(lst):
        if len(lst) <= 1:
            return lst
        mid = len(lst) // 2
        return merge(msort(lst[:mid]), msort(lst[mid:]))

    res = msort(a)
    return res, counter.count


def quick_sort(arr: Iterable, counter: Counter = None, key: Callable = lambda x: x) -> Tuple[List, int]:
    if counter is None:
        counter = Counter()
    a = list(arr)

    def qsort(lst):
        if len(lst) <= 1:
            return lst
        pivot = lst[len(lst) // 2]
        left = []
        equal = []
        right = []
        for item in lst:
            counter.inc()
            if key(item) < key(pivot):
                left.append(item)
            elif key(item) > key(pivot):
                right.append(item)
            else:
                equal.append(item)
        return qsort(left) + equal + qsort(right)

    res = qsort(a)
    return res, counter.count


# BÚSQUEDAS

def linear_search(arr: Iterable, target, key: Callable = lambda x: x) -> Tuple[int, int]:
    c = Counter()
    for i, item in enumerate(arr):
        c.inc()
        if key(item) == target:
            return i, c.count
    return -1, c.count


def binary_search(arr: Iterable, target, key: Callable = lambda x: x) -> Tuple[int, int]:
    # arr debe estar ordenado por key
    c = Counter()
    a = list(arr)
    lo = 0
    hi = len(a) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        c.inc()
        if key(a[mid]) == target:
            return mid, c.count
        elif key(a[mid]) < target:
            lo = mid + 1
        else:
            hi = mid - 1
    return -1, c.count
if __name__ == "__main__":
    datos_prueba = [5, 2, 9, 1, 5, 6]

    print("Datos originales:", datos_prueba)

    # ORDENAMIENTOS
    print("\n--- ORDENAMIENTOS ---")
    for nombre, algoritmo in [
        ("Burbuja", bubble_sort),
        ("Inserción", insertion_sort),
        ("Selección", selection_sort),
        ("MergeSort", merge_sort),
        ("QuickSort", quick_sort),
    ]:
        ordenados, comps = algoritmo(datos_prueba)
        print(f"{nombre:10}: {ordenados} | Comparaciones: {comps}")

    # BÚSQUEDAS
    print("\n--- BÚSQUEDAS ---")
    ordenados, _ = quick_sort(datos_prueba)
    idx, comps = linear_search(ordenados, 5)
    print(f"Búsqueda lineal (5): índice={idx}, comparaciones={comps}")

    idx, comps = binary_search(ordenados, 5)
    print(f"Búsqueda binaria (5): índice={idx}, comparaciones={comps}")
