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
def init_analyzer():
    """
    Llama a la función de inicialización del analizador
    """
    t1_start = process_time()
    analyzer = model.new_analyzer()
    t1_stop = process_time()
    print('Tiempo de ejecución ', t1_stop - t1_start, ' segundos')
    return analyzer

# ___________________________________________________
#  Funciones para la carga de datos y almacenamiento
#  de datos en los modelos
# ___________________________________________________
def load_data(analyzer, taxis_file):
    """
    Carga los datos del archivo
    """
    t1_start = process_time()
    load_taxis(analyzer, taxis_file)
    t1_stop = process_time()
    print('Tiempo de ejecución ', t1_stop - t1_start, ' segundos')


def load_taxis(analyzer, taxisfile):
    dialect, dialect.delimeter = csv.excel, ';'
    input_file = csv.DictReader(open(taxisfile, encoding='utf-8-sig'))
    for taxi in input_file:
        strip_dire = {}
        for key, value in taxi.items():
            strip_dire[key.strip()] = value.strip()
        taxi = strip_dire
        model.addtaxis(analyzer, taxi)
# ___________________________________________________
#  Funciones para consultas
# ___________________________________________________