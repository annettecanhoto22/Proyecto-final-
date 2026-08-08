class EntidadGeografica:
  
    def __init__(self, nombre: str):
        self.nombre = nombre

class Localidad(EntidadGeografica):

    def __init__(self, nombre, latitud, longitud):
        super().__init__(nombre)
        self.latitud = latitud
        self.longitud = longitud

    def tiene_coordenadas(self):
        if self.latitud is not None and self.longitud is not None:
            return True
        else:
            return False

    def __str__(self):
        if self.tiene_coordenadas():
            return f"{self.nombre} (Lat: {self.latitud}, Lon: {self.longitud})"
        else:
            return f"{self.nombre} (sin coordenadas)"


class Municipio(EntidadGeografica):
   
    def __init__(self, nombre):
        super().__init__(nombre)
        self.localidades = []
