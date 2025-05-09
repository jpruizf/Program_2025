from clase_gastos import Gasto
import csv
class Gestor_Gastos:
    __listado_gastos:list

    def __init__(self):
        self.__listado_gastos = []

    def Agregar_gasto(self,Un_gasto):
        self.__listado_gastos.append(Un_gasto)
    
    def Cargar_gastos(self):
        bandera = False
        with open('gastosAbril2025.csv') as archivo_gastos:
            lector = csv.reader(archivo_gastos,delimiter=';')
            for fila in lector:
                if not bandera:
                    bandera = True
                else:
                    patente = fila[0]
                    fecha = fila[1]
                    importe = float(fila[2])
                    descrip = fila[3]
                    Un_gasto = Gasto(patente,fecha,importe,descrip)
                    self.Agregar_gasto(Un_gasto)
        archivo_gastos.close()
    '''inciso a'''
    def buscar_patente(self,elemento):
        bandera = False
        encontrado = None
        indice = 0
        while not bandera and indice < len(self.__listado_gastos):
            if elemento == self.__listado_gastos[indice].get_patentex():
                bandera = True
                encontrado = self.__listado_gastos[indice].get_patentex()
            else:
                print("patente no encontrada")
                indice += 1
        return encontrado
    def listadar_gastos(self,elemento):
        for i, x in enumerate(self.__listado_gastos):
            if elemento == i.get_patentex():
                print(x)
    '''inciso b'''
    def mostrar_fecha(self,aux):
        for indice,dato in enumerate(self.__listado_gastos):
            if aux == indice.get_fecha():
                print(f"Importe->{dato.get_importe()}/Total importe->{dato.get_total_importe()}")
    
    '''inciso c'''
    def ordenar_listado(self):
        self.__listado_gastos.sort()
    
    def buscar_gasto(self, valor):
        bandera = False
        encontrado = None
        indice = 0
        while not bandera and indice < len(self.__listado_gastos):
            if valor == self.__listado_gastos[indice].get_fecha():
                bandera = True
                encontrado = self.__listado_gastos[indice].get_patentex()
            else:
                indice += 1
        return encontrado