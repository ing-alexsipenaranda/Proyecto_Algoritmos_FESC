# utils.py
import time
from functools import wraps


def timed(func):
    """Decorador que mide tiempo de ejecución en segundos.
    Si la función retorna (resultado, comparaciones) el decorador devolverá
    (resultado, comparaciones, elapsed_seconds).
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        t0 = time.perf_counter()
        res = func(*args, **kwargs)
        t1 = time.perf_counter()
        elapsed = t1 - t0
        if isinstance(res, tuple):
            return (*res, elapsed)
        else:
            return res, elapsed

    return wrapper