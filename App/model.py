"""
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.ADT import stack as st
from DISClib.ADT import queue as qu
from DISClib.ADT import map as m
from DISClib.ADT import minpq as mpq
from DISClib.ADT import indexminpq as impq
from DISClib.ADT import orderedmap as om
from DISClib.DataStructures import heap as heap
from DISClib.DataStructures import mapentry as me
from DISClib.DataStructures import bst as bst
from DISClib.DataStructures import bstnode as bstnode
from DISClib.DataStructures import rbt as rbt
from DISClib.Algorithms.Sorting import shellsort as sa
from DISClib.Algorithms.Sorting import insertionsort as ins
from DISClib.Algorithms.Sorting import selectionsort as se
from DISClib.Algorithms.Sorting import mergesort as merg
from DISClib.Algorithms.Sorting import quicksort as quk
import datetime 
assert cf

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá
dos listas, una para los videos, otra para las categorias de los mismos.
"""

# Construccion de modelos


def newAnalyzer():
    """ Inicializa el analizador

    Crea una lista vacia para guardar todos los crimenes
    Se crean indices (Maps) por los siguientes criterios:
    -Fechas

    Retorna el analizador inicializado.
    """
    analyzer = {'temblores': None,
                'dateIndex': None
                }

    analyzer['temblores'] = lt.newList('ARRAY_LIST', compareIds)
    analyzer['dateIndex'] = om.newMap(omaptype='BST',
                                      cmpfunction=compareDates)

    analyzer['depth'] = om.newMap(omaptype='BST',
                                      cmpfunction=compareDates)
    
    analyzer['year'] = om.newMap(omaptype='BST',cmpfunction=compareDates)
    return analyzer


# Funciones para agregar informacion al catalogo


def addTemblor(analyzer, temblor):
    """
    funcion que agrega un crimen al catalogo
    """
    lt.addLast(analyzer['temblores'], temblor)
    updateDateIndex(analyzer['dateIndex'], temblor)
    updateDepth(analyzer['depth'],temblor)

    return analyzer


def updateDateIndex(map, temblor):
    """
    Se toma la fecha del crimen y se busca si ya existe en el arbol
    dicha fecha.  Si es asi, se adiciona a su lista de crimenes
    y se actualiza el indice de tipos de crimenes.

    Si no se encuentra creado un nodo para esa fecha en el arbol
    se crea y se actualiza el indice de tipos de crimenes
    """
    time = temblor['time']
    temblortime = datetime.datetime.strptime(time, '%Y-%m-%dT%H:%M:%S.%fZ')
    entry = om.get(map, temblortime)
    if entry is None:
        datentry = newDataEntry(temblor)
        om.put(map, temblortime, datentry)
    else:
        datentry = me.getValue(entry)
    addDateIndex(datentry, temblor)
    return map

def updateDepth(map, temblor):
    time = temblor['time']
    temblorTime = datetime.datetime.strptime(time, '%Y-%m-%dT%H:%M:%S.%fZ')
    exist = om.get(map,temblor['depth'] )
    if exist is None:
        entry = newData(temblor)
        om.put(map,temblor['depth'], entry)
    else:
        entry = me.getValue(exist)
    addDepth(entry, temblor)
    return map

def addDepth(entry,temblor):
    
    mainValue ={
    }
    value = lt.newList('ARRAY_LIST')
    lt.addLast(value,temblor)
    mainValue[temblor['time']] = value
    
    heap.insert(entry['lstTemblores'], mainValue)
    return entry

def newData(temblor):
    entry = {'lstTemblores': None}
    entry['lstTemblores'] = heap.newHeap(compare_dicts)
    return entry
def addDateIndex(datentry, temblor):
    lt.addLast(datentry, temblor)
    return datentry

def newDataEntry(temblor):
    entry = lt.newList('SINGLE_LINKED', compareDates)
    return entry



def newlist(temblor):
    newList= lt.newList(datastructure='SINGLE_LINKED')
    return newList






def compare_dicts(dict1, dict2):
    """
    Compara dos diccionarios basándose en la clave 'id'
    """
    if dict1.get('time', "unknown") == dict2.get('time', "unknown"):
        return 0
    elif dict1.get('time', "unknown") > dict2.get('time', "unknown"):
        return 1
    else:
        return -1


def compareIds(id1, id2):
    """
    Compara dos crimenes
    """
    if (id1.key() == id2.key()):
        return 0
    elif id1.key() > id2.key():
        return 1
    else:
        return -1


def compareDates(date1, date2):
    """
    Compara dos fechas
    """
    if (date1 == date2):
        return 0
    elif (date1 > date2):
        return 1
    else:
        return -1


def compareOffenses(offense1, offense2):
    """
    Compara dos tipos de crimenes
    """
    offense = me.getKey(offense2)
    if (offense1 == offense):
        return 0
    elif (offense1 > offense):
        return 1
    else:
        return -1

# Funciones para agregar informacion al modelo

def add_data(data_structs, data):
    """
    Función para agregar nuevos elementos a la lista
    """
    #TODO: Crear la función para agregar elementos a una lista
    pass


# Funciones para creacion de datos

def new_data(id, info):
    """
    Crea una nueva estructura para modelar los datos
    """
    #TODO: Crear la función para estructurar los datos
    pass


# Funciones de consulta

def get_data(data_structs, id):
    """
    Retorna un dato a partir de su ID
    """
    #TODO: Crear la función para obtener un dato de una lista
    pass

