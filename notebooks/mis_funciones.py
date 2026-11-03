def midpoints_array(x):
    """
    Calcula los puntos medios entre elementos consecutivos de un arreglo.

    Parameters
    ----------
    x : numpy.ndarray, shape (n,)
        Arreglo unidimensional de valores numericos ordenados como se
        desean emparejar. No es necesario que esten en orden creciente.

    Returns
    -------
    numpy.ndarray, shape (max(n - 1, 0),)
        Promedio de cada par consecutivo: resultado[i] es
        0.5 * (x[i] + x[i + 1]). Si x tiene cero o un elemento,
        devuelve un arreglo vacio.
    """
    return 0.5 * (x[:-1] + x[1:])
