import string

def nombremots(texte):
    return len(texte.split(''))

def occMots(texte):
    dict={}
    for mot in texte.split(" "):
        mot=mot.strip(string.punctuation).lower()
        dict[mot]=dict.get(mot,0)+1
    return dict    

def longueurmoyen(text):
    mot=text.split(" ")
    longueur= [len(m) for m in mot]
    moy = sum(longueur)/len(longueur)
    occ = occMots(text)  
    occMax = max(occ.values())
    l = [k for k,v in occ.items() if v== occMax ] 
    return l,occMax, moy

def ponctuationUtilisee(texte):
    d = {}
    for c in texte:
        if c in string.punctuation:
            d[c] = d.get(c, 0) + 1
    return d


def StatsTypeMot(texte):
    mots = texte.split()
    maj = sum(1 for m in mots if m.istitle())
    upper = sum(1 for m in mots if m.isupper())
    lower = sum(1 for m in mots if m.islower())
    chiffres = sum(1 for m in mots if m.isdigit())
    return {"Majuscule initiale": maj, "Majuscules": upper, "Minuscules": lower, "Numériques": chiffres}

def top10mots(texte):
    occ = occMots(texte)
    top = sorted(occ.items(), key=lambda x: x[1], reverse=True)[:10]
    return top

def phrasesLongues(texte):
    phrases = texte.split(".")
    phrases_triees = sorted(phrases, key=lambda p: len(p.split()), reverse=True)
    return [p.strip() for p in phrases_triees[:3] if p.strip()]

def motsRepetes(texte):
    mots = [m.strip(string.punctuation).lower() for m in texte.split()]
    rep = []
    for i in range(len(mots) - 1):
        if mots[i] == mots[i + 1]:
            rep.append(mots[i])
    return set(rep)





with open('data.txt', 'rt') as file:
    data = file.read()
    nbmots = nombremots(data)
    print(f'nombre de mots est:{nbmots}')
    print("La frequence des mots est:", occMots(data))
    maxMots, maxOcc, moy = longueurmoyen(data)
    print(f"les mots les plus utilises sont {maxMots} utilise {maxOcc} fois")
    print("Ponctuation utilisée :", ponctuationUtilisee(data))
    print("Statistiques par type de mot :", StatsTypeMot(data))
    print("Top 10 des mots :")
    for mot, freq in top10mots(data):
        print(f"  - {mot} : {freq}")
    phrases = phrasesLongues(data)
    print(" Phrases les plus longues :")
    for p in phrases:
        print(f"   - {p}")
    rep = motsRepetes(texte)
    print("Mots répétés consécutivement :", rep if rep else "Aucun")
