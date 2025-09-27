
# Sistema de Gestión de Datos con Algoritmos Optimizados

## Descripción
Este proyecto implementa un Sistema de Gestión de Datos que permite generar datasets aleatorios, aplicar múltiples algoritmos de ordenamiento y búsqueda, analizar su rendimiento y visualizar los resultados. Además, incluye una aplicación real de inventario para productos, con ordenamiento, búsquedas y top ventas.

## Estructura del Proyecto

Proyecto_Algoritmos_William/
│
├── README.md                        # Documentación del proyecto
├── analisis_algoritmos.ipynb        # Notebook principal
├── analisis.py                      # Módulo de análisis de datasets
├── generador_datos.py               # Generación de datasets aleatorios
├── algoritmos.py                     # Implementación de algoritmos de ordenamiento y búsqueda
├── inventario.py                     # Aplicación real: inventario de productos
├── utils.py                          # Funciones auxiliares (graficar, medir tiempos)
├── datasets/                         # Carpeta con archivos CSV generados
├── resultados/                       # Carpeta con resultados y gráficas
├── graficas.py                        # Generación de gráficas
├── screenshots/                       # Capturas de evidencia
└── informe_tecnico_algoritmos.pdf     # Informe técnico (2-3 páginas)

## Requisitos

- Python 3.8+
- Librerías necesarias:

```bash
pip install numpy pandas matplotlib seaborn
```

- IDE recomendado: VS Code con extensión de Python
- Jupyter Notebook: opcional para ejecutar `analisis_algoritmos.ipynb`

## Instrucciones de Ejecución

### 1️⃣ Generar Datasets
```bash
python generador_datos.py
```
- Crea archivos CSV en `datasets/` con distribuciones:
  - Uniforme
  - Gaussiana
  - Sesgada  
- Tamaños: 100, 1000, 10000 elementos

### 2️⃣ Analizar Datasets
```bash
python analisis.py
```
- Calcula estadísticas: media, mediana, varianza, mínimo y máximo  
- Genera `resultados_analisis.csv` en la raíz del proyecto

### 3️⃣ Generar Gráficas
```bash
python graficas.py
```
- Gráficas de barras, heatmaps y líneas  
- Guardadas en `graficas/` en alta resolución (300 dpi)

### 4️⃣ Aplicación Real: Inventario de Productos
```bash
python inventario.py
```
- Genera 1000 productos aleatorios con 5 atributos: nombre, precio, stock, ventas y categoría  
- Funcionalidades:
  - Ordenar por precio o nombre
  - Buscar por rango de precios
  - Obtener top 10 productos más vendidos

## Notebook Jupyter
- Archivo: `analisis_algoritmos.ipynb`  
- Contiene ejecución paso a paso de:
  - Generación de datasets
  - Algoritmos de ordenamiento y búsqueda
  - Análisis de tiempos y comparaciones
  - Visualización de resultados

## Entregables
- `proyecto_algoritmos.zip` → Código fuente completo
- `analisis_completo.ipynb` → Notebook con análisis y visualización
- `informe_tecnico_algoritmos.pdf` → Informe resumido 2-3 páginas
- `screenshots/` → Evidencias del proyecto
- `README.md` → Este documento con instrucciones

## Autor
William Alexis Peñaranda Castro

## Nota
Este proyecto sigue un flujo modular:
1. Generación de datos  
2. Aplicación de algoritmos  
3. Análisis estadístico  
4. Visualización  
5. Aplicación real de inventario  

Se puede ejecutar de manera independiente cada módulo o de manera completa para un análisis integral.
