import pytest
import config
from DISClib.DataStructures import bst as bst
from DISClib.ADT import list as lt

assert config


def cmpfunction(key1, key2):
    if key1 == key2:
        return 0
    elif key1 < key2:
        return -1
    else:
        return 1


@pytest.fixture
def tree():
    tree = bst.newMap(cmpfunction)
    return tree


def test_empty(tree):
    assert bst.isEmpty(tree) is True


def test_put_empty(tree):
    tree = bst.put(tree, 1, 'book1')
    assert bst.size(tree) == 1


def test_put(tree):
    tree = bst.put(tree, 10, 'book10')
    tree = bst.put(tree, 7, 'book7')
    tree = bst.put(tree, 30, 'book30')
    assert bst.size(tree) == 3


def test_put_deep(tree):
    tree = bst.put(tree, 10, 'book10')
    tree = bst.put(tree, 7, 'book7')
    tree = bst.put(tree, 30, 'book30')
    tree = bst.put(tree, 5, 'book5')
    tree = bst.put(tree, 4, 'book4')
    tree = bst.put(tree, 3, 'book3')
    assert bst.size(tree) == 6


def test_get(tree):
    tree = bst.put(tree, 10, 'book10')
    tree = bst.put(tree, 7, 'book7')
    tree = bst.put(tree, 30, 'book30')
    tree = bst.put(tree, 5, 'book5')
    tree = bst.put(tree, 4, 'book4')
    tree = bst.put(tree, 3, 'book3')
    assert bst.size(tree) == 6
    node = bst.get(tree, 3)
    assert node['value'] == 'book3'
    node = bst.get(tree, 34)
    assert node is None


def test_remove(tree):
    tree = bst.put(tree, 21, 'book21')
    tree = bst.put(tree, 7, 'book7')
    tree = bst.put(tree, 30, 'book30')
    tree = bst.put(tree, 5, 'book5')
    tree = bst.put(tree, 4, 'book4')
    tree = bst.put(tree, 3, 'book3')
    tree = bst.put(tree, 20, 'book20')
    tree = bst.put(tree, 25, 'book25')
    tree = bst.put(tree, 35, 'book35')
    tree = bst.put(tree, 29, 'book29')
    tree = bst.put(tree, 11, 'book11')
    tree = bst.put(tree, 15, 'book15')
    tree = bst.remove(tree, 21)
    tree = bst.put(tree, 10, 'book10')
    tree = bst.put(tree, 10, 'book10A')
    assert bst.contains(tree, 29) is True
    assert bst.contains(tree, 28) is False
    assert bst.minKey(tree) == 3
    assert bst.maxKey(tree) == 35
    bst.deleteMin(tree)
    assert bst.contains(tree, 3) is False


def test_ceil_floor(tree):
    tree = bst.put(tree, 23, 'book21')
    tree = bst.put(tree, 7, 'book7')
    tree = bst.put(tree, 30, 'book30')
    tree = bst.put(tree, 5, 'book5')
    tree = bst.put(tree, 4, 'book4')
    tree = bst.put(tree, 3, 'book3')
    tree = bst.put(tree, 20, 'book20')
    tree = bst.put(tree, 25, 'book25')
    tree = bst.put(tree, 35, 'book35')
    tree = bst.put(tree, 29, 'book29')
    tree = bst.put(tree, 11, 'book11')
    tree = bst.put(tree, 15, 'book15')
    tree = bst.put(tree, 10, 'book10')
    assert bst.floor(tree, 21) == 20
    assert bst.floor(tree, 25) == 25
    assert bst.floor(tree, 18) == 15
    assert bst.ceiling(tree, 16) == 20
    assert bst.ceiling(tree, 15) == 15
    assert bst.ceiling(tree, 27) == 29


def test_delete_max_min(tree):
    tree = bst.put(tree, 23, 'book21')
    tree = bst.put(tree, 7, 'book7')
    tree = bst.put(tree, 30, 'book30')
    tree = bst.put(tree, 5, 'book5')
    tree = bst.put(tree, 4, 'book4')
    tree = bst.put(tree, 3, 'book3')
    tree = bst.put(tree, 20, 'book20')
    tree = bst.put(tree, 25, 'book25')
    tree = bst.put(tree, 35, 'book35')
    tree = bst.put(tree, 29, 'book29')
    tree = bst.put(tree, 11, 'book11')
    tree = bst.put(tree, 15, 'book15')
    tree = bst.put(tree, 10, 'book10')
    assert bst.contains(tree, 3) is True
    assert bst.size(tree) == 13
    bst.deleteMin(tree)
    assert bst.contains(tree, 3) is False
    assert bst.size(tree) == 12
    assert bst.contains(tree, 35) is True
    assert bst.size(tree) == 12
    bst.deleteMax(tree)
    assert bst.contains(tree, 35) is False
    assert bst.size(tree) == 11


def test_select(tree):
    tree = bst.put(tree, 23, 'book21')
    tree = bst.put(tree, 7, 'book7')
    tree = bst.put(tree, 30, 'book30')
    tree = bst.put(tree, 5, 'book5')
    tree = bst.put(tree, 4, 'book4')
    tree = bst.put(tree, 3, 'book3')
    tree = bst.put(tree, 20, 'book20')
    tree = bst.put(tree, 25, 'book25')
    tree = bst.put(tree, 35, 'book35')
    tree = bst.put(tree, 29, 'book29')
    tree = bst.put(tree, 11, 'book11')
    tree = bst.put(tree, 15, 'book15')
    tree = bst.put(tree, 10, 'book10')
    assert bst.size(tree) == 13
    assert bst.select(tree, 6) == 15


