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
                'taxis': m.newMap(60000,maptype='CHAINING', loadfactor=0.5, comparefunction=compare_ids)

               }
    return analyzer 

def new_taxi(taxi):
    taxis = {'taxi_id': taxi,
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
    if services == 0:
        None
    else:
        alpha = (miles/money)*services
        return alpha

def addtaxis(analyzer, information):
    """
    Agrega la información de cada taxi
    """

    taxis = analyzer['taxis']
    taxi_id = int(information['taxi_id'], base= 16)
    existtaxi = m.contains(taxis, taxi_id)
    money = information['trip_total']
    miles = information['trip_miles']

    if existtaxi:
        entry = m.get(taxis, taxi_id)
        taxiss = me.getValue(entry)
    else:
        taxiss = new_taxi(taxi_id)
        m.put(taxis, taxi_id, taxiss)
    taxiss['services'] += 1
    taxiss['money'] += float(money)
    taxiss['miles'] += float(miles)
    print(taxiss['services'])

    #Cálculo de puntos 
    print('***'+ str(taxi_id))
    puntos = alpha_fuction(taxiss['miles'], taxiss['money'], taxiss['services'])
    taxiss['points'] = puntos
    
    print(taxiss)

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