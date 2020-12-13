import pytest
import config
from DISClib.ADT import graph as g
from DISClib.Algorithms.Graphs import scc

assert config


@pytest.fixture
def graph():
    graph = g.newGraph(size=12, directed=True, comparefunction=compareVertices)

    g.insertVertex(graph, 'Pedro')
    g.insertVertex(graph, 'Maria')
    g.insertVertex(graph, 'Carol')
    g.insertVertex(graph, 'Laura')
    g.insertVertex(graph, 'Felipe')
    g.insertVertex(graph, 'Jose')
    g.insertVertex(graph, 'Martin')
    g.insertVertex(graph, 'Camila')
    g.insertVertex(graph, 'Gloria')
    g.insertVertex(graph, 'Luz')
    g.insertVertex(graph, 'Tere')
    g.insertVertex(graph, 'Susana')

    g.addEdge(graph, 'Pedro', 'Jose')
    g.addEdge(graph, 'Jose', 'Felipe')
    g.addEdge(graph, 'Felipe', 'Laura')
    g.addEdge(graph, 'Laura', 'Carol')
    g.addEdge(graph, 'Carol', 'Maria')
    g.addEdge(graph, 'Maria', 'Pedro')
    g.addEdge(graph, 'Camila', 'Jose')
    g.addEdge(graph, 'Camila', 'Martin')
    g.addEdge(graph, 'Martin', 'Gloria')
    g.addEdge(graph, 'Gloria', 'Camila')
    g.addEdge(graph, 'Gloria', 'Luz')
    g.addEdge(graph, 'Luz', 'Tere')
    g.addEdge(graph, 'Tere', 'Susana')
    g.addEdge(graph, 'Susana', 'Luz')

    return graph


def test_scc(graph):
    sc = scc.KosarajuSCC(graph)
    assert scc.connectedComponents(sc) == 3
    assert scc.stronglyConnected(sc, 'Pedro', 'Carol') is True
    assert scc.stronglyConnected(sc, 'Pedro', 'Luz') is False


# --------------------------------------
#       Funciones de Comparacion
# --------------------------------------


def compareVertices(searchname, element):
    if (searchname == element['key']):
        return 0
    elif (searchname < element['key']):
        return -1
    return 1
