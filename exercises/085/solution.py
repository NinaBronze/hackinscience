import operator


def sort_a_list(l):
    a = sorted(l)
    print(a)


def sort_by_mark(my_class):
    a = sorted(my_class, key=operator.itemgetter(0), reverse=True)
    print(a)


def sort_by_name(my_class):
    a = sorted(my_class, key=operator.itemgetter(1))
    print(a)
