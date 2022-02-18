from src.checkCancionRandom import checkCancionRandom
from test.diccionarios import libreria
import pytest

# Comprueba que la función devuelva True si está bien
@pytest.mark.checkCancion
def test_correcto1():
    assert checkCancionRandom(libreria, "Seattle_Party") 

# Si el str no se encuentra en el diccionario devuelve False
@pytest.mark.checkCancion
def test_incorrecto1():
    assert checkCancionRandom(libreria, "Hula") == False

# Si a la funcion no le llega un dict devuelve False
@pytest.mark.checkCancion
def test_incorrecto2():
    assert checkCancionRandom(123, "Seattle_Party") == False
    
# Si a la funcion no le llega un str devuelve False
@pytest.mark.checkCancion
def test_incorrecto3():
    assert checkCancionRandom(libreria, 2) == False