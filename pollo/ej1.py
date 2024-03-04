from ej2 import StackException

def mi_funcion():
    raise StackException("Este es un mensaje personalizado de error 2")

try:
    mi_funcion()
except StackException as e:
    print(f"Se ha producido una excepción personalizada: {e}")
