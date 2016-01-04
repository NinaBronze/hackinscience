

def filtered(items, filtre):
    new_items = []
    for i in items:
        if filtre(i):
            new_items.append(i)
    for j in new_items[0:len(new_items)-1]:
        a = print(j, end=', ')
    a = print(new_items[len(new_items)-1])
    return(a)

if __name__ == '__main__':
    trois = filtered(range(0, 101), lambda x: x % 3 == 0)
    cinq = filtered(range(0, 101), lambda x: x % 5 == 0)
    quinze = filtered(range(0, 101), lambda x: x % 15 == 0)
