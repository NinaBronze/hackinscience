def sans_tiret_sans_espace(phrase):
    sans_tiret = phrase.split("- ") 
    phrase_2_0 = " ".join(sans_tiret)
    sans_espace = phrase_2_0.split(" ")
    for i in sans_espace:
        if i == '':
            sans_espace.remove(i)
    return(sans_espace)
