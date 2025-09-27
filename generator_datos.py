# generator_datos.py

import numpy as np
import os

DEFAULT_SEED = 123


def set_seed(seed=DEFAULT_SEED):
    np.random.seed(seed)


def gen_uniform(n, low=0, high=100000, seed=None):
    if seed is not None:
        np.random.seed(seed)
    return np.random.randint(low, high + 1, size=n)


def gen_gaussian(n, mean=50000, std=15000, seed=None):
    if seed is not None:
        np.random.seed(seed)
    data = np.random.normal(loc=mean, scale=std, size=n)
    data = np.clip(np.round(data).astype(int), 0, None)
    return data


def gen_skewed(n, scale=20000, seed=None):
    # Distribución sesgada: exponencial (cola a la derecha)
    if seed is not None:
        np.random.seed(seed)
    data = np.random.exponential(scale=scale, size=n)
    data = np.round(data).astype(int)
    return data


def save_csv(data, filename):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    np.savetxt(filename, data, delimiter=",", fmt="%d", header="value", comments='')


def generar_datos(output_dir="data", sizes=[100, 1000, 10000], seed=DEFAULT_SEED):
    set_seed(seed)
    os.makedirs(output_dir, exist_ok=True)

    for s in sizes:
        u = gen_uniform(s, seed=seed)
        save_csv(u, f"{output_dir}/uniform_{s}.csv")

        g = gen_gaussian(s, seed=seed)
        save_csv(g, f"{output_dir}/gaussian_{s}.csv")

        sk = gen_skewed(s, seed=seed)
        save_csv(sk, f"{output_dir}/skewed_{s}.csv")

    print(f"✅ Datasets creados en ./{output_dir}/")
if __name__ == "__main__":
    sizes = [100, 1000, 10000]
    set_seed(DEFAULT_SEED)
    for s in sizes:
        u = gen_uniform(s)
        save_csv(u, f"data/uniform_{s}.csv")
        g = gen_gaussian(s)
        save_csv(g, f"data/gaussian_{s}.csv")
        sk = gen_skewed(s)
        save_csv(sk, f"data/skewed_{s}.csv")
    print("Datasets creados en ./data/")