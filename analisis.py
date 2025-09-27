# analisis.py
import os
import pandas as pd
import numpy as np

DATA_DIR = "data"
RESULTADOS_FILE = "resultados_analisis.csv"

def analizar():
    resultados = []

    # Recorremos todos los archivos de ./data
    for archivo in os.listdir(DATA_DIR):
        if archivo.endswith(".csv"):
            ruta = os.path.join(DATA_DIR, archivo)
            print(f"📊 Analizando {archivo}...")

            # Leer los datos (columna "valor")
            df = pd.read_csv(ruta)
            
            # Asegurarse de que existe la columna "valor"
            if "value" not in df.columns:
                raise KeyError(
                    f"El archivo {archivo} no contiene la columna 'valor'. "
                    f"Columnas encontradas: {list(df.columns)}"
                )

            datos = df["value"].tolist()

            # Calcular estadísticas básicas
            media = np.mean(datos)
            mediana = np.median(datos)
            varianza = np.var(datos)
            minimo = np.min(datos)
            maximo = np.max(datos)

            resultados.append({
                "archivo": archivo,
                "media": media,
                "mediana": mediana,
                "varianza": varianza,
                "minimo": minimo,
                "maximo": maximo
            })

    # Guardar resultados en un CSV comparativo
    resultados_df = pd.DataFrame(resultados)
    resultados_df.to_csv(RESULTADOS_FILE, index=False)
    print(f"\n✅ Análisis completado. Resultados guardados en {RESULTADOS_FILE}")


if __name__ == "__main__":
    analizar()