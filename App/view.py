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
from DISClib.DataStructures import listiterator as it
import timeit
assert config

"""
La vista se encarga de la interacción con el usuario.
Presenta el menu de opciones  y  por cada seleccion
hace la solicitud al controlador para ejecutar la
operación seleccionada.
"""

# ___________________________________________________
#  Variables
# ___________________________________________________

small_file = "taxi-trips-wrvz-psew-subset-small.csv"
medium_file = "taxi-trips-wrvz-psew-subset-medium.csv"
large_file = "taxi-trips-wrvz-psew-subset-large.csv"

# ___________________________________________________
#  Menu principal
# ___________________________________________________
def print_menu():
    print('\n')
    print('-----------------------------------------------')
    print('1- Inicializar Catálogo')
    print('2- Cargar información de taxis')
    print('3- Reporte general')
    print('4- ...')
    print('5- ...')
    print('0- Salir')
    print('-----------------------------------------------')

def option_two():
    selection = input("Seleccione un archivo a cargar:\na- Small\nb- Medium\nc- Large\nIngrese una letra: ")
    if selection == "a":
        file = small_file
    elif selection == "b":
        file = medium_file
    elif selection == "c":
        file = large_file
    else:
        print("Dato inválido")
    controller.loadFile(cont, file)
    
def option_three():
    top_number_1 = int(input("Ingrese el rango para el top de compañías ordenadas por cantidad de taxis afiliados: "))
    top_number_2 = int(input("Ingrese el rango para el top de compañías que más servicios prestaron: "))
    taxis_total = controller.taxis_total(cont)
    companies_total = controller.companies_total(cont)
    top_companies_by_taxis = controller.top_companies_by_taxis(cont, top_number_1)
    top_companies_by_services = controller.top_companies_by_services(cont, top_number_2)
    print("Número total de taxis en los servicios reportados:",taxis_total)
    print("Número total de compañías que tienen al menos un taxi inscrito:",companies_total)
    print("Top",top_number_1,"de compañías por cantidad de taxis afiliados")
    iterator_1 = it.newIterator(top_companies_by_taxis)
    while it.hasNext(iterator_1):
        company = it.next(iterator_1)
        print(company[0],"| Taxis afiliados:",company[1])
    print("Top",top_number_2,"de compañías por cantidad de servicios prestados")
    iterator_2 = it.newIterator(top_companies_by_services)
    while it.hasNext(iterator_2):
        company = it.next(iterator_2)
        print(company[0],"| Taxis afiliados:",company[1])
    

"""
Menu principal
"""
while True:

    print_menu()
    inputs = input('Seleccione una opción para continuar \n')

    if int(inputs[0]) == 1:
        print('\nInicializando...')
        cont = controller.init_catalog()
    elif int(inputs[0]) == 2:
        option_two()
    elif int(inputs[0]) == 3:
        option_three()
    elif int(inputs[0]) == 4:
        option_four()
    elif int(inputs[0]) == 5:
        execution_time = timeit.timeit(option_five, number=1)
        print("Tiempo de ejecución: " + str(execution_time))
    else:
        sys.exit(0)
sys.exit(0)