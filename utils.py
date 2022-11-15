from Station import Allomas
from passenger import Utas
import random


allomas_string_lista = ["BUD", "GYOR", "KOM", "SZEK", "SIO", "PECS", "KECS", "SZE", "SZO", "DEB", "MIS"]
print(type((random.sample(allomas_string_lista,max(1,random.randint(0,len(allomas_string_lista)-1))))))

print(random.randint(0,len(allomas_string_lista)-1))