"""
 * Copyright 2020, Departamento de sistemas y Computación,
   Universidad de Los Andes
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
 """

import pytest
import config
from DISClib.DataStructures import listiterator as it
from DISClib.ADT import queue as q

assert config

list_type = 'ARRAY_LIST'

"""
   Creacion de diccionarios utilizados en las pruebas de la estructura de datos
"""
book1 = {'book_id': '1', 'book_title': 'Title 1', 'author': 'author 1'}
book2 = {'book_id': '2', 'book_title': 'Title 2', 'author': 'author 2'}
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


def test_queueElements():
    """
    Se prueba la creacion de una nueva cola, se agregan todos los datos
    creados por sistema y se imprime su valor
    """
    queue = q.newQueue(list_type)

    q.enqueue(queue, book5)
    q.enqueue(queue, book6)
    q.enqueue(queue, book3)
    q.enqueue(queue, book10)
    q.enqueue(queue, book1)
    q.enqueue(queue, book2)
    q.enqueue(queue, book8)
    q.enqueue(queue, book4)
    q.enqueue(queue, book7)
    q.enqueue(queue, book9)
    iterator = it.newIterator(queue)
    while it.hasNext(iterator):
        element = it.next(iterator)
        result = ("".join(str(key) + ": " + str(value) + ",  "
                          for key, value in element.items()))
        print(result)


def test_sizeQueue():
    """
    Se prueba la creacion de una cola y la relacion con el tamaño al
    ingresar datos
    """

    queue = q.newQueue(list_type)
    assert (q.size(queue) == 0)
    assert (q.isEmpty(queue))
    queue = q.newQueue(list_type)

    q.enqueue(queue, book5)
    q.enqueue(queue, book6)
    q.enqueue(queue, book3)
    q.enqueue(queue, book10)
    q.enqueue(queue, book1)
    q.enqueue(queue, book2)
    q.enqueue(queue, book8)
    q.enqueue(queue, book4)
    q.enqueue(queue, book7)
    q.enqueue(queue, book9)
    assert q.size(queue) == 10


def test_infoElements():
    """
    Este test busca confirmar que los datos se almacenen de forma
    correcta y que sean los valores correctos en el orden apropiado
    de la estructura.
    """
    queue = q.newQueue(list_type)
    assert (q.size(queue) == 0)
    assert (q.isEmpty(queue))
    queue = q.newQueue(list_type)

    q.enqueue(queue, book5)
    q.enqueue(queue, book6)
    q.enqueue(queue, book3)
    q.enqueue(queue, book10)
    q.enqueue(queue, book1)
    q.enqueue(queue, book2)
    q.enqueue(queue, book8)
    q.enqueue(queue, book4)
    q.enqueue(queue, book7)
    q.enqueue(queue, book9)

    elem = q.peek(queue)
    assert (q.size(queue) == 10)
    assert (elem == book5)

    elem = q.dequeue(queue)
    assert (q.size(queue) == 9)
    assert (elem == book5)

    elem = q.dequeue(queue)
    assert (q.size(queue) == 8)
    assert (elem == book6)

    elem = q.peek(queue)
    assert (q.size(queue) == 8)
    assert (elem == book3)

    q.enqueue(queue, book9)
    assert (q.size(queue) == 9)
    elem = q.peek(queue)
    assert (elem == book3)


def test_peek_dequeue():
    """
    Este test prueba la creacion de una cola y que el orden de salida
    sea el correcto para la estructura en cuestion, y que el tamaño
    se reduzca para cada salida de objeto
    """

    queue = q.newQueue(list_type)
    assert q.size(queue) == 0
    assert q.isEmpty(queue)
    queue = q.newQueue(list_type)

    q.enqueue(queue, book5)
    q.enqueue(queue, book6)
    q.enqueue(queue, book3)
    q.enqueue(queue, book10)
    q.enqueue(queue, book1)
    q.enqueue(queue, book2)
    q.enqueue(queue, book8)
    q.enqueue(queue, book4)
    q.enqueue(queue, book7)
    q.enqueue(queue, book9)
    total = q.size(queue)
    while not (q.isEmpty(queue)):
        peek = q.peek(queue)
        assert (q.dequeue(queue) == peek)
        total -= 1
        assert (total == q.size(queue))


def test_enqueue_dequeue():
    """
    Este test prueba que la cola pueda manejar inserciones y eliminaciones
    de forma correcta siguiendo un orden establecido, y que no quede
    referencia al objeto sacado despues de haberlo removido de la
    cola
    """
    queue = q.newQueue(list_type)
    assert (q.size(queue) == 0)
    assert (q.isEmpty(queue))

    q.enqueue(queue, book5)
    assert (q.size(queue) == 1)
    assert (q.peek(queue) == q.dequeue(queue))
    assert (q.size(queue) == 0)

    q.enqueue(queue, book6)
    assert (q.size(queue) == 1)
    assert (q.peek(queue) == q.dequeue(queue))
    assert (q.size(queue) == 0)

    q.enqueue(queue, book3)
    assert (q.size(queue) == 1)
    assert (q.peek(queue) == q.dequeue(queue))
    assert (q.size(queue) == 0)

    q.enqueue(queue, book10)
    assert (q.size(queue) == 1)
    assert (q.peek(queue) == q.dequeue(queue))
    assert (q.size(queue) == 0)

    q.enqueue(queue, book1)
    assert (q.size(queue) == 1)
    assert (q.peek(queue) == q.dequeue(queue))
    assert (q.size(queue) == 0)

    q.enqueue(queue, book2)
    assert (q.size(queue) == 1)
    assert (q.peek(queue) == q.dequeue(queue))
    assert (q.size(queue) == 0)

    q.enqueue(queue, book8)
    q.enqueue(queue, book4)
    q.enqueue(queue, book7)
    q.enqueue(queue, book9)

    assert (q.size(queue) == 4)
    assert book8 == q.dequeue(queue)
    assert book4 == q.dequeue(queue)
    assert book7 == q.dequeue(queue)
    assert book9 == q.dequeue(queue)

    assert (q.size(queue) == 0)


def test_error_dequeue():
    """
    Este test busca comprobar que es imposible eliminar un objeto de
    una cola vacia
    """
    queue = q.newQueue(list_type)
    assert (q.size(queue) == 0)
    assert (q.isEmpty(queue))

    with pytest.raises(Exception):
        q.dequeue(queue)
