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

    def agregar_localidad(self, localidad):
        self.localidades.append(localidad)

    def obtener_localidades_con_coordenadas(self):
        lista_validas = []
        for loc in self.localidades:
            if loc.tiene_coordenadas():
                lista_validas.append(loc)
        return lista_validas

    def contar_con_coordenadas(self):
        return len(self.obtener_localidades_con_coordenadas())

    def contar_sin_coordenadas(self):
        return len(self.localidades) - self.contar_con_coordenadas()

    def porcentaje_con_coordenadas(self):
        if len(self.localidades) == 0:
            return 0.0
        return (self.contar_con_coordenadas() / len(self.localidades)) * 100

    def __len__(self):
        return len(self.localidades)

class DatoMeteorologico:
    
    def __init__(self, temperatura, humedad, viento):
        self.temperatura = temperatura
        self.humedad = humedad
        self.viento = viento

    def __str__(self):
        return f"Temp: {self.temperatura} °C | Humedad: {self.humedad}% | Viento: {self.viento} km/h"

class ClimaActual(DatoMeteorologico):
   
    def __init__(self, nombre_municipio, nombre_localidad, lat, lon, temperatura, humedad, viento, descripcion):
        super().__init__(temperatura, humedad, viento)
        self.nombre_municipio = nombre_municipio
        self.nombre_localidad = nombre_localidad
        self.lat = lat
        self.lon = lon
        self.descripcion = descripcion

class RegistroDiario(DatoMeteorologico):
  
    def __init__(self, fecha, temperatura, humedad, viento, precipitacion):
        super().__init__(temperatura, humedad, viento)
        self.fecha = fecha
        self.precipitacion = precipitacion

    def obtener_anio(self):
        return self.fecha.split("-")[0]

    def obtener_mes(self):
        return self.fecha.split("-")[1]


class ResumenPeriodo:
    def __init__(self, etiqueta):
        self.etiqueta = etiqueta
        self.temperaturas = []
        self.humedades = []
        self.vientos = []
        self.precipitaciones = []

    def agregar_registro(self, registro):

        if registro.temperatura is not None:
            self.temperaturas.append(registro.temperatura)
        if registro.humedad is not None:
            self.humedades.append(registro.humedad)
        if registro.viento is not None:
            self.vientos.append(registro.viento)
        if registro.precipitacion is not None:
            self.precipitaciones.append(registro.precipitacion)

    def promedio_temperatura(self):

        if len(self.temperaturas) == 0:
            return 0.0
        return sum(self.temperaturas) / len(self.temperaturas)

    def promedio_humedad(self):

        if len(self.humedades) == 0:
            return 0.0
        return sum(self.humedades) / len(self.humedades)

    def promedio_viento(self):
        if len(self.vientos) == 0:
            return 0.0
        return sum(self.vientos) / len(self.vientos)

    def precipitacion_total(self):
        return sum(self.precipitaciones)


class ResumenMensual(ResumenPeriodo):
    def __init__(self, anio, mes):
        etiqueta = f"{anio}-{mes}"
        super().__init__(etiqueta)
        self.anio = anio
        self.mes = mes


class ResumenAnual(ResumenPeriodo):
    def __init__(self, anio):
        super().__init__(anio)
        self.anio = anio
