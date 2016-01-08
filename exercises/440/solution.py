

def filtered(items, filtre):
    new_items = []
    a = ''
    for i in items:
        if filtre(i):
            new_items.append(i)
    for j in new_items[0:len(new_items)-1]:
        a = a + str(j) + ', '
    a = a + str(new_items[-1])
    return(a)

if __name__ == '__main__':
    print(filtered(range(0, 101), lambda x: x % 3 == 0))
    print(filtered(range(0, 101), lambda x: x % 5 == 0))
    print(filtered(range(0, 101), lambda x: x % 15 == 0))
