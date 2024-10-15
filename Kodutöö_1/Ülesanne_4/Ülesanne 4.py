def bin_otsing(numbrid, siht):
    algus = 0
    lõpp = len(numbrid) - 1

    while algus <= lõpp:
        kesk = (algus + lõpp) // 2
        if numbrid[kesk] == siht:
            return f"Element leitud indeksilt: {kesk}"
        elif numbrid[kesk] < siht:
            algus = kesk + 1
        else:
            lõpp = kesk - 1

    return "Elementi ei leitud loendist."

# Näide kasutusest
sorteeritud_numbrid = [2, 6, 10, 11, 17, 20, 31, 50]
siht = 31
tulemus = bin_otsing(sorteeritud_numbrid, siht)
print(tulemus)
