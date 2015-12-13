def sans_tiret_sans_espace(phrase):
    sans_tiret = phrase.split("- ")
    if len(sans_tiret) > 2:
        sans_tiret[0] = "- ".join(sans_tiret[0:2])
        del sans_tiret[1]
    phrase_2_0 = " ".join(sans_tiret)
    sans_espace = phrase_2_0.split(" ")
    for i in sans_espace:
        if i == '':
            sans_espace.remove(i)
    return(sans_espace)
