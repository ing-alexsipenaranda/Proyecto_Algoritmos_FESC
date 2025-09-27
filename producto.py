# producto.py
import random
from algoritmos import bubble_sort, merge_sort


class Producto:
    def __init__(self, id_: int, nombre: str, precio: int, stock: int, vendidos: int):
        self.id = id_
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
        self.vendidos = vendidos

    def __repr__(self):
        return f"Producto(id={self.id}, nombre='{self.nombre}', precio={self.precio}, stock={self.stock}, vendidos={self.vendidos})"


def random_name():
    adjs = ["Alpha", "Beta", "Delta", "Gamma", "Eco", "Pro", "Max", "Lite", "Ultra", "Nova"]
    nouns = ["Boot", "Shield", "Safe", "Seat", "Filter", "Gear", "Pack", "Bag", "Chair", "Mask"]
    return random.choice(adjs) + " " + random.choice(nouns) + " " + str(random.randint(1, 999))


def generate_products(n=1000, seed=12345):
    random.seed(seed)
    products = []
    for i in range(1, n + 1):
        nombre = random_name()
        precio = random.randint(10000, 500000)
        stock = random.randint(0, 500)
        vendidos = random.randint(0, 2000)
        products.append(Producto(i, nombre, precio, stock, vendidos))
    return products


def sort_products(products, key_attr='precio', algorithm='merge'):
    key = (lambda p: getattr(p, key_attr))
    if algorithm == 'bubble':
        sorted_list, comps = bubble_sort(products, key=key)
    else:
        # usar merge sort por defecto (eficiente)
        sorted_list, comps = merge_sort(products, key=key)
    return sorted_list, comps


def search_price_range(products, low, high, use_binary=False):
    # Devuelve sublista con productos cuyo precio está en [low, high]
    if not use_binary:
        return [p for p in products if low <= p.precio <= high]
    else:
        # Si se usa binaria, primero ordenar por precio
        sorted_products, _ = sort_products(products, key_attr='precio', algorithm='merge')

        # buscar primer índice >= low y último <= high
        def left_bound(arr, target):
            lo, hi = 0, len(arr)
            while lo < hi:
                mid = (lo + hi) // 2
                if arr[mid].precio < target:
                    lo = mid + 1
                else:
                    hi = mid
            return lo

        def right_bound(arr, target):
            lo, hi = 0, len(arr)
            while lo < hi:
                mid = (lo + hi) // 2
                if arr[mid].precio <= target:
                    lo = mid + 1
                else:
                    hi = mid
            return lo - 1

        L = left_bound(sorted_products, low)
        R = right_bound(sorted_products, high)
        if L <= R:
            return sorted_products[L:R + 1]
        else:
            return []


def top_n_most_sold(products, n=10):
    return sorted(products, key=lambda p: p.vendidos, reverse=True)[:n]


if __name__ == "__main__":
    prods = generate_products(100)
    print("Productos generados:")
    for p in prods[:5]:
        print(p)
    sorted_by_price, comps = sort_products(prods, key_attr='precio', algorithm='merge')
    print(f"\nProductos ordenados por precio (primeros 5):")
    for p in sorted_by_price[:5]:
        print(p)
    in_range = search_price_range(prods, 50000, 100000, use_binary=True)
    print(f"\nProductos con precio entre 50000 y 100000 (total {len(in_range)}):")
    for p in in_range[:5]:
        print(p)
    top_sold = top_n_most_sold(prods, n=5)
    print(f"\nTop 5 productos más vendidos:")
    for p in top_sold:
        print(p)
