from util import Writer

__author__ = 'alex'


def add(w, a):
    """

    @type w: Writer
    """
    w.add_input(str(a))
    w.add_output(str(a))
    if (a > 0):
        name = 'var' + str(a)
    else:
        name = 'var' + str(-a)
    w.add_source(name + ' = 0')
    w.add_source('read ' + name)
    w.add_source('print ' + name)


w = Writer('io')

add(w, 0)
add(w, 1)
add(w, 1234567)
add(w, -1)
add(w, -2342423)
add(w, 100)

w.close()