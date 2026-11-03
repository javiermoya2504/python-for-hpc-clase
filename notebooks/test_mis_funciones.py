import numpy as np
from mis_funciones import midpoints_array

def test_midpoints_dos_elementos():
    resultado = midpoints_array(np.array([0.0, 10.0]))
    assert np.allclose(resultado, [5.0])

def test_midpoints_tamano_correcto():
    x = np.arange(10.0)
    resultado = midpoints_array(x)
    # con 10 elementos de entrada, deberian salir 9 puntos medios
    assert len(resultado) == 9
