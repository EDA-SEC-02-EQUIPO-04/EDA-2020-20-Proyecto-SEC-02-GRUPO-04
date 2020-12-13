"""
 * Copyright 2020, Departamento de sistemas y Computación
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
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 * Contribución de:
 *
 * Dario Correal
 *
 """
import config
from DISClib.ADT.graph import gr
from DISClib.ADT import map as m
from DISClib.DataStructures import mapentry as me
from DISClib.ADT import list as lt
from DISClib.ADT import orderedmap as om
from DISClib.DataStructures import listiterator as it
from DISClib.Algorithms.Graphs import scc
from DISClib.Algorithms.Graphs import dijsktra as djk
from DISClib.Utils import error as error
from DISClib.ADT import minpq as min
import datetime
assert config

"""
En este archivo definimos los TADs que vamos a usar y las operaciones
de creacion y consulta sobre las estructuras de datos.
"""

# -----------------------------------------------------
#                       API
# -----------------------------------------------------

def new_catalog():
    catalog = {'date_index': om.newMap(omaptype='RBT', comparefunction= compare_dates),
                'taxis_filter': m.newMap(60, maptype='CHAINING', comparefunction= compare_ids),
                'taxis_with_filter': lt.newList('SINGLE_LINKED', compare_ids)
               }
    return catalog 

def newTaxiEntry(taxi):
    taxis = {'serviceIndex': m.newMap(numelements=60,
                                      maptype='PROBING',
                                      comparefunction=compare_ids),
             'lsttaxis': lt.newList('SINGLE_LINKED', compare_dates)
            } 

    return taxis

def newServiceEntry(taxi):
    entry = {'taxi': taxi,
             'lsttaxis': lt.newList('SINGLE_LINKED', compare_ids)
            }
    return entry

def new_taxi(taxi):
    taxis = {'taxi': taxi,
             'services': 0,
             'money': 0,
             'miles': 0,
             'points': 0
           }
    return taxis

# ==============================
# Funciones de consulta
# ==============================

def alpha_fuction(miles, money, services):
    """Calculo función alfa de puntos

    Args:
        miles ([int]): Millas recorridas
        money ([int]): Total dinero recibido 
        services ([int]): Servicios prestados 
    """
    if money == float(0):
        None
    else:
        alpha = (miles/money)*services
        return alpha

def addTaxi(catalog, taxi):
    updateDateIndex(catalog['date_index'], taxi)
    return catalog


def addDateIndex(datentry, information):
    """
    Agrega la información de cada taxi
    """
    lst = datentry['lsttaxis']
    lt.addLast(lst, information)
    serviceIndex = datentry['serviceIndex']
    taxi_id = information['taxi_id']
    servicentry = m.get(serviceIndex, taxi_id)
    
    if servicentry is None:
        entry = newServiceEntry(taxi_id)
        lt.addLast(entry['lsttaxis'], information)
        m.put(serviceIndex, taxi_id, entry)
    else:
        entry = me.getValue(servicentry)
        lt.addLast(entry['lsttaxis'], information)
    return datentry


def updateDateIndex(map, taxi):
    """
    Se toma la fecha en la que se inició el viaje del taxi y se busca si ya 
    existe en el arbol dicha fecha. Si es así, se adiciona a su lista los taxis 
    y se actualiza el indice de taxis. 

    Si no se encuentra, se crea un nodo para esa fecha en el arbol y se actualiza 
    el indice de taxis    
    """
    occurreddate = taxi['trip_start_timestamp'][0:10]
    taxi_date_start = datetime.datetime.strptime(occurreddate, '%Y-%m-%d')
    entry = om.get(map, taxi_date_start.date())
    if entry is None:
        datentry = newTaxiEntry(taxi)
        om.put(map, taxi_date_start.date(), datentry)
    else:
        datentry = me.getValue(entry)
    addDateIndex(datentry, taxi) 
    return map

