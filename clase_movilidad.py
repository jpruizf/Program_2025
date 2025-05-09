class Movilidad:
    __patente:str
    __tipo_vehiculo:str
    __capacidad_carga:int
    __importe_patente:float
    __marca:str
    __modelo:str
    def __init__(self,patente,tipo,capacidad,importe,marca,modelo):
        self.__patente = patente
        self.__tipo_vehiculo = tipo
        self.__capacidad_carga = capacidad
        self.__importe_patente = importe
        self.__marca = marca
        self.__modelo = modelo
    def get_patente(self):
        return self.__patente
    def get_tipo_vehiculo(self):
        return self.__tipo_vehiculo
    def get_capacidad_carga(self):
        return self.__capacidad_carga
    def get_importe(self):
        return self.__importe_patente
    def get_marca(self):
        return self.__marca
    def get_modelo(self):
        return self.__modelo
    def __lt__(self,otro):
        return (self.__patente < otro.get_patente())
    def __str__(self):
        return f"Patente->{self.get_patente()}/Tipo de vehiculo->{self.get_tipo_vehiculo()}/\nCapacidad de carga->{self.get_capacidad_carga()}/\nImporte de patente->{self.get_importe()}/Marca->{self.get_marca()}/Modelo->{self.get_modelo()}"