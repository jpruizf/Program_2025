from clase_movilidad import Movilidad
import csv
import numpy as np

class Gestor_Movilidades:
    __cantidad:int
    __dimension:int
    __incremento = 5
    __listado_movilidades:np.ndarray

    def __init__(self,dimension):
        self.__dimension = dimension
        self.__cantidad = 0
        self.__listado_movilidades = np.empty(5,Movilidad)
    
    def Agregar_Una_movilidad(self,Una_Movilidad):
        if self.__dimension == self.__cantidad:
            self.__dimension += self.__incremento
            self.__listado_movilidades.resize(self.__dimension)
        self.__listado_movilidades[self.__cantidad] = Una_Movilidad
        self.__cantidad += 1
    
    def cargar_movilidades(self):
        bandera = False
        with open('movilidades.csv') as archivo_molidades:
            lector = csv.reader(archivo_molidades,delimiter=';')
            for fila in lector:
                if not bandera:
                    bandera = False
                else:
                    patente = fila[0]
                    tipo = fila[1]
                    capacidad = int(fila[2])
                    importe = float(fila[3])
                    marca = fila[4]
                    modelo = fila[5]
                    Una_movilidad = Movilidad(patente,capacidad,importe,marca,modelo)
                    self.Agregar_Una_movilidad(Una_movilidad)
    '''inciso a'''
    def mostrar_listado(self,elemento):
        for i, y in enumerate(self.__listado_movilidades):
            if elemento == i.get_patente():
                print(y)
    '''inciso c'''
    def ordenar_listado(self):
        self.__listado_movilidades.sort()
    
    def mostrar_movilidad(self, aux_patente):
        for indice, datos in enumerate(self.__listado_movilidades):
            if aux_patente == indice.get_patente():
                print(datos)
