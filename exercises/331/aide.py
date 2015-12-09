def sans_tiret_sans_espace(phrase):
    sans_tiret = phrase.split("- ")
    phrase_2_0 = " ".join(sans_tiret)
    sans_espace = phrase_2_0.split(" ")
    return(sans_espace)
