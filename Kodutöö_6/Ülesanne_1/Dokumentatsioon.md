Läbimise üheks tehnikaks on Laius-esmalt otsing ehk Breadth-First Search (BFS).
# Algoritmi kood:

from collections import deque

def Laius_otsing(graaf, algus):
    läbi_vaadatud = set()           #Hoiab meeles juba läbi vaadatud sõlmed
    järjekord = deque([algus])   #Sõlmed, mida veel uurida
    tulemus = []                 #Järjekord, milles sõlmed läbi vaadatakse

    while järjekord:
        sõlm = järjekord.popleft()   #Võtame järgmise sõlme järjekorrast
        if sõlm not in läbi_vaadatud:
            läbi_vaadatud.add(sõlm)     #Märgime sõlme läbi vaadatuks
            tulemus.append(sõlm)    #Lisame tulemusse
            # Lisa kõik naabrid, mida pole läbi vaadatud, uurimisjärjekorda
            järjekord.extend(naaber for naaber in graaf[sõlm] if naaber not in läbi_vaadatud)

    return tulemus

# Kujutame graafi:
A --- B
|     |
C --- D

# Esitame selle graafi Pythonis sõnastikuna:
graaf = {"A" : ["B", "C"], "B" : ["A", "D"], "C" : ["A", "D"], "D" : ["B", "C"]}

# Saame kogu töötava koodi:

from collections import deque

graaf = {"A" : ["B", ""], "B" : ["A", "D"], "C" : ["A", "D"], "D" : ["B", "C"]}

def Laius_otsing(graaf, algus):
    läbi_vaadatud = set()           #Hoiab meeles juba läbi vaadatud sõlmed
    järjekord = deque([algus])   #Sõlmed, mida veel uurida
    tulemus = []                 #Järjekord, milles sõlmed läbi vaadatakse

    while järjekord:
        sõlm = järjekord.popleft()   #Võtame järgmise sõlme järjekorrast
        if sõlm not in läbi_vaadatud:
            läbi_vaadatud.add(sõlm)     #Märgime sõlme läbi vaadatuks
            tulemus.append(sõlm)    #Lisame tulemusse
            # Lisa kõik naabrid, mida pole läbi vaadatud, uurimisjärjekorda
            järjekord.extend(naaber for naaber in graaf[sõlm] if naaber not in läbi_vaadatud)

    return tulemus

tulemus = Laius_otsing(graaf, "A")
print("Laiusotsingu läbi vaadatud järjekord:", tulemus)

# Tulemuseks on "Laiusotsingu läbi vaadatud järjekord: ['A', 'B', 'C', 'D']"
