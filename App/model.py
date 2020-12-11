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
def new_catalog():
    catalog = {
               "taxis": {"taxi_lst": lt.newList(cmpfunction=compare_taxis)},
               "companies": {"companies_lst": lt.newList(cmpfunction=compare_companies), "companies_per_services": m.newMap(comparefunction=compare_companies), "companies_per_taxis": m.newMap(comparefunction=compare_companies)}
               }
    return catalog

# Funciones para agregar informacion
def add_taxi(catalog, service):
    taxi = service["taxi_id"]
    taxi_lst = catalog["taxis"]["taxi_lst"]
    if lt.isPresent(taxi_lst, taxi) == 0:
        lt.addLast(taxi_lst, taxi)
    return catalog

def add_company(catalog, service):
    companies_lst = catalog["companies"]["companies_lst"]
    companies_per_services = catalog["companies"]["companies_per_services"]
    companies_per_taxis = catalog["companies"]["companies_per_taxis"]
    taxi = service["taxi_id"]
    if service["company"] == "":
        company = "Independent Owner"
    else:
        company = service["company"]

    if lt.isPresent(companies_lst, company) == 0:
        lt.addLast(companies_lst, company)

    if m.get(companies_per_services, company) != None:
        services_number = me.getValue(m.get(companies_per_services, company))
        services_number += 1 
    else:
        services_number = 1
    m.put(companies_per_services, company, services_number)

    if m.get(companies_per_taxis, company) != None:
        taxis_number = me.getValue(m.get(companies_per_taxis, company))["taxis_number"]
        taxis_lst = me.getValue(m.get(companies_per_taxis, company))["taxis_lst"]
        if lt.isPresent(taxis_lst, taxi) == 0:
            taxis_number += 1
            lt.addLast(taxis_lst, taxi)
    else:
        value_dict = {"taxis_number": 1, "taxis_lst": lt.newList(cmpfunction=compare_taxis)}
        m.put(companies_per_taxis, company, value_dict)
    return catalog

# ==============================
# Funciones de consulta
# ==============================
def taxis_total(catalog):
    taxis_lst = catalog["taxis"]["taxi_lst"]
    size = lt.size(taxis_lst)
    return size

def companies_total(catalog):
    companies_lst = catalog["companies"]["companies_lst"]
    size = lt.size(companies_lst)
    return size

def top_companies_by_taxis(catalog, top_number):
    companies_per_taxis = catalog["companies"]["companies_per_taxis"]
    key_lst = m.keySet(companies_per_taxis)
    iterator = it.newIterator(key_lst)
    greater = 0
    counter = 0
    lst = lt.newList(cmpfunction=compare_companies)
    while counter < top_number:
        while it.hasNext(iterator):
            company = it.next(iterator)
            entry = m.get(companies_per_taxis, company)
            taxis_number = me.getValue(entry)["taxis_number"]
            if taxis_number > greater:
                greater = taxis_number
                greater_company = company
        lt.addLast(lst, (greater_company, greater))
        pos = lt.isPresent(key_lst, greater_company)
        lt.deleteElement(key_lst, pos)
        counter += 1
    return lst

def top_companies_by_services(catalog, top_number):
    companies_per_services = catalog["companies"]["companies_per_services"]
    key_lst = m.keySet(companies_per_services)
    iterator = it.newIterator(key_lst)
    greater = 0
    counter = 0
    lst = lt.newList(cmpfunction=compare_companies)
    while counter < top_number:
        while it.hasNext(iterator):
            company = it.next(iterator)
            entry = m.get(companies_per_services, company)
            services_number = me.getValue(entry)
            if services_number > greater:
                greater = services_number
                greater_company = company
        lt.addLast(lst, (greater_company, greater))
        pos = lt.isPresent(key_lst, greater_company)
        lt.deleteElement(key_lst, pos)
        counter += 1
    return lst
        

# ==============================
# Funciones Helper
# ==============================

# ==============================
# Funciones de Comparacion
# ==============================
def compare_taxis(id1, id2):
    if id1 == id2:
        return 0
    elif id1 > id2:
        return 1
    else:
        return -1

def compare_companies(company1, company2):
    if type(company2) is not str:
        company2 = company2["key"]
    if type(company1) is not str:
        company1 = company1["key"]
    if company1 == company2:
        return 0
    elif company1 > company2:
        return 1
    else:
        return -1