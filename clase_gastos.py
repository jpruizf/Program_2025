class Gasto:
    __aux_patente:str
    __fecha:str
    __importe:float
    __descripcion:str
    __total:float
    def __init__(self,aux_p,fecha,importe,descripcion):
        self.__aux_patente = aux_p
        self.__fecha = fecha
        self.__importe = importe
        self.__descripcion = descripcion
        self.__total = 0.0

    
    def get_patentex(self):
        return self.__aux_patente
    
    def get_fecha(self):
        return self.__fecha
    
    def get_importe(self):
        return self.__importe
    
    def get_descripcion(self):
        return self.__descripcion
    def __add__(self,otro):
        self.__total = self.__importe + otro.get_importe()
        return self.__total
    def get_total_importe(self):
        return self.__total
    def __lt__(self,otro):
        return self.__fecha < otro.get_fecha()
    def __str__(self):
        return f"Patente->{self.get_patentex()}/\nFecha->{self.get_fecha}/Importe->{self.get_importe()}/Importe Total->{self.__total}/Descripcion->{self.get_descripcion()}"