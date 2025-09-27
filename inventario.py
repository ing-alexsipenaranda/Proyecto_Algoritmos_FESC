import random
import string

class Producto:
    """Clase que representa un producto en el inventario."""
    def __init__(self, nombre, precio, stock, ventas, categoria):
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
        self.ventas = ventas
        self.categoria = categoria

    def __repr__(self):
        return f"{self.nombre} | Precio: ${self.precio} | Ventas: {self.ventas} | Stock: {self.stock} | Categoria: {self.categoria}"

# ------------------- Generar productos aleatorios -------------------
def generar_productos(n=1000):
    """
    Genera una lista de n productos aleatorios.
    """
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
    Ordena productos según la clave ('precio' o 'nombre') y orden.
    """
    return sorted(productos, key=lambda x: getattr(x, clave), reverse=reverse)

# ------------------- Búsqueda por rango de precios -------------------
def buscar_por_rango_precio(productos, minimo, maximo):
    """
    Retorna los productos cuyo precio está entre minimo y maximo.
    """
    return [p for p in productos if minimo <= p.precio <= maximo]

# ------------------- Top 10 productos más vendidos -------------------
def top_10_mas_vendidos(productos):
    """
    Retorna los 10 productos con más ventas.
    """
    return ordenar_productos(productos, clave='ventas', reverse=True)[:10]

# ------------------- Estadísticas resumidas -------------------
def estadisticas(productos):
    precios = [p.precio for p in productos]
    ventas = [p.ventas for p in productos]
    return {
        "precio_min": min(precios),
        "precio_max": max(precios),
        "precio_prom": round(sum(precios)/len(precios), 2),
        "ventas_max": max(ventas),
        "ventas_prom": round(sum(ventas)/len(ventas), 2)
    }

# ------------------- Ejemplo de uso -------------------
if __name__ == "__main__":
    productos = generar_productos(1000)
    print("✅ Productos generados")

    # Estadísticas generales
    stats = estadisticas(productos)
    print(f"\n📊 Estadísticas generales: {stats}")

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

    top_ventas = top_10_mas_vendidos(productos)
    print("\n🏆 Top 10 productos más vendidos:")
    print(top_ventas)