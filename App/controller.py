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

import config as cf
from App import model
import csv
from time import process_time
import datetime

"""
El controlador se encarga de mediar entre la vista y el modelo.
Existen algunas operaciones en las que se necesita invocar
el modelo varias veces o integrar varias de las respuestas
del modelo en una sola respuesta.  Esta responsabilidad
recae sobre el controlador.
"""


# ___________________________________________________
#  Inicializacion del catalogo
# ___________________________________________________
def init_catalog():
    """
    Llama a la función de inicialización del analizador
    """
    t1_start = process_time()
    catalog = model.new_catalog()
    t1_stop = process_time()
    print('Tiempo de ejecución ', t1_stop - t1_start, ' segundos')

    return catalog


# ___________________________________________________
#  Funciones para la carga de datos y almacenamiento
#  de datos en los modelos
# ___________________________________________________

def load_data(catalog, taxis_file):
    """
    Carga los datos del archivo
    """
    t1_start = process_time()
    load_taxis(catalog, taxis_file)
    t1_stop = process_time()
    print('Tiempo de ejecución ', t1_stop - t1_start, ' segundos')


def load_taxis(catalog, taxisfile):
    taxisfile = cf.data_dir + taxisfile
    with open(taxisfile, encoding='utf-8') as input_file:
        reader = csv.DictReader(input_file, delimiter=',')
        for taxi in reader:
            if taxi['taxi_id'] == 'NA':
                continue
            elif taxi['taxi_id'] is None:
                continue
            elif taxi['trip_total'] == float(0):
                continue
            elif taxi['trip_miles'] == float(0):
                continue
            elif taxi['trip_total'] is None or taxi['trip_miles'] is None:
                continue
            elif taxi['trip_total'] == "":
                continue
            elif taxi['trip_miles'] == "":
                continue
            else:
                model.addTaxi(catalog, taxi)
    return catalog


# ___________________________________________________
#  Funciones para consultas
# ___________________________________________________
def getTaxis(catalog, initialDate, finalDate):
    initialDate = datetime.datetime.strptime(initialDate, '%Y-%m-%d')
    finalDate = datetime.datetime.strptime(finalDate, '%Y-%m-%d')
    lista = model.TaxisbyRange(catalog, initialDate.date(), finalDate.date())
    return lista


def getTaxisbyRange(lista, number_of_taxis):
    """
    Retorna los N taxis según los puntos obtenidos
    """
    return model.getTaxisbyRange(lista, number_of_taxis)


def index_height(catalog):
    return model.index_height(catalog)


def index_size(catalog):
    return model.index_size(catalog)


def maxKey(catalog):
    return model.maxKey(catalog)


def minKey(catalog):
    return model.minKey(catalog)


def loadFile(catalog, service_file):
    service_file = cf.data_dir + service_file
    input_file = csv.DictReader(open(service_file, encoding='utf-8'), delimiter=',')
    for service in input_file:
        model.add_taxi(catalog, service)
        model.add_company(catalog, service)
    return catalog


# ___________________________________________________
#  Funciones para consultas
# ___________________________________________________
def taxis_total(catalog):
    return model.taxis_total(catalog)


def companies_total(catalog):
    return model.companies_total(catalog)


def top_companies_by_taxis(catalog, top_number):
    return model.top_companies_by_taxis(catalog, top_number)


def top_companies_by_services(catalog, top_number):
    return model.top_companies_by_services(catalog, top_number)


def best_schedule(catalog, origin_area, destination_area, initial_date, final_date):
    initial_date = datetime.datetime.strptime(initial_date, '%Y-%m-%d')
    final_date = datetime.datetime.strptime(final_date, '%Y-%m-%d')
    return model.best_schedule(catalog, origin_area, destination_area, initial_date.date(), final_date.date())
