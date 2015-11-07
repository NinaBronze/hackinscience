def is_alpha(num):
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    for i in num:
        if alphabet.find(i) < 0:
            return(False)
    return(True) 
