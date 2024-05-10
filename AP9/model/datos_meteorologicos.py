class DatosMeteorologicos:
    puntos_cardinales={
        "N": 0,
        "NNE": 22.5,
        "NE": 45,
        "ENE": 67.5,
        "E": 90,
        "ESE": 112.5,
        "SE": 135,
        "SSE": 157.5,
        "S": 180,
        "SSW": 202.5,
        "SW": 225,
        "WSW": 247.5,
        "W": 270,
        "WNW": 292.5,
        "NW": 315,
        "NNW": 337.5,
    }
    def __init__(self, nombre_archivo: str):
        self.nombre_archivo: str = nombre_archivo


    def procesar_datos(self)-> tuple[float, float, float, float, str]:
        sumas = {
            "Temperatura":0,
            "Humedad":0,
            "Presion":0,
            "Velocidad":0,
            "Direccion":0,
        }
        cont=1
        with open(self.nombre_archivo, "r") as archivo:
            for linea in archivo:
                if linea == "\n":
                    cont+=1
                    continue
                parametro = linea.split(":")[0]
                valor = linea.split(":")[1].strip()
                if parametro == "Estacion" or parametro=="Latitud"\
                    or parametro == "Longitud" or parametro=="Fecha"\
                        or parametro == "Hora":
                    continue

                if parametro =="Viento":
                    velocidad = float(valor.split(",")[0])
                    direccion= valor.split(",")[1]
                    sumas["Velocidad"] += velocidad
                    sumas["Direccion"] += DatosMeteorologicos.puntos_cardinales[direccion] 
                else:
                    sumas[parametro]+=float(valor)
        promedio_temperatura = sumas["Temperatura"]/ cont
        promedio_humedad= sumas["Humedad"]/ cont
        promedio_presion= sumas["Presion"]/ cont
        promedio_velocidad= sumas["Velocidad"]/ cont
        promedio_direccion= sumas["Direccion"]/ cont
        punto_cardinal_premodinante = self.convertir_grado_a_punto_cardinal(promedio_direccion)

        return (promedio_temperatura, promedio_humedad, promedio_presion, promedio_velocidad,punto_cardinal_premodinante )


    def convertir_grado_a_punto_cardinal(self, grado:float)->str:
        menor_diferencia = 337.5
        punto_cardinal_mas_cercano= "NNW" 
        for punto_cardinal in DatosMeteorologicos.puntos_cardinales.keys():
            diferencia = abs(grado-DatosMeteorologicos.puntos_cardinales[punto_cardinal])
            if diferencia==0:
                return punto_cardinal

            if diferencia< menor_diferencia:
                menor_diferencia = diferencia
                punto_cardinal_mas_cercano = punto_cardinal 

        return punto_cardinal_mas_cercano
