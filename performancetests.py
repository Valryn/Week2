import timeit

testdict = {}

for k in range(99):
    testdict[k] = 1

lst = [1] * 100


def dictionaryget():
    for i in range(99):
        x = testdict.get(i)


def dictionaryget_timer():
    setup_code = """
from __main__ import dictionaryget
"""

    test_code = """
dictionaryget()
"""
    times = timeit.repeat(setup=setup_code, stmt=test_code, repeat=5, number=1000)

    print('Dictionary get time min: {}'.format(min(times)))
    print('Dictionary get time max: {}'.format(max(times)))


def dictionaryset():
    for i in range(99):
        x = testdict[i]


def dictionaryset_timer():
    setup_code = """
from __main__ import dictionaryset
"""

    test_code = """
dictionaryset()
"""
    times = timeit.repeat(setup=setup_code, stmt=test_code, repeat=5, number=1000)

    print('Dictionary set time min: {}'.format(min(times)))
    print('Dictionary set time max: {}'.format(max(times)))


def listindex():
    for i in range(99):
        x = lst[i]


def listindex_timer():
    setup_code = """
from __main__ import listindex
"""

    test_code = """
listindex()
"""
    times = timeit.repeat(setup=setup_code, stmt=test_code, repeat=5, number=1000)

    print('List index time min: {}'.format(min(times)))
    print('List index time max: {}'.format(max(times)))


def listdel():
    testlist = [1] * 100
    for i in range(99):
        del testlist[1]


def listdel_timer():
    setup_code = """
from __main__ import listdel
    """

    test_code = """
listdel()
    """
    times = timeit.repeat(setup=setup_code, stmt=test_code, repeat=5, number=1000)

    print('List del time min: {}'.format(min(times)))


def dictdel():
    deldict = {}

    for i in range(99):
        deldict[i] = 1

    for i in range(99):
        del deldict[i]


def dictdel_timer():
    setup_code = """
from __main__ import dictdel
    """

    test_code = """
dictdel()
    """
    times = timeit.repeat(setup=setup_code, stmt=test_code, repeat=5, number=1000)

    print('Dictionary del time min: {}'.format(min(times)))


if __name__ == "__main__":
    listindex_timer()
    dictionaryget_timer()
    dictionaryset_timer()
    listdel_timer()
    dictdel_timer()
