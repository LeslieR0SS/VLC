import random

def seleccionaCancionRandom(libreria):
    # Comprobamos que a esta función le llega un diccionario llamado librería
    assert isinstance(libreria, dict)
    # Creamos una lista de las keys y con random.choice obtenemos una al azar
    tituloCancion = random.choice(list(libreria.keys())) 
    # Devolvemos la canción random como str
    return str(tituloCancion) 