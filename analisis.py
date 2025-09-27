# analisis.py
"""
Módulo 3 - Análisis de Algoritmos
---------------------------------
- Ejecuta cada algoritmo 10 veces por dataset
- Calcula media y desviación estándar de comparaciones y tiempo
- Genera matriz de resultados para identificar el mejor algoritmo
"""

import os
import pandas as pd
import numpy as np
from algoritmos import bubble_sort, insertion_sort, selection_sort, merge_sort, quick_sort

DATA_DIR = "data"
RESULTADOS_FILE = "resultados_analisis.csv"
EJECUCIONES = 10  # número de repeticiones por algoritmo/dataset

algoritmos = [
    ("Bubble Sort", bubble_sort),
    ("Insertion Sort", insertion_sort),
    ("Selection Sort", selection_sort),
    ("Merge Sort", merge_sort),
    ("Quick Sort", quick_sort)
]

def analizar():
    resultados = []

    # Recorremos todos los archivos de ./data
    for archivo in os.listdir(DATA_DIR):
        if archivo.endswith(".csv"):
            ruta = os.path.join(DATA_DIR, archivo)
            print(f"📊 Analizando {archivo}...")

            df = pd.read_csv(ruta)
            if "value" not in df.columns:
                raise KeyError(
                    f"El archivo {archivo} no contiene la columna 'value'. "
                    f"Columnas encontradas: {list(df.columns)}"
                )

            datos = df["value"].tolist()
            tamaño = len(datos)

            # Ejecutar cada algoritmo EJECUCIONES veces
            for nombre_alg, func_alg in algoritmos:
                tiempos = []
                comps = []

                for _ in range(EJECUCIONES):
                    _, comparaciones, tiempo = func_alg(datos)
                    tiempos.append(tiempo)
                    comps.append(comparaciones)

                # Calcular media y desviación estándar
                media_tiempo = np.mean(tiempos)
                std_tiempo = np.std(tiempos)
                media_comps = np.mean(comps)
                std_comps = np.std(comps)

                resultados.append({
                    "archivo": archivo,
                    "tamaño": tamaño,
                    "algoritmo": nombre_alg,
                    "media_tiempo": media_tiempo,
                    "std_tiempo": std_tiempo,
                    "media_comparaciones": media_comps,
                    "std_comparaciones": std_comps
                })

    # Guardar resultados en CSV
    resultados_df = pd.DataFrame(resultados)
    resultados_df.to_csv(RESULTADOS_FILE, index=False)
    print(f"\n✅ Análisis completado. Resultados guardados en {RESULTADOS_FILE}")

if __name__ == "__main__":
    analizar()