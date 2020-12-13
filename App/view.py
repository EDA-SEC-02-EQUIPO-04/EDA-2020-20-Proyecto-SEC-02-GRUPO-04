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


import sys
import config
from App import controller
from DISClib.ADT import stack
import timeit
assert config
import sys 

"""
La vista se encarga de la interacción con el usuario.
Presenta el menu de opciones  y  por cada seleccion
hace la solicitud al controlador para ejecutar la
operación seleccionada.
"""

# ___________________________________________________
#  Variables
# ___________________________________________________

taxisfile = 'taxi_trips_medium.csv'
recursionlimit = sys.setrecursionlimit(16000)

# ___________________________________________________
#  Menu principal
# ___________________________________________________

def printMenu():
    print('\n')
    print('--------------------------------------------------')
    print('1- Inicializar Analizador')
    print('2- Cargar información taxis en Chicago')
    print('3- Información ?')
    print('4- Número de taxis en los servicios reportados')
    print('5- Número total de compañias con un taxi inscrito')
    print('6- Top compañias con taxis afiliados')
    print('7- Top compañias por servicios prestados')
    print('8- Taxis según fecha determinada')
    print('9- Taxis con más puntos')
    print('10- Mejor horario')
    print('0- Salir')
    print('--------------------------------------------------')

def option_four():
    print('\nBuscando taxis con mejor puntaje en un rango de fechas')
    initialDate = input('Rango inicial (YYYY-MM-DD): ').strip()
    finalDate = input('Rango final (YYYY-MM-DD): ').strip()
    lista = controller.getTaxis(cont, initialDate, finalDate)
    if lista != None:
        number_of_taxis = int(input('Número de taxis: '))
        return controller.getTaxisbyRange(lista, number_of_taxis)

def option_five():
    print('\nBuscando taxis con mejor puntaje en una fecha')
    initialDate = input('Rango inicial (YYYY-MM-DD): ').strip()
    lista = controller.getTaxis(cont, initialDate, initialDate)
    if lista != None:
        number_of_taxis = int(input('Número de taxis: '))
        return controller.getTaxisbyRange(lista, number_of_taxis)

"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar \n')

    if int(inputs[0]) == 1:
        print('\nInicializando...')
        cont = controller.init_catalog()
    elif int(inputs[0]) == 2:
        controller.load_data(cont, taxisfile)
        print('Altura del arbol: ' + str(controller.index_height(cont)))
        print('Elementos en el arbol: ' + str(controller.index_size(cont)))
        print('Mayor llave: ' + str(controller.maxKey(cont)))
        print('Menor llave: ' + str(controller.minKey(cont)))        
    elif int(inputs[0]) == 3:
        None
    elif int(inputs[0]) == 4:
        option_four()
    elif int(inputs[0]) == 5:
        option_five()
    elif int(inputs[0]) == 6:
        None
    elif int(inputs[0]) == 7:
        None
    elif int(inputs[0]) == 8:
        None
    elif int(inputs[0]) == 9:
        None
    elif int(inputs[0]) == 10:
        None
    else:
        sys.exit(0)
sys.exit(0)