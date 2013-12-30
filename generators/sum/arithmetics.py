from util import Writer

__author__ = 'alex'


def add(w, a, b):
    def add_impl(symbol, l):
        w.add_source('print ' + str(a) + symbol + str(b))
        w.add_output(l(a, b))

    add_impl('+', lambda x, y: x + y)
    add_impl('-', lambda x, y: x - y)
    add_impl('*', lambda x, y: x * y)
    add_impl('/', lambda x, y: abs(x) / abs(y) * cmp(x, 0) * cmp(y, 0))

w = Writer('arithmetic')

add(w, -1, 2)
add(w, 83, 23)
add(w, 1, 234234)
add(w, 0, 1)
add(w, -1, 1)
add(w, 8445, 4734)
add(w, 543, 23)
add(w, 23434, 2)
add(w, -43223, 34525)
add(w, -3424, 34242)
add(w, 4322, 3422)
add(w, -4342, 967)
add(w, 2, 23)
add(w, 3262, 262)
add(w, 83, 23)
# r = Random(123)
#
# for r in range(0, 10):
#     add(w, r.randint(0, 1000), r.randint(0, 1000))

w.close()