def test_rank(tree):
    tree = bst.put(tree, 23, 'book21')
    tree = bst.put(tree, 7, 'book7')
    tree = bst.put(tree, 30, 'book30')
    tree = bst.put(tree, 5, 'book5')
    tree = bst.put(tree, 4, 'book4')
    tree = bst.put(tree, 3, 'book3')
    tree = bst.put(tree, 20, 'book20')
    tree = bst.put(tree, 25, 'book25')
    tree = bst.put(tree, 35, 'book35')
    tree = bst.put(tree, 29, 'book29')
    tree = bst.put(tree, 11, 'book11')
    tree = bst.put(tree, 15, 'book15')
    tree = bst.put(tree, 10, 'book10')
    assert bst.size(tree) == 13
    assert bst.rank(tree, 15) == 6


def test_height(tree):
    tree = bst.put(tree, 23, 'book21')
    tree = bst.put(tree, 7, 'book7')
    tree = bst.put(tree, 30, 'book30')
    tree = bst.put(tree, 5, 'book5')
    tree = bst.put(tree, 4, 'book4')
    tree = bst.put(tree, 3, 'book3')
    tree = bst.put(tree, 20, 'book20')
    tree = bst.put(tree, 25, 'book25')
    tree = bst.put(tree, 35, 'book35')
    tree = bst.put(tree, 29, 'book29')
    tree = bst.put(tree, 11, 'book11')
    tree = bst.put(tree, 15, 'book15')
    tree = bst.put(tree, 10, 'book10')
    assert bst.size(tree) == 13
    assert bst.height(tree) == 4
    tree = bst.put(tree, 37, 'book11')
    tree = bst.put(tree, 40, 'book15')
    tree = bst.put(tree, 45, 'book10')
    assert bst.size(tree) == 16
    assert bst.height(tree) == 5


def test_keys(tree):
    tree = bst.put(tree, 23, 'book21')
    tree = bst.put(tree, 7, 'book7')
    tree = bst.put(tree, 30, 'book30')
    tree = bst.put(tree, 5, 'book5')
    tree = bst.put(tree, 4, 'book4')
    tree = bst.put(tree, 3, 'book3')
    tree = bst.put(tree, 20, 'book20')
    tree = bst.put(tree, 25, 'book25')
    tree = bst.put(tree, 35, 'book35')
    tree = bst.put(tree, 29, 'book29')
    tree = bst.put(tree, 11, 'book11')
    tree = bst.put(tree, 15, 'book15')
    tree = bst.put(tree, 10, 'book10')
    tree = bst.put(tree, 37, 'book11')
    tree = bst.put(tree, 40, 'book15')
    tree = bst.put(tree, 45, 'book10')
    assert bst.size(tree) == 16
    lst = bst.keys(tree, 10, 40)
    assert lt.size(lst) == 11


def test_values(tree):
    tree = bst.put(tree, 23, 'book21')
    tree = bst.put(tree, 7, 'book7')
    tree = bst.put(tree, 30, 'book30')
    tree = bst.put(tree, 5, 'book5')
    tree = bst.put(tree, 4, 'book4')
    tree = bst.put(tree, 3, 'book3')
    tree = bst.put(tree, 20, 'book20')
    tree = bst.put(tree, 25, 'book25')
    tree = bst.put(tree, 35, 'book35')
    tree = bst.put(tree, 29, 'book29')
    tree = bst.put(tree, 11, 'book11')
    tree = bst.put(tree, 15, 'book15')
    tree = bst.put(tree, 10, 'book10')
    tree = bst.put(tree, 37, 'book11')
    tree = bst.put(tree, 40, 'book15')
    tree = bst.put(tree, 45, 'book10')
    assert bst.size(tree) == 16
    lst = bst.values(tree, 10, 40)
    assert lt.size(lst) == 11


def test_keySet(tree):
    tree = bst.put(tree, 23, 'book21')
    tree = bst.put(tree, 7, 'book7')
    tree = bst.put(tree, 30, 'book30')
    tree = bst.put(tree, 5, 'book5')
    tree = bst.put(tree, 4, 'book4')
    tree = bst.put(tree, 3, 'book3')
    tree = bst.put(tree, 20, 'book20')
    tree = bst.put(tree, 25, 'book25')
    tree = bst.put(tree, 35, 'book35')
    tree = bst.put(tree, 29, 'book29')
    tree = bst.put(tree, 11, 'book11')
    tree = bst.put(tree, 15, 'book15')
    tree = bst.put(tree, 10, 'book10')
    tree = bst.put(tree, 37, 'book11')
    tree = bst.put(tree, 40, 'book15')
    tree = bst.put(tree, 45, 'book10')
    assert bst.size(tree) == 16
    lst = bst.keySet(tree)
    assert lt.size(lst) == 16
    assert lt.isPresent(lst, 11) > 0


def test_valueSet(tree):
    tree = bst.put(tree, 23, 'book21')
    tree = bst.put(tree, 7, 'book7')
    tree = bst.put(tree, 30, 'book30')
    tree = bst.put(tree, 5, 'book5')
    tree = bst.put(tree, 4, 'book4')
    tree = bst.put(tree, 3, 'book3')
    tree = bst.put(tree, 20, 'book20')
    tree = bst.put(tree, 25, 'book25')
    tree = bst.put(tree, 35, 'book35')
    tree = bst.put(tree, 29, 'book29')
    tree = bst.put(tree, 11, 'book11')
    tree = bst.put(tree, 15, 'book15')
    tree = bst.put(tree, 10, 'book10')
    tree = bst.put(tree, 37, 'book11')
    tree = bst.put(tree, 40, 'book15')
    tree = bst.put(tree, 45, 'book10')
    assert bst.size(tree) == 16
    lst = bst.valueSet(tree)
    assert lt.size(lst) == 16
    assert lt.isPresent(lst, 'book20') > 0
