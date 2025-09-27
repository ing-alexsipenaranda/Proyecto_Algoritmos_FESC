# algoritmos.py
"""
Módulo de Algoritmos Optimizado
-------------------------------
Incluye:
- 5 algoritmos de ordenamiento con contador de comparaciones
- Búsqueda lineal y binaria con contador
- Decorador para medir tiempo de ejecución
- Función para guardar resultados en CSV
"""

import time
import csv
from typing import Callable, Iterable, List, Tuple

# ------------------- Contador -------------------
class Counter:
    def __init__(self):
        self.count = 0

    def inc(self, n=1):
        self.count += n

# ------------------- Decorador de tiempo -------------------
def medir_tiempo(func):
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        resultado = func(*args, **kwargs)
        end = time.perf_counter()
        tiempo = end - start
        return resultado + (tiempo,)  # retorna tupla (resultado, comparaciones, tiempo)
    return wrapper

# ------------------- Algoritmos de Ordenamiento -------------------
@medir_tiempo
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

@medir_tiempo
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

@medir_tiempo
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

@medir_tiempo
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

@medir_tiempo
def quick_sort(arr: Iterable, counter: Counter = None, key: Callable = lambda x: x) -> Tuple[List, int]:
    if counter is None:
        counter = Counter()
    a = list(arr)

    def qsort(lst):
        if len(lst) <= 1:
            return lst
        pivot = lst[len(lst) // 2]
        left, equal, right = [], [], []
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

# ------------------- Búsquedas -------------------
def linear_search(arr: Iterable, target, key: Callable = lambda x: x) -> Tuple[int, int]:
    c = Counter()
    for i, item in enumerate(arr):
        c.inc()
        if key(item) == target:
            return i, c.count
    return -1, c.count

def binary_search(arr: Iterable, target, key: Callable = lambda x: x) -> Tuple[int, int]:
    c = Counter()
    a = list(arr)
    lo, hi = 0, len(a) - 1
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

# ------------------- Guardar resultados en CSV -------------------
def guardar_resultados_csv(nombre_archivo: str, datos: List[dict]):
    """Recibe lista de dicts y guarda en CSV"""
    if not datos:
        return
    campos = list(datos[0].keys())
    with open(nombre_archivo, mode='w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=campos)
        writer.writeheader()
        writer.writerows(datos)

# ------------------- Ejemplo de uso -------------------
if __name__ == "__main__":
    # Datos de prueba
    datos = [5, 2, 9, 1, 5, 6]

    algoritmos = [
        ("Bubble Sort", bubble_sort),
        ("Insertion Sort", insertion_sort),
        ("Selection Sort", selection_sort),
        ("Merge Sort", merge_sort),
        ("Quick Sort", quick_sort)
    ]

    resultados = []
    for nombre, alg in algoritmos:
        sorted_list, comps, tiempo = alg(datos)
        print(f"{nombre}: {sorted_list} | Comparaciones: {comps} | Tiempo: {tiempo:.6f}s")
        resultados.append({
            "algoritmo": nombre,
            "comparaciones": comps,
            "tiempo_segundos": tiempo,
            "dataset": datos
        })

    # Guardar resultados en CSV
    guardar_resultados_csv("resultados_algoritmos.csv", resultados)
    print("\n✅ Resultados guardados en resultados_algoritmos.csv")