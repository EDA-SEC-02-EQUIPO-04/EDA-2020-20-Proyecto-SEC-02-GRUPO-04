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
import datetime
assert config

"""
En este archivo definimos los TADs que vamos a usar y las operaciones
de creacion y consulta sobre las estructuras de datos.
"""

# -----------------------------------------------------
#                       API
# -----------------------------------------------------

def new_analyzer():
    analyzer = {'date_index': om.newMap(omaptype='RBT', comparefunction= compare_dates),
                'taxis': lt.newList('SINGLE_LINKED', compare_ids),
                'taxis_filter': lt.newList('SINGLE_LINKED')

               }
    return analyzer 

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

def addtaxis(analyzer, information):
    """
    Agrega la información de cada taxi
    """
    taxis = analyzer['taxis_filter']
    taxi_id = int(information['taxi_id'], base= 16)
    existtaxi = m.contains(taxis, taxi_id)
    
    money = information['trip_total'].strip()
    miles = information['trip_miles'].strip()
    if existtaxi:
        entry = m.get(taxis, taxi_id)
        taxiss = me.getValue(entry)
    else:
        taxiss = new_taxi(taxi_id)
        m.put(taxis, taxi_id, taxiss)
    taxiss['services'] += 1    
    taxiss['money'] += float(money)
    taxiss['miles'] += float(miles)
    
    
    #Cálculo de puntos 
    puntos = alpha_fuction(taxiss['miles'], taxiss['money'], taxiss['services'])
    taxiss['points'] = puntos
    print(taxis)

def addTaxi(analyzer, taxi):
    lt.addLast(analyzer['taxis'], taxi)
    updateDateIndex(analyzer['date_index'], taxi)
    return analyzer


def addDateIndex(datentry, information):
    """
    Agrega la información de cada taxi
    """
    lst = datentry['lsttaxis']
    lt.addLast(lst, information)
    serviceIndex = datentry['serviceIndex']
    taxi_id = int(information['taxi_id'], base= 16)
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


def getTaxisbyRange(analyzer, initialDate, finalDate, number_of_taxis):
    lst = om.values(analyzer['date_index'], initialDate, finalDate)
    lsts = om.keys(analyzer['date_index'], initialDate, finalDate)
    listiterator = it.newIterator(lst)
    while it.hasNext(listiterator):
        lstdate = it.next(listiterator)['lsttaxis']
        iterator_2 = it.newIterator(lstdate)
        while it.hasNext(iterator_2):
            prueba = it.next(iterator_2)
            print(prueba['trip_start_timestamp'])

def maxKey(analyzer):
    """
    Llave más grande 
    """
    return om.maxKey(analyzer['date_index'])

def minKey(analyzer):
    """
    Llave más pequeña
    """
    return om.minKey(analyzer['date_index'])
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
    if int(id_) == int(entry):
        return 0
    elif int(id_) > int(entry):
        return 1
    else:
        return 0