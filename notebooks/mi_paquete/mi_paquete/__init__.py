def saludar(nombre, mensaje="Este saludo viene de un paquete instalado de verdad."):
    """
    Saluda a una persona con un mensaje opcional.

    Parameters
    ----------
    nombre : str
        Nombre de la persona a saludar.
    mensaje : str, optional
        Mensaje que se agrega al saludo. Por defecto, indica que el
        saludo proviene de un paquete instalado.

    Returns
    -------
    str
        Saludo con el nombre y el mensaje elegido.
    """
    return f"Hola, {nombre}! {mensaje}"
