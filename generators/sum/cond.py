from util import Writer

__author__ = 'alex'


def add(w, a, b):

    def add_impl(symbol, out, l):
        w.add_source('if ' + str(a) + symbol + str(b) + ':')
        w.add_source('print ' + str(out))
        if l(a, b):
            w.add_output(str(out))
        w.add_source('end')

    add_impl('>', 1, lambda x, y: x > y)
    add_impl('>=', 2, lambda x, y: x >= y)
    add_impl('<', 3, lambda x, y: x < y)
    add_impl('<=', 4, lambda x, y: x <= y)
    add_impl('==', 5, lambda x, y: x == y)
    add_impl('!=', 6, lambda x, y: x != y)


w = Writer('cond')

add(w, 0, 0)
add(w, 123, 232)
add(w, 342234, 1)
add(w, 123, -2)
add(w, -3123, 2423)
add(w, -234234, -23)
add(w, -6, -345345)

w.close()
