from util import Writer

__author__ = 'alex'


def create_sum_test(min_value, max_value, step):
    w = Writer('sum')

    for a in range(min_value, max_value, step):
        for b in range(min_value, max_value, step):
            w.add_source(str(a) + ' + ' + str(b))
            w.add_output(str(a + b))

    w.close()


create_sum_test(-1000, 1000, 10)