def TaxisbyRange(catalog, initialDate, finalDate): #Taxis de acuerdo a la fecha seleccionada
    lst = om.values(catalog['date_index'], initialDate, finalDate)
    listiterator = it.newIterator(lst)
    while it.hasNext(listiterator):
        lstdate = it.next(listiterator)['lsttaxis']
        iterator_2 = it.newIterator(lstdate)
        while it.hasNext(iterator_2):
            taxis_id = it.next(iterator_2)['taxi_id']
            money = it.next(iterator_2)['trip_total']
            miles = it.next(iterator_2)['trip_miles']
            if money != "" and miles != "" and taxis_id != "" and taxis_id != 'NA':
                existtaxi = m.contains(catalog['taxis_filter'], taxis_id)
                taxis = catalog['taxis_filter']
                if existtaxi:
                    entry = m.get(taxis, taxis_id)
                    taxiss = me.getValue(entry)                   
                else:
                    taxiss = new_taxi(taxis_id)
                    m.put(taxis, taxis_id, taxiss)

                taxiss['services'] += 1    
                taxiss['money'] += float(money)
                taxiss['miles'] += float(miles)

                #Cálculo de puntos 

                puntos = alpha_fuction(taxiss['miles'], taxiss['money'], taxiss['services'])
                taxiss['points'] = puntos
            else: 
                None

    lst = m.keySet(catalog['taxis_filter'])    
    iterator = it.newIterator(lst)
    lista_taxis = []
    mayor = []

    while it.hasNext(iterator):
        taxis = it.next(iterator)        
        points = m.get(catalog['taxis_filter'], taxis)['value'] 
        if points['miles'] != 0.0 and points['money'] != 0.0 :                
            lista_taxis.append(points)
            m.remove(catalog['taxis_filter'], taxis)     

    if len(lista_taxis) == 0:
        print('No se regustran taxis, vuelva a intentarlo')
        mayor = None
    else:
        while len(lista_taxis)-1 != 0:        
            for i in range(len(lista_taxis)-1): 
                if lista_taxis[i]['points'] >= lista_taxis[i+1]['points']:
                    aux = lista_taxis[i]
                    lista_taxis[i] = lista_taxis[i+1]
                    lista_taxis[i+1] = aux
                
            mayor_taxi = lista_taxis.pop(len(lista_taxis)-1)
            mayor.append(mayor_taxi)
        print('\nSe tienen ' + str(len(mayor)) + ' taxis, seleccione un número menor o igual\n' )
    return mayor

def getTaxisbyRange(list, number_of_taxis):
    if list == None:
        None
    else:
        for i in range(0, number_of_taxis):
            print('\n' + str(i+1) + '\n------------------------------------------------------------')
            print('\033[1m' + 'Taxi id: ' + '\033[0m' + list[i]['taxi'])
            print('\033[1m' + 'Taxi services: ' + '\033[0m' + str(list[i]['services']))
            print('\033[1m' +'Taxi money: ' + '\033[0m' + str(list[i]['money']))
            print('\033[1m' +'Taxi miles: ' + '\033[0m' + str(list[i]['miles']))
            print('\033[1m' +'Taxi points: '+ '\033[0m' + str(list[i]['points']))
            print('------------------------------------------------------------')
            print ('\033[0m')

def index_height(catalog):
    """
    Altura del arbol
    """
    return om.height(catalog['date_index'])

def index_size(catalog):
    """
    Número de elementos 
    """
    return om.size(catalog['date_index'])

def maxKey(catalog):
    """
    Llave más grande 
    """
    return om.maxKey(catalog['date_index'])

def minKey(catalog):
    """
    Llave más pequeña
    """
    return om.minKey(catalog['date_index'])
# ==============================
# Funciones Helper
# ==============================

# ==============================
# Funciones de Comparacion
# ==============================
def compare_dates(date1, date2):
    """
    Compara dos fechas
    """
    if date1 == date2:
        return 0
    elif (date1 > date2):
        return 1
    else:
        return -1

def compare_ids(id_, tag):
    entry = me.getKey(tag)
    if id_ == entry:
        return 0
    elif id_ > entry:
        return 1
    else:
        return 0

def compare_points(points_1, points_2):
    """
    Compara dos fechas
    """
    if points_1 == points_2:
        return 0
    elif (points_1 > points_2):
        return 1
    else:
        return -1