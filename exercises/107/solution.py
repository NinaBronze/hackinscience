import operator


def select_student(classe, note):
    bon = []
    mauvais = []
    for i in classe:
        if i[1] >= note:
            bon.append(i)
        else:
            mauvais.append(i)
    dico = {'Accepted' : \
            sorted(bon, key=operator.itemgetter(1), reverse=True),
            'Refused' : sorted(mauvais, key=operator.itemgetter(1))}
    return(dico)
