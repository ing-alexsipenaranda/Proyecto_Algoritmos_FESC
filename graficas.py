# graficas.py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

RESULTADOS_FILE = "resultados_analisis.csv"
RESULTADOS_DIR = "graficas"

# Crear carpeta de gráficos si no existe
os.makedirs(RESULTADOS_DIR, exist_ok=True)

def generar_graficas():
    # Leer resultados
    df = pd.read_csv(RESULTADOS_FILE)
    
    # ---- Gráfica de barras: media por archivo ----
    plt.figure(figsize=(10,6))
    sns.barplot(x="archivo", y="media", data=df, palette="viridis")
    plt.xticks(rotation=45, ha="right")
    plt.title("Media por Dataset")
    plt.ylabel("Media")
    plt.xlabel("Archivo")
    plt.tight_layout()
    plt.savefig(os.path.join(RESULTADOS_DIR, "media_por_archivo.png"), dpi=300)
    plt.show()

    # ---- Heatmap de estadísticas ----
    stats_df = df.set_index("archivo")[["media", "mediana", "varianza", "minimo", "maximo"]]
    
    plt.figure(figsize=(10,6))
    sns.heatmap(stats_df, annot=True, fmt=".2f", cmap="YlGnBu")
    plt.title("Heatmap de Estadísticas por Archivo")
    plt.tight_layout()
    plt.savefig(os.path.join(RESULTADOS_DIR, "heatmap_estadisticas.png"), dpi=300)
    plt.show()

    # ---- Gráfica de líneas: media vs varianza ----
    plt.figure(figsize=(8,5))
    plt.plot(df["archivo"], df["media"], marker="o", label="Media")
    plt.plot(df["archivo"], df["varianza"], marker="s", label="Varianza")
    plt.xticks(rotation=45, ha="right")
    plt.title("Media y Varianza por Archivo")
    plt.xlabel("Archivo")
    plt.ylabel("Valor")
    plt.legend()
    plt.tight_layout()
    plt.savefig(os.path.join(RESULTADOS_DIR, "media_varianza_lineas.png"), dpi=300)
    plt.show()
    
    print(f"\n✅ Gráficas generadas en la carpeta '{RESULTADOS_DIR}'")

if __name__ == "__main__":
    generar_graficas()