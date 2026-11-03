def midpoints_array(x):
    """Calcula los puntos medios entre elementos consecutivos de x."""
    if len(x) < 2:
        raise ValueError("Se necesitan al menos 2 elementos para calcular puntos medios.")
    return 0.5*(x[:-1] + x[1:])
