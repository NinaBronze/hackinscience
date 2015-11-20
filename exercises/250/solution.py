def draw_n_squares(n):
    haut = '+' + (n * '---+')
    cotes = '|' + (n * '   |')
    t = ''
    for i in range(1, n+1):
        i = haut + '\n' + cotes + '\n'
        t = t + i
    return(t + haut)
