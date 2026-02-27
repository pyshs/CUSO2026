def calcul_proportion(texte, nombre_min_lettres = 4):
    """
    Calculer la proportion de mots de plus de nombre_min_lettres dans le texte
    """
    liste_mots = texte.split(" ") 
    nombre_mots = len(liste_mots)
    if len(texte) > 0: 
        compteur = 0 # 
        for i in liste_mots:
            if len(i) >= nombre_min_lettres: 
                compteur += 1
        proportion = round(100 * compteur / nombre_mots, 2)
        informations = {"Total": compteur, 
                        "Proportion": proportion, 
                        "Phrase": texte,
                        "Seuil": nombre_min_lettres,
        }
    return informations