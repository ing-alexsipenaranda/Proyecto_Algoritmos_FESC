# inventario.py
import random
import string

class Producto:
    def __init__(self, nombre, precio, stock, ventas, categoria):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
        self.ventas = ventas
        self.categoria = categoria

    def __repr__(self):
        return f"{self.nombre} | Precio: {self.precio} | Ventas: {self.ventas}"

# ------------------- Generar productos aleatorios -------------------
def generar_productos(n=1000):
    categorias = ['Electrónica', 'Hogar', 'Seguridad', 'Ropa', 'Deportes']
    productos = []

    for _ in range(n):
        nombre = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
        precio = round(random.uniform(10, 1000), 2)
        stock = random.randint(1, 100)
        ventas = random.randint(0, 500)
        categoria = random.choice(categorias)
        productos.append(Producto(nombre, precio, stock, ventas, categoria))

    return productos

# ------------------- Ordenamiento -------------------
def ordenar_productos(productos, clave='precio', reverse=False):
    """
    clave: 'precio' o 'nombre'
    reverse: True para orden descendente
    """
    return sorted(productos, key=lambda x: getattr(x, clave), reverse=reverse)

# ------------------- Búsqueda por rango de precios -------------------
def buscar_por_rango_precio(productos, minimo, maximo):
    return [p for p in productos if minimo <= p.precio <= maximo]

# ------------------- Top 10 productos más vendidos -------------------
def top_10_mas_vendidos(productos):
    return ordenar_productos(productos, clave='ventas', reverse=True)[:10]

# ------------------- Ejemplo de uso -------------------
if __name__ == "__main__":
    productos = generar_productos(1000)

    print("✅ Productos generados")

    # Ordenar por precio ascendente
    productos_ordenados = ordenar_productos(productos, clave='precio')
    print("\n💰 Productos ordenados por precio (asc):")
    print(productos_ordenados[:10])

    # Ordenar por nombre
    productos_ordenados_nombre = ordenar_productos(productos, clave='nombre')
    print("\n🔤 Productos ordenados por nombre:")
    print(productos_ordenados_nombre[:10])

    # Buscar productos entre $100 y $200
    rango = buscar_por_rango_precio(productos, 100, 200)
    print(f"\n🔎 Productos entre $100 y $200: {len(rango)} encontrados")
    print(rango[:10])

    # Top 10 más vendidos
    top_ventas = top_10_mas_vendidos(productos)
    print("\n🏆 Top 10 productos más vendidos:")
    print(top_ventas)