Sügavus-Esmalt otsing ehk Depth-First Search (DFS).
# Rekursiivse implementatsiooniga kood:

def Sügavusotsing_rekursiivne(graaf, sõlm, läbi_vaadatud=None, tulemus=None):
    if läbi_vaadatud is None:
        läbi_vaadatud = set()
    if tulemus is None:
        tulemus = []

    läbi_vaadatud.add(sõlm)  #Märgi sõlm läbi vaadatuks
    tulemus.append(sõlm)  #Lisa sõlm tulemusse

    for naaber in graaf[sõlm]:
        if naaber not in läbi_vaadatud:
            Sügavusotsing_rekursiivne(graaf, naaber, läbi_vaadatud, tulemus)

    return tulemus
# Ajakeerukus
Ajakeerukus sõltub sõlmede arvust (V) ja ühenduste ehk kaarte arvust (E).
Seljuhul oleks ajakeerukus O(V+E), kuna iga sõlm ja ühendus vaadatakse läbi maksimaalselt ühe korra.
# Ruumikeerukus
Ruumikeerukus sõltub rekursiooni sügavusest, mis on graafi maksimaalne sügavus.
Ruumikeerukus on halvimal juhul O(V).