def tembloresSize(analyzer):
    """
    Número de crimenes
    """
    return lt.size(analyzer['temblores'])


def indexHeight(analyzer):
    """
    Altura del arbol
    """
    return om.height(analyzer['dateIndex'])


def indexSize(analyzer):
    """
    Numero de elementos en el indice
    """
    return om.size(analyzer['dateIndex'])


def minKey(analyzer):
    """
    Llave mas pequena
    """
    return om.minKey(analyzer['dateIndex'])


def maxKey(analyzer):
    """
    Llave mas grande
    """
    return om.maxKey(analyzer['dateIndex'])


def getDatesByRange(analyzer, initialDate, finalDate):
    """
    Retorna el numero de crimenes en un rago de fechas.
    """
    detalles = lt.newList('ARRAY_LIST')
    final = lt.newList('ARRAY_LIST')
    dic = {}
    initialDate = datetime.datetime.strptime(initialDate, '%Y-%m-%dT%H:%M')
    finalDate = datetime.datetime.strptime(finalDate, '%Y-%m-%dT%H:%M') 
    lst = om.values(analyzer, initialDate, finalDate)
    keys = om.keys(analyzer, initialDate, finalDate)
    totearthquakes = lt.size(lst)
    
    events = 0
    for lstdate in lt.iterator(lst):
        for j in lt.iterator(lstdate):
            
            time = j['time']
            
            
            events += 1
            dic[time] = {
                'time':time,
                'events':1,
                'details':j
                
            }
            lt.addFirst(final,dic[time])
        
    
        
    return totearthquakes, final, events


def req_2(data_structs):
    """
    Función que soluciona el requerimiento 2
    """
    # TODO: Realizar el requerimiento 2
    pass


def req_3(data_structs):
    """
    Función que soluciona el requerimiento 3
    """
    # TODO: Realizar el requerimiento 3
    pass


# Función recursiva para realizar un recorrido in-order en el árbol RBT
def in_order_traversal(node, sig_min, gap_max, result):
    if node is not None:
        in_order_traversal(node['left'], sig_min, gap_max, result)

        event = node['value']['lsttemblores']['first']['info']
        if event['sig']:
         sig = float(event['sig'])
        cmp_sig = float(sig_min) - sig
        if event['gap']:
            cmp_gap = float(gap_max) - float(event['gap'])
        
        if cmp_sig <= 0 and cmp_gap >= 0:
            lt.addLast(result, event)

        in_order_traversal(node['right'], sig_min, gap_max, result)


# Función para consultar los 15 eventos sísmicos más recientes
def consultar_15_eventos_sismicos(sig_min, gap_max, data_structs):
    result = lt.newList()

    in_order_traversal(data_structs['dateIndex']['root'], sig_min, gap_max, result)
    size = lt.size(result)
    

    return size, result




def req_5(data_structs):
    """
    Función que soluciona el requerimiento 5
    """
    # TODO: Realizar el requerimiento 5
    pass


def req_6(data_structs):
    """
    Función que soluciona el requerimiento 6
    """
    # TODO: Realizar el requerimiento 6
    pass


def req_7(data_structs):
    """
    Función que soluciona el requerimiento 7
    """
    # TODO: Realizar el requerimiento 7
    pass


def req_8(data_structs):
    """
    Función que soluciona el requerimiento 8
    """
    # TODO: Realizar el requerimiento 8
    pass


# Funciones utilizadas para comparar elementos dentro de una lista

def compare(data_1, data_2):
    """
    Función encargada de comparar dos datos
    """
    #TODO: Crear función comparadora de la lista
    pass

# Funciones de ordenamiento


def sort_criteria(data_1, data_2):
    """sortCriteria criterio de ordenamiento para las funciones de ordenamiento

    Args:
        data1 (_type_): _description_
        data2 (_type_): _description_

    Returns:
        _type_: _description_
    """
    #TODO: Crear función comparadora para ordenar
    pass


def sort(data_structs):
    """
    Función encargada de ordenar la lista con los datos
    """
    #TODO: Crear función de ordenamiento
    pass
def getFirstNum(number, tablelist):
    if number <= lt.size(tablelist):
        firsts = lt.newList('ARRAY_LIST')
        for element in range(1, number+1):
            d = lt.getElement(tablelist, element)
            lt.addLast(firsts, d)
        return firsts
    else:
        return tablelist
def getLastNum(number, tablelist):
    if number <= lt.size(tablelist):
        last = lt.newList('ARRAY_LIST')
        for element in range(0,number):
            d = lt.getElement(tablelist, lt.size(tablelist)-element)
            lt.addFirst(last, d)
        return last
    else:
        return tablelist

def listFusion(list1, list2):
    listfusion = lt.newList('ARRAY_LIST')
    for element in lt.iterator(list1):
        lt.addLast(listfusion, element)
    for element in lt.iterator(list2):
        lt.addLast(listfusion, element)
    return listfusion

def getnameTeam(tableList,name):
    nameTeam = lt.newList('ARRAY_LIST')
    x =lt.compareElements(tableList, name, element)
    for element in lt.iterator(tableList['home_team']):
        if name == element:
            nameTeam.addLast(element)

from math import radians, sin, cos, sqrt, atan2

def getdistance(lon1, lat1, lon2, lat2):
    R = 6371.0
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance = R * c
    return distance
