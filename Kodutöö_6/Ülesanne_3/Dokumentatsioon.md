Dijkstra on graafi otsingu algoritm, mis leiab lühimad teed alguspunktist kõigi teiste graafi tippudeni.
# Dijkstra algoritmi kasutusjuhud
  1. Võrgu marsruutimisprotokollid
  2. Google Maps - lühima tee leidmine ühest asukohast teise.
  3. Sotsiaalvõrgustikud - lühimate teede leidmine sotsiaalgraafis.
  4. Telekommunikatsioon - Kõnede marsruutimine telefonivõrkudes.
# Dijkstra algoritmi keerukus
Ajaline keerukus on O((V+E)Log V).
Ruumiline keerukus on O(V).
# Dijkstra efektiivsus
  1. Positiivsete kaaludega graafid - transpordivõrgud, kus tee pikkused on positiivsed.
  2. Kui kasutame tihedaid graafe ja prioriteetset järjekorda (min-heap või Fibonacci).
  3. Kui on vaja leida lühimad teed ühest ühest asukohast mitmesse sihtkohta (marsruutide planeerimine).
  4. Staatilised ehk muutumatud graafid või graafid, mis ei muutu sagedasti.
# Dijkstra ebaefektiivsus
  1. Negatiivsete kaaludega graafid - negatiivse kaaluga servad võivad anda valesid tulemusi.
  2. Väga suured ja hõredad graafid - Kui graafis on plaju sõlmi ja vähe servi, muutub ressursikulukaks.
  3. Dünaamilised graafid - kui graaf muutub  sageli, sest peab iga kord nullist arvutama.
