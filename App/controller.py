﻿"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
import model
import time
import csv
import tracemalloc

"""
El controlador se encarga de mediar entre la vista y el modelo.
"""


def init():
    """
    Llama la funcion de inicializacion  del modelo.
    """
    # catalog es utilizado para interactuar con el modelo
    analyzer = model.newAnalyzer()
    return analyzer


# ___________________________________________________
#  Funciones para la carga de datos y almacenamiento
#  de datos en los modelos
# ___________________________________________________

def loadData(analyzer, sampleoption):
    """
    Carga los datos de los archivos CSV en el modelo
    """
    temblorfile = cf.data_dir + f'earthquakes/temblores-utf8{sampleoption}.csv'
    input_file = csv.DictReader(open(temblorfile, encoding="utf-8"),
                                delimiter=",")
    for crime in input_file:
        model.addTemblor(analyzer, crime)
        
    return analyzer



# Funciones de ordenamiento

def sort(control):
    """
    Ordena los datos del modelo
    """
    #TODO: Llamar la función del modelo para ordenar los datos
    pass


# Funciones de consulta sobre el catálogo

def tembloresSize(analyzer):
    """
    Numero de crimenes leidos
    """
    return model.tembloresSize(analyzer)


def indexHeight(analyzer):
    """
    Altura del indice (arbol)
    """
    return model.indexHeight(analyzer)


def indexSize(analyzer):
    """
    Numero de nodos en el arbol
    """
    return model.indexSize(analyzer)


def minKey(analyzer):
    """
    La menor llave del arbol
    """
    return model.minKey(analyzer)


def maxKey(analyzer):
    """
    La mayor llave del arbol
    """
    return model.maxKey(analyzer)
def getDatesByRange(analyzer, ini, fin):
    "Retorna los goles totales de un jugador, y los últimos n goles"
    
    start_time = get_time()
    totearthquakes, detalles, events = model.getDatesByRange(analyzer, ini, fin)
    end_time = get_time()
    
    deltatime = delta_time(start_time, end_time)
    return deltatime,  totearthquakes, detalles, events

def req_2(analyzer, ini, fin):
    
    start_time = get_time()
    totearthquakes, detalles, events = model.req_2(analyzer, ini, fin)
    end_time = get_time()
    
    deltatime = delta_time(start_time, end_time)
    return deltatime,  totearthquakes, detalles, events



def req_3(mag_min, depth_max,analyzer):
    
    start_time = get_time()
   
    result = model.req_3(mag_min, depth_max, analyzer)

    end_time = get_time()
    deltatime = delta_time(end_time, start_time)
    return result, deltatime


def req_4(sig,gap,analyzer):
    start_time = get_time()
    size, answer = model.req_4(sig,gap,analyzer)
    end_time = get_time()
    
    deltatime = delta_time(start_time, end_time)
    
    return size, answer, deltatime

def req_5(n,year,lat,lon,radio, data_structs):
    """
    Retorna el resultado del requerimiento 6
    """
    # TODO: Modificar el requerimiento 6
    start_time = get_time()
    answer, ax = model.req_5(n,year,lat,lon,radio, data_structs)
    end_time = get_time()
    deltatime = delta_time(end_time, start_time)
    return answer,deltatime ,ax

def req_6(depth,nst, analyzer):
    """
    Retorna el resultado del requerimiento 6
    """
    # TODO: Modificar el requerimiento 6
    start_time = get_time()
    answer = model.req_6(depth,nst, analyzer)
    end_time = get_time()
    size = model.lt.size(answer)
    deltatime = delta_time(start_time, end_time)
    return answer,deltatime,size





def req_7(year, title, prop, bins, analyzer):
    start_time = get_time()
    eventos_periodo, eventos_hist, mayor, menor, prop_values, lista = model.req_7_histogram(year, title, prop, bins, analyzer)
    end_time = get_time()
    
    deltatime = delta_time(start_time, end_time)
    
    return eventos_periodo, eventos_hist, mayor, menor, prop_values, lista, deltatime


def req_8(control):
    """
    Retorna el resultado del requerimiento 8
    """
    # TODO: Modificar el requerimiento 8
    pass


# Funciones para medir tiempos de ejecucion

def get_time():
    """
    devuelve el instante tiempo de procesamiento en milisegundos
    """
    return float(time.perf_counter()*1000)


def delta_time(start, end):
    """
    devuelve la diferencia entre tiempos de procesamiento muestreados
    """
    elapsed = float(end - start)
    return elapsed

def get_memory():
    """
    toma una muestra de la memoria alocada en instante de tiempo
    """
    return tracemalloc.take_snapshot()


def delta_memory(stop_memory, start_memory):
    """
    calcula la diferencia en memoria alocada del programa entre dos
    instantes de tiempo y devuelve el resultado en bytes (ej.: 2100.0 B)
    """
    memory_diff = stop_memory.compare_to(start_memory, "filename")
    delta_memory = 0.0

    # suma de las diferencias en uso de memoria
    for stat in memory_diff:
        delta_memory = delta_memory + stat.size_diff
    # de Byte -> kByte
    delta_memory = delta_memory/1024.0
    return delta_memory
def sixdata(tableList):
    if model.lt.size(tableList) <6:
        return tableList
    else:
        firsts = getFirstNum(3, tableList)
        lasts = getLastNum(3, tableList)
        return model.listFusion(firsts, lasts)
def othersixdata(tableList):
    if model.lt.size(tableList) <6:
        return tableList
    else:
        firsts = getFirstNum(6, tableList)
        lasts = getLastNum(0, tableList)
        return model.listFusion(firsts, lasts)
def Tendata(tableList):
    if model.lt.size(tableList) <=6:
        return tableList
    else:
        firsts = getFirstNum(5, tableList)
        lasts = getLastNum(5, tableList)
        return model.listFusion(firsts, lasts)
def getFirstNum(number, tableList):
    return model.getFirstNum(number,tableList)

def getLastNum(number,tableList):
    return model.getLastNum(number,tableList)

def FindTeam(tableList, name):
    team = model.getnameTeam(tableList,name)
    
    return team
    

def sixdata(tableList):
    if model.lt.size(tableList) <=6:
        return tableList
    else:
        firsts = getFirstNum(3, tableList)
        lasts = getLastNum(3, tableList)
        return model.listFusion(firsts, lasts)
def getFirstNum(number, tableList):
    return model.getFirstNum(number,tableList)

def getLastNum(number,tableList):
    return model.getLastNum(number,tableList)

def FindTeam(tableList, name):
    team = model.getnameTeam(tableList,name)
    
    return team
