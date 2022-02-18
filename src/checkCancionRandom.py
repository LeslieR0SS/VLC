def checkCancionRandom(libreria, tituloCancion):
    libreriaCorrecta = isinstance(libreria, dict)
    cancionCorrecta = isinstance(tituloCancion, str)
    if libreriaCorrecta and cancionCorrecta:
        cancionEnLibreria = tituloCancion in libreria.keys()
    return libreriaCorrecta and cancionCorrecta and cancionEnLibreria