"""
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
all_keys = ['mag','place','time','updated','tz','felt','cdi','mmi','alert','status','tsunami','sig','net','code','ids','sources','types','nst','dmin','rms','gap','magType','type','title','long','lat','depth']

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

def print_temblores_fecha( totearthquakes, detalles, events):
    print("Clasificación de los mejores anotadores:")
    print(f"Total de fechas: {totearthquakes}")
    print(f"Total de eventos: {events}")

    if events> 0:
        keys = [
                'time',
                'events',
                'details'
                
                    
        ]

        if  events > 6:
            detalles = controller.sixdata(detalles)

        # Crear una tabla para los equipos clasificados
        temblor_table = PrettyTable()
        temblor_table.field_names = keys
        temblor_table.horizontal_char = '-'
        temblor_table.hrules =ALL
        temblor_table.field_names = keys
        # Recorrer los equipos clasificados y agregarlos a la tabla

        for detail in lt.iterator(detalles):
            detalle= detail['details']  
            detalle_table = PrettyTable()  # Crear una tabla para el máximo goleador
            detalle_keys = ['mag','long','lat','depth', 'sig', 'nst', 'title','cdi', 'mmi', 'magType', 'type','code'] 
                       
            
            # Agregar los datos del máximo goleador a la tabla del máximo goleador
            detalle_table.field_names =  detalle_keys
            detalle_table.add_row([detalle.get(key, '') for key in detalle_keys])
            
            # Agregar una fila en la tabla de equipos con la tabla del máximo goleador
            temblor_data = [detail[key] if key != 'details' else str(detalle_table) for key in keys]
            temblor_table.add_row(temblor_data)
    
        # Imprimir la tabla de equipos clasificados
        print(temblor_table)
    else:
        print("No se encontraron goles para el jugador especificado.")


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



def print_req_4 (size, detalles):
    print(f'El total de eventos con una distancia azimutal  máxima y una significancia mínima son: {size}')
    if len(detalles)> 0:
        keys = [
                'time',
                'events',
                'details'
                
                    
        ]

        
        detalles = controller.sixdata(detalles)

        # Crear una tabla para los equipos clasificados
        
            
        
            # Crear una tabla 
        temblor_table = PrettyTable()
        temblor_table.field_names = keys
        temblor_table.horizontal_char = '-'
        temblor_table.hrules =ALL
     # Crear una tabla para los equipos clasificados

        # Recorrer los equipos clasificados y agregarlos a la tabla

        for equipo in lt.iterator(detalles):
            details_data = equipo['details']  
            details_table = PrettyTable()  # Crear una tabla para el máximo goleador    
            details_keys = ['mag','long','lat','depth', 'sig', 'gap', 'nst', 'title','cdi', 'mmi', 'magType', 'type','code'] 
            
            # Agregar los datos del máximo goleador a la tabla del máximo goleador
            details_table.field_names = details_keys
            details_table.add_row([details_data.get(key, '') for key in details_keys])
            
            # Agregar una fila en la tabla de equipos con la tabla del máximo goleador
            temblor_data = [equipo[key] if key != 'details' else str(details_table) for key in keys]
            temblor_table.add_row(temblor_data)
            
        # Imprimir la tabla de equipos clasificados
        print(temblor_table)
    else:
        print("No se encontraron goles para el jugador especificado.")
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
def print_req_6(control,deltatime,size, n,max):
    """
        Función que imprime la solución del Requerimiento 6 en consola
    """
    """
        Función que imprime la solución del Requerimiento 6 en consola
    """
    # TODO: Imprimir el resultado del requerimiento 6
    print(f"Total de eventos : {size}")

    if size> 0:
        keys = [
                'time',
                'events',
                'details'
                

        ]
        if  size > 6:
            tabla = controller.sixdata(control)
        temblor_table = PrettyTable()
        temblor_table.field_names = keys
        temblor_table.horizontal_char = '-'
        temblor_table.hrules =ALL
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

def print_req_7(eventos_periodo, eventos_hist,mayor, menor, prop_values, lista, bins, prop):
    print(f'Total de eventos en la fecha: {eventos_periodo}')
    print(f'Total de eventos en el histograma {eventos_hist}')
    print(f'Propiedad menor del histograma {menor}')
    print(f'Propiedad mayor del histograma {mayor}')
    
    plt.hist(prop_values, bins=int(bins), edgecolor='black', rwidth=0.8)

    plt.xlabel(f"{prop} Values")
    plt.ylabel("Number of Events")
    plt.title(f"Histogram of {prop}")
    plt.show()
    if float(eventos_hist) > 0:
        keys = ['time', 'lat', 'long', 'title', 'code', prop]

        if float(eventos_hist) > 6:
            # Aquí puedes implementar una función para mostrar solo los primeros 6 goles
            lista = controller.sixdata(lista)

        # Imprimir la tabla de goles
        printSimpleTable(lista, keys)
    else:
        print("No se encontraron goles para el jugador especificado.")



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
            
            start_time = controller.get_time()
            printSimpleTable(sixTemblores, ["code","time","lat","long","mag","title","depth","felt","cdi","mmi","tsunami"])
            end_time = controller.get_time()
            deltatime = controller.delta_time(start_time, end_time)
            print("el tiempo fue :", deltatime)
                    
        elif int(inputs) == 2:
                print("========================== Req No. 1 Inputs ===============")
                ini  = input("Ingrese la fecha inicial: ")
                fin  = input("Ingrese la fecha final: ")
                
                print("========================= Req No.1 Results ==================")
                f = cont
                time, totearthquakes, detalles, events = controller.getDatesByRange(cont['dateIndex'], ini, fin)
                
                print(" delta tiempo fue:", str(time))
                print_temblores_fecha( totearthquakes, detalles, events)
        elif int(inputs) == 3:
            print_req_2(control)

        elif int(inputs) == 4:
            print_req_3(control)

        elif int(inputs) == 5:
            print("========================== Req No. 4 Inputs ===============")
            
            sig = input("Ingrese la significancia mínima (sig): ")
            gap = input("Ingrese la distancia azimutal máxima del evento (gap): ") 
              
            print("========================= Req No.4 Results ==================")
            size, result, time= controller.req_4(sig, gap,cont)
           
            print("Para calcular los n goles por jugador, delta tiempo fue:", str(time))
            print_req_4 (size, result)

        elif int(inputs) == 6:
            z = cont
            depth = float(input("Ingrese la profundidad minima del evento: "))
            nst = int(input("Ingrese el numero minimo de estaciones que detectan el  evento: "))
            
            answer,deltatime,size = controller.req_6(depth,nst, cont)
            print_req_5(answer,deltatime,size)

        elif int(inputs) == 7:
            year = int(input("Ingrese el año relevante: "))
            lat = float(input("Ingrese la Latitud de referencia para el área de eventos: "))
            lon = float(input("Ingrese la longitud de referencia para el área de eventos "))
            radio = float((input("Ingrese el radio [km] del área circundante ")))
            n = int(input("Ingrese el número de los N eventos de magnitud más cercana a mostrar.: "))
            
            
            answer,deltatime, max = controller.req_5(year,lat,lon,radio, cont['year'] )
            size = lt.size(answer)
            print_req_6(answer,deltatime,size, n,max)

        elif int(inputs) == 8:
            print("========================== Req No. 7 Inputs ===============")
            
            year= input("Ingrese el año de interés: ")
            title = input("Ingrese el area de interés: ") 
            prop =  input("Ingrese la propiedad de interés: ") 
            bins = input('Ingrese el número de segmentos del histograma: ')
            
              
            print("========================= Req No.7 Results ==================")
            eventos_periodo, eventos_hist, mayor, menor, prop_values, lista, deltatime= controller.req_7(year, title, prop, bins, cont)
           
            print("Para calcular los n goles por jugador, delta tiempo fue:", str(deltatime))
            print_req_7(eventos_periodo, eventos_hist, mayor, menor, prop_values, lista, bins, prop)

        elif int(inputs) == 9:
            print_req_8(control)

        elif int(inputs) == 0:
            working = False
            print("\nGracias por utilizar el programa")
        else:
            print("Opción errónea, vuelva a elegir.\n")
    sys.exit(0)
