"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
 *
 * Desarrollado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
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
 *
 * Contribución de:
 *
 * Dario Correal
 *
 """

import config
from DISClib.DataStructures import adjlist as alt

assert config

"""
  Este módulo implementa el tipo abstracto de datos (TAD) Graph.
  Se puede implementar sobre una lista de adyacencias (ADJ_LIST)
  o una matriz de adyacencias (ADJ_MATRIX)
"""


def newGraph(datastructure, directed, size, comparefunction):
    """
    Crea un grafo vacio

    Args:
        size: Tamaño inicial del grafo
        cmpfunction: Funcion de comparacion
        directed: Indica si el grafo es dirigido o no
    Returns:
        Un nuevo grafo
    Raises:
        Exception
    """
    if (datastructure == "ADJ_LIST"):
        graph = alt.newGraph(size, comparefunction, directed)
        return graph
    else:
        return None


def insertVertex(graph, vertex):
    """
    Inserta el vertice vertex en el grafo graph

    Args:
        graph: El grafo sobre el que se ejecuta la operacion
        vertex: El vertice que se desea insertar
    Returns:
        Un nuevo grafo
    Raises:
        Exception
    """
    if (graph['type'] == "ADJ_LIST"):
        return alt.insertVertex(graph, vertex)


def removeVertex(graph, vertex):
    """
    Remueve el vertice vertex del grafo graph

    Args:
        graph: El grafo sobre el que se ejecuta la operacion
        vertex: El vertice que se desea remover
    Returns:
        Un nuevo grafo
    Raises:
        Exception
    """
    if (graph['type'] == "ADJ_LIST"):
        return alt.removeVertex(graph, vertex)


def numVertices(graph):
    """
    Retorna el numero de vertices en el  grafo graph

    Args:
        graph: El grafo sobre el que se ejecuta la operacion

    Returns:
        El numero de vertices
    Raises:
        Exception
    """
    if (graph['type'] == "ADJ_LIST"):
        return alt.numVertices(graph)


def numEdges(graph):
    """
    Retorna el numero de arcos en el  grafo graph

    Args:
        graph: El grafo sobre el que se ejecuta la operacion

    Returns:
        El numero de vertices
    Raises:
        Exception
    """
    if (graph['type'] == "ADJ_LIST"):
        return alt.numEdges(graph)


def vertices(graph):
    """
    Retorna una lista con todos los vertices del grafo graph
    Args:
        graph: El grafo sobre el que se ejecuta la operacion

    Returns:
        El numero de vertices
    Raises:
        Exception
    """
    if (graph['type'] == "ADJ_LIST"):
        return alt.vertices(graph)


def edges(graph):
    """
    Retorna una lista con todos los arcos del grafo graph

    Args:
        graph: El grafo sobre el que se ejecuta la operacion

    Returns:
        Una lista con los arcos
    Raises:
        Exception
    """
    if (graph['type'] == "ADJ_LIST"):
        return alt.edges(graph)


def degree(graph, vertex):
    """
    Retorna el numero de arcos asociados al vertice vertex

    Args:
        graph: El grafo sobre el que se ejecuta la operacion
        vertex: El vertice del que se desea conocer el grado

    Returns:
        El grado del vertice
    Raises:
        Exception
    """
    if (graph['type'] == "ADJ_LIST"):
        return alt.degree(graph, vertex)


def outdegree(graph, vertex):
    """
    Retorna el numero de arcos que salen del grafo vertex

    Args:
        graph: El grafo sobre el que se ejecuta la operacion
        vertex: El vertice del que se desea conocer el grado

    Returns:
        El grado del vertice
    Raises:
        Exception
    """
    if (graph['type'] == "ADJ_LIST"):
        return alt.outdegree(graph, vertex)


def indegree(graph, vertex):
    """
    Retorna el numero de arcos que llegan al vertice vertex

    Args:
        graph: El grafo sobre el que se ejecuta la operacion
        vertex: El vertice del que se desea conocer el grado

    Returns:
        El grado del vertice
    Raises:
        Exception
    """
    if (graph['type'] == "ADJ_LIST"):
        return alt.indegree(graph, vertex)


def getEdge(graph, vertexa, vertexb):
    """
    Retorna el arco asociado a los vertices vertexa ---- vertexb

    Args:
        graph: El grafo sobre el que se ejecuta la operacion
        vertexa: Vertice de inicio
        vertexb: Vertice destino

    Returns:
        El grado el arco
    Raises:
        Exception
    """
    if (graph['type'] == "ADJ_LIST"):
        return alt.getEdge(graph, vertexa, vertexb)


def addEdge(graph, vertexa, vertexb, weight):
    """
    Agrega un arco entre los vertices vertexa ---- vertexb, con peso weight.
    Si el grafo es no dirigido se adiciona dos veces el mismo arco,
    en el mismo orden
    Si el grafo es dirigido se adiciona solo el arco vertexa --> vertexb

    Args:
        graph: El grafo sobre el que se ejecuta la operacion
        vertexa: Vertice de inicio
        vertexb: Vertice de destino
        wight: peso del arco

    Returns:
       True si el vertice esta presente
    Raises:
        Exception
    """
    if (graph['type'] == "ADJ_LIST"):
        return alt.addEdge(graph, vertexa, vertexb, weight)


def containsVertex(graph, vertex):
    """
    Retorna el arco asociado a los vertices vertexa ---- vertexb

    Args:
        graph: El grafo sobre el que se ejecuta la operacion
        vertexa: Vertice que se busca

    Returns:
       True si el vertice esta presente
    Raises:
        Exception
    """
    if (graph['type'] == "ADJ_LIST"):
        return alt.containsVertex(graph, vertex)


def adjacents(graph, vertex):
    """
    Retorna una lista con todos los vertices adyacentes al vertice vertex

    Args:
        graph: El grafo sobre el que se ejecuta la operacion
        vertex: El vertice del que se quiere la lista

    Returns:
        La lista de adyacencias
    Raises:
        Exception
    """
    if (graph['type'] == "ADJ_LIST"):
        return alt.adjacents(graph, vertex)


def adjacentEdges(graph, vertex):
    """
    Retorna una lista con todos los arcos asociados a los vértices
    adyacentes de vertex

    Args:
        graph: El grafo sobre el que se ejecuta la operacion
        vertex: El vertice del que se quiere la lista

    Returns:
        La lista de adyacencias
    Raises:
        Exception
    """
    if (graph['type'] == "ADJ_LIST"):
        return alt.adjacentEdges(graph, vertex)
