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
    catalog = model.new_catalog()
    return catalog

# ___________________________________________________
#  Funciones para la carga de datos y almacenamiento
#  de datos en los modelos
# ___________________________________________________
def loadFile(catalog, service_file):
    service_file = cf.data_dir + service_file
    input_file = csv.DictReader(open(service_file, encoding= 'utf-8'), delimiter = ',')
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
