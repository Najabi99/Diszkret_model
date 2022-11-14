import random


from Station import Allomas
from passenger import Utas
from Line import Vonal
from Train import Vonat

allomas_string_lista = ["BUD", "GYOR", "KOM", "SZEK", "SIO", "PECS", "KECS", "SZE", "SZO", "DEB", "MIS"]
utas_ossz_list = []
allomas_list = []
vonal_list = []
stations = {
    "BUD": ["KOM", "SZEK", "PECS", "KECS", "MIS"],
    "GYOR": ["KOM", "SZEK"],
    "KOM": ["BUD", "GYOR"],
    "SZEK": ["SIO", "BUD", "GYOR"],
    "SIO": ["SZEK", "PECS"],
    "PECS": ["SIO", "BUD"],
    "KECS": ["BUD", "SZE", "SZO"],
    "SZE": ["KECS"],
    "SZO": ["KECS", "DEB"],
    "DEB": ["SZO", "MIS"],
    "MIS": ["DEB", "BUD"]
}

lines = {
    "GYOR-SZE": ["GYOR","KOM","BUD","KECS","SZE"],
    "PECS-GYOR": ["PECS","SIO","SZEK","GYOR"],
    "PECS-MIS":["PECS","BUD","MIS"],
    "MIS-SZE": ["MIS","DEB","SZO","KECS","SZE"],
    "BUD-DEB":["BUD","KECS","SZO","SZE"]
}

for allo in allomas_string_lista:
    tmp_utas_list = []
    for cel in random.sample(allomas_string_lista, max(1, random.randint(0, len(allomas_string_lista) - 1))):
        random.randint(1, 10)
        tmp = Utas(random.randint(1, 10), allo, cel)
        utas_ossz_list.append(tmp)
        tmp_utas_list.append(tmp)
    tmp2 = Allomas(allo, stations[allo], tmp_utas_list)
    allomas_list.append(tmp2)

for line in lines:
    tmp = Vonal(lines[line])
    vonal_list.append(tmp)


