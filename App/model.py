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

    analyzer['depth'] = om.newMap(omaptype='BST')
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
    entry = om.get(map, temblortime.date())
    if entry is None:
        datentry = newDataEntry(temblor)
        om.put(map, temblortime.date(), datentry)
    else:
        datentry = me.getValue(entry)
    addDateIndex(datentry, temblor)
    return map

def updateDepth(map, temblor):
    
    exist = om.get(map,float (temblor['depth']) )
    if exist is None:
        value = om.newMap(omaptype="RBT")
        om.put(map,float(temblor['depth']), value)
    else:
        value = me.getValue(exist)
    addDepth(map, temblor,value)
    return map


def addDepth(map,temblor, value):
    
    if len(temblor['nst']) ==0: 
        nst = 0
    else:
        nst = float(temblor['nst'])
        
    exist = om.get(value,nst )
    if exist is None:
        entry = newlist(temblor)
        om.put(value,nst, entry)
    else:
        entry = me.getValue(exist)
    addNst(value, temblor, nst)
    om.put(map,float(temblor['depth']),value)
    return map

def addNst(value, temblor, nst):
    time = temblor['time']
    temblorTime = datetime.datetime.strptime(time, '%Y-%m-%dT%H:%M:%S.%fZ')
    temblor['time'] = temblorTime
    newList = om.get(value, nst)
    valor = me.getValue(newList)
    lt.addLast(valor, temblor)
    om.put(value, nst, valor)
    return value
    


def newlist(temblor):
    newList= lt.newList(datastructure='ARRAY_LIST')
    return newList

def newData(temblor):
    entry = om.newMap(omaptype='RBT') 
    return entry
def addDateIndex(datentry, temblor):
    lt.addLast(datentry['lsttemblores'], temblor)
    return datentry

def newDataEntry(temblor):
    entry = {'lsttemblores': None}
    entry['lsttemblores'] = lt.newList('SINGLE_LINKED', compareDates)
    return entry

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


def req_1(data_structs):
    """
    Función que soluciona el requerimiento 1
    """
    # TODO: Realizar el requerimiento 1
    pass


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


def req_4(data_structs):
    """
    Función que soluciona el requerimiento 4
    """
    # TODO: Realizar el requerimiento 4
    pass


def req_5(data_structs):
    """
    Función que soluciona el requerimiento 5
    """
    # TODO: Realizar el requerimiento 5
    pass


def req_6(depth,nst,analyzer):
    """
    Función que soluciona el requerimiento 6
    """
    # TODO: Realizar el requerimiento 6
    newLista = lt.newList()
    data_structs = analyzer['depth']
    x = om.values(data_structs,depth, om.maxKey(data_structs))
    for i in lt.iterator(x):
        a =i['root']['value']
        b = i['root']
        f = om.values(i,nst,om.maxKey(i))
        for j in lt.iterator(f):
            for z in j['elements']:
                lt.addLast(newLista,z)
    se.sort(newLista,compareDates2)
    f= newLista
    return newLista

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



def compareDates2(tem1, tem2):
    """
    Compara dos fechas

    """
    date1 = tem1['time']
    date2 = tem2['time']
    
    if (date1 == date2):
        return 0
    elif (date1 < date2):
        return 1
    else:
        return -1


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
