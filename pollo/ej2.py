class StackException(Exception):
    def __init__(self, mensaje="Ocurrió un error personalizado"):
        self.mensaje = mensaje
        super().__init__(self.mensaje)
