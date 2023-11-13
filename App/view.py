﻿"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
from DISClib.ADT import stack as st
from DISClib.ADT import queue as qu
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
assert cf
from tabulate import tabulate
import traceback
from prettytable import PrettyTable, ALL
from matplotlib import pyplot as plt
import model as model

def new_controller():
    """
        Se crea una instancia del controlador
    """
    #TODO: Llamar la función del controlador donde se crean las estructuras de datos
    control ={
        'model': None
    }
    control['model'] = model.newAnalyzer()
    return control

"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""
cont = None

import sys
default_limit = 1000
sys.setrecursionlimit(default_limit*10)
"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""
def printSimpleTable(tableList, keys):
    """
    Función encargada de mostrar los datos en tablas
    """
    table = PrettyTable()
    table.max_width = 20
    table.hrules =ALL
    table.field_names = keys
    lines = []
    for element in lt.iterator(tableList):
        line = []
        for key in keys:
            stringE = str(element[key])
            if len(stringE) > 20:
                stringE = stringE[:20]
            line.append(stringE)
        lines.append(line)
    table.add_rows(lines)
    print(table)



def print_menu():
    print("Bienvenido")
    print("1- Cargar información")
    print("2- Ejecutar Requerimiento 1")
    print("3- Ejecutar Requerimiento 2")
    print("4- Ejecutar Requerimiento 3")
    print("5- Ejecutar Requerimiento 4")
    print("6- Ejecutar Requerimiento 5")
    print("7- Ejecutar Requerimiento 6")
    print("8- Ejecutar Requerimiento 7")
    print("9- Ejecutar Requerimiento 8")
    print("0- Salir")


def load_data(control):
    """
    Carga los datos
    """
    #TODO: Realizar la carga de datos
    pass


def print_data(control, id):
    """
        Función que imprime un dato dado su ID
    """
    #TODO: Realizar la función para imprimir un elemento
    pass

def print_req_1(control):
    """
        Función que imprime la solución del Requerimiento 1 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 1
    pass


def print_req_2(control):
    """
        Función que imprime la solución del Requerimiento 2 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 2
    pass


def print_req_3(control):
    """
        Función que imprime la solución del Requerimiento 3 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 3
    pass




def print_req_5(control,deltatime,size):
    """
        Función que imprime la solución del Requerimiento 5 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 5
    
    print(f"Total de eventos : {size}")

    if size> 0:
        keys = [
                'time',
                'events',
                'details'
                
                    
        ]

        
        detalles = controller.sixdata(detalles)

        # Crear una tabla para los equipos clasificados
        if  size > 6:
            tabla = controller.sixdata(control)
        
            # Crear una tabla 
        temblor_table = PrettyTable()
        temblor_table.field_names = keys
        temblor_table.horizontal_char = '-'
        temblor_table.hrules =ALL

        # Recorrer los earthquakes

        for detail in lt.iterator(tabla):
            detalle_table = PrettyTable()  # Crear una tabla 
            detalle_table.field_names = ['mag','long','lat','depth', 'sig', 'nst', 'title','cdi', 'mmi', 'magType', 'type','code'] 
            
            detalle_table.add_row([detail['mag'], detail['long'], detail['lat'], detail['depth'],
                       detail['sig'], detail['nst'], detail['title'], detail['cdi'],
                       detail['mmi'], detail['magType'], detail['type'], detail['code']])



                       
            temblor_table.add_row([detail['time'],'1',detalle_table])
     
            #
    
        # Imprimir la tabla de equipos clasificados
        print(temblor_table)
    else:
        print("No se encontro temblor especifico.")
    print("El tiempo fue de: ", deltatime)
    
def print_req_6(control):
    """
        Función que imprime la solución del Requerimiento 6 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 6
    pass


def print_req_7(prop_list, bins, prop, title, year):
    plt.hist(prop_list, bins=bins)
    plt.xlabel(f"{prop} Values")
    plt.ylabel("Number of Events")
    plt.title(f"Histogram of {prop} for {title} in {year}")

    # Mostrar el histograma
    plt.show()


def print_req_8(control):
    """
        Función que imprime la solución del Requerimiento 8 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 8
    pass


# Se crea el controlador asociado a la vista
control = new_controller()

# main del reto
if __name__ == "__main__":
    """
    Menu principal
    """
    working = True
    #ciclo del menu
    cont = controller.init()
    while working:
        

        print_menu()
        inputs = input('Seleccione una opción para continuar\n')

        
            

        if int(inputs[0]) == 1:
            sample_option = input("Selecciona el tamaño de muestra (-5pct, -20pct, -30pct, -50pct, -large): ")
            print("\nCargando información de crimenes ....")
            controller.loadData(cont, sample_option)
            print('Crimenes cargados: ' + str(controller.tembloresSize(cont)))
            print('Altura del arbol: ' + str(controller.indexHeight(cont)))
            print('Elementos en el arbol: ' + str(controller.indexSize(cont)))
            print('Menor Llave: ' + str(controller.minKey(cont)))
            print('Mayor Llave: ' + str(controller.maxKey(cont)))
                                    #--------------------MATCH RESULTS ----------------------
            print("-------------------- TEMBLORES --------------------")
            sixTemblores =controller.Tendata(cont['temblores'])
            printSimpleTable(sixTemblores, ["code","time","lat","long","mag","title","depth","felt","cdi","mmi","tsunami"])
        
        elif int(inputs) == 2:
            print_req_1(control)

        elif int(inputs) == 3:
            print_req_2(control)

        elif int(inputs) == 4:
            print_req_3(control)

        elif int(inputs) == 5:
            print("========================== Req No. 4 Inputs ===============")
            
            sig = input("Ingrese la significancia mínima (sig): ")
            gap = input("Ingrese la distancia azimutal máxima del evento (gap): ") 
              
            print("========================= Req No.4 Results ==================")
            result, time= controller.req_4(sig, gap,cont)
           
            print("Para calcular los n goles por jugador, delta tiempo fue:", str(time))
            print_req_4 (result)

        elif int(inputs) == 6:
            z = cont
            depth = float(input("Ingrese la profundidad minima del evento: "))
            nst = int(input("Ingrese el numero minimo de estaciones que detectan el  evento: "))
            
            answer,deltatime,size = controller.req_6(depth,nst, cont)
            print_req_5(answer,deltatime,size)

        elif int(inputs) == 7:
            pass

        elif int(inputs) == 8:
            print("========================== Req No. 4 Inputs ===============")
            
            year= input("Ingrese el año de interés: ")
            title = input("Ingrese el area de interés: ") 
            prop =  input("Ingrese la propiedad de interés: ") 
            bins = input('Ingrese el número de segmentos del histograma: ')
            
              
            print("========================= Req No.4 Results ==================")
            prop_list, prop_values, time= controller.req_7(year, title, prop, bins, cont)
           
            print("Para calcular los n goles por jugador, delta tiempo fue:", str(time))
            print_req_7(prop_list, bins, prop, title, year)

        elif int(inputs) == 9:
            print_req_8(control)

        elif int(inputs) == 0:
            working = False
            print("\nGracias por utilizar el programa")
        else:
            print("Opción errónea, vuelva a elegir.\n")
    sys.exit(0)
