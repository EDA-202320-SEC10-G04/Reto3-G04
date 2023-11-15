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
from math import radians, sin, cos, sqrt, atan2

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


    
    
    
    analyzer['year'] = m.newMap(1000,
                                maptype='CHAINING',
                                loadfactor=50,
                                )

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
    addYear(analyzer['year'], temblor)
    updateYear(analyzer['years'], temblor)

    updateSig(analyzer['sig'],temblor)
    #updateYear(analyzer['years'],temblor)

    return analyzer

def updateYear(map, temblor):
    time = temblor['time']
    temblortime = datetime.datetime.strptime(time, '%Y-%m-%dT%H:%M:%S.%fZ')
    exist = om.get(map, (temblortime.date()) )
    if exist is None:
        value = om.newMap(omaptype="RBT")
        om.put(map,temblortime.date(), value)
    else:
        value = me.getValue(exist)
    addYear1(map, temblor,value)
    return map


def addYear1(map,temblor, value):
    time = temblor['time']
    temblortime = datetime.datetime.strptime(time, '%Y-%m-%dT%H:%M:%S.%fZ')
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
    om.put(map,(temblortime.date()),value)
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
    entry = om.get(map, temblortime)
    if entry is None:
        datentry = newDataEntry(temblor)
        om.put(map, temblortime, datentry)
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
    lt.addLast(datentry, temblor)
    return datentry

def newDataEntry(temblor):
    entry = lt.newList('SINGLE_LINKED', compareDates)
    return entry



def newlist(temblor):
    newList= lt.newList(datastructure='SINGLE_LINKED')
    return newList




#----------------------------------------------------------------
def addYear(catalog, temblor):
    time = temblor['time'][0:4]
    year = int(time)
    exist= m.contains(catalog, year)
    if exist:
        valor = m.get(catalog, year)
        lista_temblores = me.getValue(valor)
        lt.addLast(lista_temblores, temblor)
    else:
        lista_temblores = lt.newList(datastructure='SINGLE_LINKED')
    m.put(catalog, year, lista_temblores)
    
    return catalog
        







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


def getDatesByRange(analyzer, initialDate, finalDate):
    """
    Retorna el numero de crimenes en un rago de fechas.
    """
    
    
    final = lt.newList('ARRAY_LIST')
    dic = {}
    initialDate = datetime.datetime.strptime(initialDate, '%Y-%m-%dT%H:%M')
    finalDate = datetime.datetime.strptime(finalDate, '%Y-%m-%dT%H:%M') 
    lst = om.values(analyzer, initialDate, finalDate)
    
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



def req_4(sig,gap,analyzer):
    """
    Función que soluciona el requerimiento 6
    """
    # TODO: Realizar el requerimiento 
    final = lt.newList('ARRAY_LIST')
    newLista = lt.newList('ARRAY_LIST')
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
    sa.sort(newLista,compareDates2)
    
    a = lt.subList(newLista,1,17)
    for z in lt.iterator(a):
        time = z['time']
            
            
                
        dic[time] = {
            'time':time,
            'events':1,
            'details':z
                
             }
        lt.addLast(final,dic[time])
    return lt.size(newLista), final




def req_5(year,lat,lon,radio, data_structs):
    a =0
    max ={}
    c = lt.newList('SINGLE_LINKED')
    array = lt.newList('ARRAY_LIST')
    array2 = lt.newList('ARRAY_LIST')
    temblor =m.get(data_structs,year)
    temblores = me.getValue(temblor)
    for j in lt.iterator(temblores):
        distancia = getdistance(lon,lat,j['long'],j['lat'])
        time = j['time']
        time2 = datetime.datetime.strptime(j['time'],'%Y-%m-%dT%H:%M:%S.%fZ')
        j['time'] = time2
        j['distancia'] = round(distancia,3)
        
        if j['distancia'] <radio:
            lt.addLast(array,j)
            if a <float(j['mag']):
                a =float(j['mag'])
                ax = j
    lt.addLast(c,ax)
    f = merg.sort(array,compareDates3)
    return f, c
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
    
    prop_values = lt.newList('ARRAY_LIST')
    
    
    year = me.getValue(m.get(analyzer['year'],int(year)))
    lista = lt.newList('ARRAY_LIST')
    
    prop_values2 = []
    

    # Iterar por las fechas
    for date in lt.iterator(year):
        

       
        if title in date['title']:
            if date[prop] is not None:
              lt.addLast(prop_values, date[prop])
              lt.addLast(lista, date)
    
    sa.sort(prop_values, compare_prop)
    sa.sort(lista, compareDates2)
    for a in lt.iterator(prop_values):
        prop_values2.append(a)

    mayor = lt.firstElement(prop_values)
    menor = lt.lastElement(prop_values)

    # Mostrar el resumen de eventos y rangos
    return lt.size(year), lt.size(lista), mayor, menor, prop_values2, lista
def compare_prop(inf1,inf2):
    if inf1>inf2:
        return True
    else: 
        return False


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
def compareDates2(tem1, tem2):
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

def getdistance(lon1, lat1, lon2, lat2):
    R = 6371.0
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, float(lon2), float(lat2)])
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    distance = R * c
    return distance




def compareDates3(tem1, tem2):
    """
    Compara dos fechas

    """
    date1 = tem1['time']
    date2 = tem2['time']
    if date1 > date2:
        return False
    elif date1 < date2:
        return True
