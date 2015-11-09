def starts_with(str1, str2):
    nb = len(str2)
    print(nb)
    if str2 == str1[0:nb]:
        return(True)
    else:
        return(False)
