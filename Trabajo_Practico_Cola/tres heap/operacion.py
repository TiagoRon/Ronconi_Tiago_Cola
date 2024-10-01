class Operacion:
    def __init__(self, encargado, descripcion, hora, stormtroopers=0):
        self.encargado = encargado
        self.descripcion = descripcion
        self.hora = hora
        self.stormtroopers = stormtroopers

    def __str__(self):
        return (f"Encargado: {self.encargado}, Descripcion: {self.descripcion}, "
                f"Hora: {self.hora}, Stormtroopers: {self.stormtroopers}")

    def __repr__(self):
        return self.__str__()
