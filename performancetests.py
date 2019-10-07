import timeit

# Establish test dictionaries and lists
testdict = {}
for k in range(99):
    testdict[k] = 1

lst = [1] * 100

def dictionaryget():
    """Get each value in testdict"""
    for i in range(99):
        x = testdict.get(i)


def dictionaryget_timer():
    """Create a timer to evaluate dictionaryget"""
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
    """Set each value in testdict"""
    for i in range(99):
        x = testdict[i]


def dictionaryset_timer():
    """Create a timer to evaluate dictionaryset"""
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
    """Index each spot in lst"""
    for i in range(99):
        x = lst[i]


def listindex_timer():
    """Create a timer to evaluate listindex"""
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
    """Deletes 100 values from testlist"""
    deletelist = [1] * 100

    for i in range(100):
        del deletelist[0]


def listdel_timer():
    """Create a timer to evaluate listdel"""
    setup_code = """
from __main__ import listdel
    """

    test_code = """
listdel()
    """
    times = timeit.repeat(setup=setup_code, stmt=test_code, repeat=5, number=1000)

    print('List del time min: {}'.format(min(times)))


def dictdel():
    """Deletes 100 values from deletedict"""
    deletedict = {}
    for j in range(99):
        deletedict[j] = 1

    for i in range(99):
        del deletedict[i]


def dictdel_timer():
    """Create a timer to evaluate dictdel"""
    setup_code = """
from __main__ import dictdel
    """

    test_code = """
dictdel()
    """
    times = timeit.repeat(setup=setup_code, stmt=test_code, repeat=5, number=1000)

    print('Dictionary del time min: {}'.format(min(times)))


if __name__ == "__main__":
    # Run each timer for evaluation/comparison
    listindex_timer()
    dictionaryget_timer()
    dictionaryset_timer()
    listdel_timer()
    dictdel_timer()
