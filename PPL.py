from Manejador_movilidad import Gestor_Movilidades
from Manejador_gastos import Gestor_Gastos

def menu():
    print("1->inicio    |   0->Teminar")
    inicio = input("Seleccione una opcion ->")
    while inicio != '0':
        G_Movil = Gestor_Movilidades(5)
        G_G = Gestor_Gastos()
        print("a->Ver los datos de movilidades y total de gastos para una fecha")
        print("b->Ver el total de gastos y gasto para una fecha")
        print("c->Ver datos de cada movilidad y total a pagar para una fecha")
        opcion = input("Seleccione una opcion->")
        if opcion == 'a':
            patente = None
            G_Movil.cargar_movilidades()
            G_Movil.ordenar_listado()
            G_G.Cargar_gastos()
            G_G.ordenar_listado()
            aux = input("Fecha->")
            patente = G_G.buscar_patente(aux)
            G_G.listadar_gastos(patente)
            G_Movil.mostrar_listado(patente)
        elif opcion == 'b':
            aux1 = input("Ingrese una fecha->")
            G_G.mostrar_fecha(aux1)
        elif opcion =='c':
            patente = None
            aux = input("Fecha->")
            patente = G_G.buscar_gasto(aux)
            G_Movil.mostrar_movilidad(patente)
        print("1->inicio    |   0->Teminar")
        inicio = input("Seleccione una opcion ->")


if __name__ == '__main__':
    menu()