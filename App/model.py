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
    analyzer['years'] = om.newMap(omaptype='BST')

    analyzer['depth'] = om.newMap(omaptype='BST')
    analyzer['sig'] = om.newMap(omaptype='BST')
    return analyzer


# Funciones para agregar informacion al catalogo


def addTemblor(analyzer, temblor):
    """
    funcion que agrega un crimen al catalogo
    """
        
    
    lt.addLast(analyzer['temblores'], temblor)
    updateDateIndex(analyzer['dateIndex'], temblor)
    updateDepth(analyzer['depth'],temblor)
    updateSig(analyzer['sig'],temblor)
    updateYear(analyzer['years'],temblor)
    return analyzer

def updateYear(map, temblor):
    
    exist = om.get(map, (temblor['time'].date()) )
    if exist is None:
        value = om.newMap(omaptype="RBT")
        om.put(map,temblor['time'].date(), value)
    else:
        value = me.getValue(exist)
    addYear(map, temblor,value)
    return map


def addYear(map,temblor, value):
    
    if (temblor['gap']) is None or len(temblor['title'])==0: 
        title = 'Unknown'
    else:
         title = temblor['title']
        
    exist = om.get(value,title )
    if exist is None:
        entry = newlist(temblor)
        om.put(value,title, entry)
    else:
        entry = me.getValue(exist)
    addTitle(value, temblor, title)
    om.put(map,(temblor['time'].date()),value)
    return map

def addTitle(value, temblor, title):

    
    newList = om.get(value, title)
    valor = me.getValue(newList)
    lt.addLast(valor, temblor)
    om.put(value, title, valor)
    return value
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
    temblor['time']= temblorTime
    newList = om.get(value, nst)
    valor = me.getValue(newList)
    lt.addLast(valor, temblor)
    om.put(value, nst, valor)
    return value
    
def updateSig(map, temblor):
    
    exist = om.get(map,float (temblor['sig']) )
    if exist is None:
        value = om.newMap(omaptype="RBT")
        om.put(map,float(temblor['sig']), value)
    else:
        value = me.getValue(exist)
    addSig(map, temblor,value)
    return map


def addSig(map,temblor, value):
    
    if (temblor['gap']) is None or len(temblor['gap'])==0: 
        gap = 0
    else:
        gap = float(temblor['gap'])
        
    exist = om.get(value,gap )
    if exist is None:
        entry = newlist(temblor)
        om.put(value,gap, entry)
    else:
        entry = me.getValue(exist)
    addGap(value, temblor, gap)
    om.put(map,float(temblor['sig']),value)
    return map

def addGap(value, temblor, gap):

    
    newList = om.get(value, gap)
    valor = me.getValue(newList)
    lt.addLast(valor, temblor)
    om.put(value, gap, valor)
    return value
    

def newlist(temblor):
    newList= lt.newList(datastructure='SINGLE_LINKED')
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


def comparePlaces(offense1, offense2):
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


def req_4(sig,gap,analyzer):
    """
    Función que soluciona el requerimiento 6
    """
    # TODO: Realizar el requerimiento 6
    
    final = lt.newList('ARRAY_LIST')
    newLista = lt.newList('ARRAY_LIST')
    hp = heap.newHeap(compare_dicts)
    dic = {}
    data_structs = analyzer['sig']
   
    x = om.values(data_structs,float(sig), float(om.maxKey(data_structs)))
    
    for i in lt.iterator(x):
       
        f = om.values(i,float(om.minKey(i)),float(gap))
        for j in lt.iterator(f):
            for z in lt.iterator(j):
                if len(z['gap'])>0:
                
                 if float(z['gap'])>0: 
                     lt.addFirst(newLista,z)
                
   

    sa.sort(newLista,compareDates3)
    a = lt.subList(newLista,1,17)
    for z in lt.iterator(a):
        time = z['time']
            
            
                
        dic[time] = {
            'time':time,
            'events':1,
            'details':z
                
             }
        lt.addLast(final,dic[time])


                
        

            

    
    
    return final



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
    
    newLista = lt.newList('SINGLE_LINKED')
    data_structs = analyzer['depth']
    x = om.values(data_structs,depth, om.maxKey(data_structs))
    
    for i in lt.iterator(x):
        
        f = om.values(i,nst,om.maxKey(i))
        
        for j in lt.iterator(f):
          
            for z in lt.iterator(j):
                lt.addLast(newLista,z )
            

    merg.sort(newLista,compareDates2)
    
    return newLista


def req_7_histogram(year, title, prop, bins, analyzer):
    total_events = 0
    prop_values = lt.newList('ARRAY_LIST')

    # Rangos
    min_date = f"{year}-01-01"
    max_date = f"{year}-12-31"
    
    
    a = datetime.date.strftime(min_date, '%Y-%m-%d')
    b = datetime.date.strftime(max_date, '%Y-%m-%d')
    print(a)
    
    # Variables para almacenar propiedades y fechas de eventos para el histograma
    prop_list = []
    date_list = []
    

    # Obtener los temblores del año
    year_events = om.keys(analyzer['years'],a,b )

    # Iterar por las fechas
    for date_key in lt.iterator(year_events):
        date_data = me.getValue(m.get(analyzer['years'], date_key))

        # Verificar si la región específica tiene eventos
        if title in date_data:
            region_events = me.getValue(m.get(date_data, title))

            for event in lt.iterator(region_events):
                if prop in event and event[prop] is not None:
                    # Almacenar las propiedades para el histograma
                    prop_list.append(event[prop])

                    # Almacenar las fechas para los eventos con la propiedad especificada
                    date_list.append(event['time'])
                    lt.addLast(prop_values,event)
                    
                    total_events += 1

    # Obtener los valores mínimo y máximo para el histograma
    min_val = min(prop_list)
    max_val = max(prop_list)
    if min_val is None:
        min_val = 0
    if max_val is None:
        max_val = 0


    # Mostrar el resumen de eventos y rangos
    return prop_list, prop_values



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
    
    profundidad1 = tem1['depth']
    profundidad2 = tem2['depth']

    nst1 = tem1['nst']
    nst2 = tem2['nst']


    if date1 < date2:
        return False
    elif date1 > date2:
        return True
    else:        
        if profundidad1 <  profundidad2:
            return False
        elif profundidad1 > profundidad2:
            return True
        else:
            if nst1 <  nst2:
                return False
            elif nst1 > nst2:
                return True
def compareDates3(tem1, tem2):
    """
    Compara dos fechas

    """
    date1 = tem1['time']
    date2 = tem2['time']
    
    sig1 = tem1['sig']
    sig2 = tem2['sig']

    gap1 = tem1['gap']
    gap2 = tem2['gap']


    if date1 < date2:
        return False
    elif date1 > date2:
        return True
    else:        
        if sig1 <  sig2:
            return False
        elif sig1 > sig2:
            return True
        else:
            if gap1 <  gap2:
                return False
            elif gap1 > gap2:
                return True


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
