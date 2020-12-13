"""
 * Copyright 2020, Departamento de sistemas y Computación
 * Universidad de Los Andes
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
 """

import pytest
import config
from DISClib.DataStructures import listiterator as it
from DISClib.ADT import stack as st

assert config

list_type = 'ARRAY_LIST'

"""
   Creacion de diccionarios utilizados en las pruebas de la estructura de datos
"""

book1 = {'book_id': '1', 'book_title': 'Title 1', 'author': 'author 1'}
book2 = {'book_id': '2', 'book_title': ' Title 2', 'author': 'author 2'}
book3 = {'book_id': '3', 'book_title': 'Title 3', 'author': 'author 3'}
book4 = {'book_id': '4', 'book_title': 'Title 4', 'author': 'author 4'}
book5 = {'book_id': '5', 'book_title': 'Title 5', 'author': 'author 5'}
book6 = {'book_id': '6', 'book_title': 'Title 6', 'author': 'author 6'}
book7 = {'book_id': '7', 'book_title': 'Title 7', 'author': 'author 7'}
book8 = {'book_id': '8', 'book_title': 'Title 8', 'author': 'author 8'}
book9 = {'book_id': '9', 'book_title': 'Title 9', 'author': 'author 9'}
book10 = {'book_id': '10', 'book_title': 'Title 10', 'author': 'author 10'}
book11 = {'book_id': '7', 'book_title': 'Title 11', 'author': 'author 11'}
book12 = {'book_id': '8', 'book_title': 'Title 12', 'author': 'author 12'}
book13 = {'book_id': '9', 'book_title': 'Title 13', 'author': 'author 13'}
book14 = {'book_id': '10', 'book_title': 'Title 14', 'author': 'author 14'}


def test_pushElements():
    """
    Se prueba la creacion de una nueva pila, se agregan todos los datos
    creados por sistema y se imprime su valor
    """
    stack = st.newStack(list_type)

    st.push(stack, book5)
    st.push(stack, book6)
    st.push(stack, book3)
    st.push(stack, book10)
    st.push(stack, book1)
    st.push(stack, book2)
    st.push(stack, book8)
    st.push(stack, book4)
    st.push(stack, book7)
    st.push(stack, book9)
    iterator = it.newIterator(stack)
    while it.hasNext(iterator):
        element = it.next(iterator)
        print(element)


def test_sizeStack():
    """
    Se prueba la creacion de una cola y la relacion con el
    tamaño al ingresar datos
    """

    stack = st.newStack(list_type)
    assert (st.size(stack) == 0)
    assert (st.isEmpty(stack))
    st.push(stack, book5)
    st.push(stack, book6)
    st.push(stack, book3)
    st.push(stack, book10)
    st.push(stack, book1)
    st.push(stack, book2)
    st.push(stack, book8)
    st.push(stack, book4)
    st.push(stack, book7)
    st.push(stack, book9)
    assert st.size(stack) == 10


def test_infoElements():
    """
    Este test busca confirmar que los datos se almacenen de forma correcta
    y que sean los valores correctos en el orden apropiado de la estructura.
    """
    stack = st.newStack(list_type)
    assert (st.size(stack) == 0)
    assert (st.isEmpty(stack))
    st.push(stack, book5)
    st.push(stack, book6)
    st.push(stack, book3)
    st.push(stack, book10)
    st.push(stack, book1)
    st.push(stack, book2)
    st.push(stack, book8)
    st.push(stack, book4)
    st.push(stack, book7)
    st.push(stack, book9)

    elem = st.top(stack)
    assert (st.size(stack) == 10)
    assert (elem == book9)

    elem = st.pop(stack)
    assert (st.size(stack) == 9)
    assert (elem == book9)

    elem = st.pop(stack)
    assert (st.size(stack) == 8)
    assert (elem == book7)

    elem = st.top(stack)
    assert (st.size(stack) == 8)
    assert (elem == book4)

    st.push(stack, book9)
    assert (st.size(stack) == 9)
    elem = st.top(stack)
    assert (elem == book9)


def test_top_pop():
    """
    Este test prueba la creacion de una cola y que el orden de salida sea
    el correcto para la estructura en cuestion, y que el tamaño se reduzca
    para cada salida de objeto
    """
    stack = st.newStack(list_type)
    assert st.size(stack) == 0
    assert st.isEmpty(stack)
    st.push(stack, book5)
    st.push(stack, book6)
    st.push(stack, book3)
    st.push(stack, book10)
    st.push(stack, book1)
    st.push(stack, book2)
    st.push(stack, book8)
    st.push(stack, book4)
    st.push(stack, book7)
    st.push(stack, book9)
    total = st.size(stack)
    while not (st.isEmpty(stack)):
        top = st.top(stack)
        assert (st.pop(stack) == top)
        total -= 1
        assert (total == st.size(stack))


def test_push_pop():
    """
    Este test prueba que la cola pueda manejar inserciones y eliminaciones
    de forma correcta siguiendo un orden establecido, y que no quede
    referencia al objeto sacado despues de haberlo removido de la
    cola
    """
    stack = st.newStack(list_type)
    assert (st.size(stack) == 0)
    assert (st.isEmpty(stack))

    st.push(stack, book5)
    assert (st.size(stack) == 1)
    assert (st.top(stack) == st.pop(stack))
    assert (st.size(stack) == 0)

    st.push(stack, book6)
    assert (st.size(stack) == 1)
    assert (st.top(stack) == st.pop(stack))
    assert (st.size(stack) == 0)

    st.push(stack, book3)
    assert (st.size(stack) == 1)
    assert (st.top(stack) == st.pop(stack))
    assert (st.size(stack) == 0)

    st.push(stack, book10)
    assert (st.size(stack) == 1)
    assert (st.top(stack) == st.pop(stack))
    assert (st.size(stack) == 0)

    st.push(stack, book1)
    assert (st.size(stack) == 1)
    assert (st.top(stack) == st.pop(stack))
    assert (st.size(stack) == 0)

    st.push(stack, book2)
    assert (st.size(stack) == 1)
    assert (st.top(stack) == st.pop(stack))
    assert (st.size(stack) == 0)

    st.push(stack, book8)
    st.push(stack, book4)
    st.push(stack, book7)
    st.push(stack, book9)

    assert (st.size(stack) == 4)
    assert book9 == st.pop(stack)
    assert book7 == st.pop(stack)
    assert book4 == st.pop(stack)
    assert book8 == st.pop(stack)

    assert (st.size(stack) == 0)


def test_error_pop():
    """
    Este test busca comprobar que es imposible eliminar un objeto
    de una pila vacia
    """
    stack = st.newStack(list_type)
    assert (st.size(stack) == 0)
    assert (st.isEmpty(stack))

    with pytest.raises(Exception):
        st.pop(stack)
