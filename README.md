# INFK_Python_frogger

Képek betöltődése -> béka megjelenik alul középen, a levél, amire el kell juttatni felül középen, az út szélén pedig az autók. Két autó tart jobbról balra, egy pedig balról jobbra, mindegyik más sebességgel közlekedve.
A béka irányítható előre, hátra, jobbra és balra, mind az AWSD billentyűkkel, mind a nyilakkal.
A békának három élete van, ezekből akkor veszít, amikor ütközik egy autóval, és visszakerül a kezdőpozícióba.
Amikor a béka eléri a levelet, a bejuttatott békák száma nő 1-gyel. A béka visszakerül a kezdőpozícióba, hogy új békát lehessen a levélre juttatni.
A játék "megnyeréséhez" három békát kell bejuttatni.

Hibák:
-> a béka kezdőpozícióba való helyezésénél a késleltetés kikommentelve, mert akkor az élet és bejuttatott békák számlálója nem jól számol
-> az autók mozgása és újrajövetele működik, de valamelyiknél csak úgy, hogy bizonyos kódrészeket ki kellett kommentelni, pedig másik autónál azzal működik (de most már legalább folyamatosan jönnek)
