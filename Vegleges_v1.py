class Graph:
    def __init__(self, V, E):
        self.E = list([u,v,weight] for u,v,weight in E)
        self._nbrs = {}
        self.V = V
        self.aMatrix = [[0 for i in range(len(V)) ] for j in range(len(V))]


        for v in V:
            self.addvertex(v)
        for u,v,weight in self.E:
            self.addedge(u,v)
        for u, v, weight in E:
            self.aMatrix[(ord(u)-65)][(ord(v)-65)] = weight
            self.aMatrix[(ord(v)-65)][(ord(u)-65)] = weight
        
    
    def addedge(self, u, v):
        self.addvertex(u)
        self.addvertex(v)
        self._nbrs[u].add(v)
        self._nbrs[v].add(u)

    def addvertex(self, v):
        if v not in self._nbrs:
            self._nbrs[v] = set()

    def deg(self, v):
        return len(self._nbrs[v])
    
    def nbrs(self, v):
        return iter(self._nbrs[v])

    def printSolution(self, dist):
        print(dist)
        print("Vertex \t Distance from Source")
        for node in range(len(self.V)):
            print(node, "\t\t", dist[node])

	
    def minDistance(self, dist, sptSet):

        min = 1000

        for v in range(len(self.V)):
            if dist[v] < min and sptSet[v] == False:
                min = dist[v]
                min_index = v

        return min_index

	

    def dijkstra(self, src):

        dist = [1000] * len(self.V)
        dist[src] = 0
        sptSet = [False] * len(self.V)

        for cout in range(len(self.V)):

            u = self.minDistance(dist, sptSet)

            sptSet[u] = True

            for v in range(len(self.V)):
                if (self.aMatrix[u][v] > 0 and
                sptSet[v] == False and
                dist[v] > dist[u] + self.aMatrix[u][v]):
                    dist[v] = dist[u] + self.aMatrix[u][v]
        
     
        
        #self.printSolution(dist)
        return dist

    @property
    def m(self):
        return len(self.E)
    
    @property
    def n(self):
        return len(self._nbrs)

stations = {
    "A":[["B",2],["G",5]],
    "B":[["B",2],["C",4],["H",5]],
    "C":[["H",5],["D",6],["B",4]],
    "D":[["E",3],["C",6]],
    "E":[["D",3],["J",2],["F",9]],
    "F":[["E",9],["K",5],["R",4]],
    "G":[["A",5],["H",3],["S",2],["O",8]],
    "H":[["G",3],["B",5],["I",2],["L",3],["C",5]],
    "I":[["H",2],["L",3],["J",3]],
    "J":[["I",3],["E",2],["K",4],["M",3]],
    "K":[["F",5],["Q",2],["J",4],["N",3]],
    "L":[["H",3],["I",3],["M",3]],
    "M":[["L",3],["J",3],["N",2],["O",3],["N",2]],
    "N":[["P",1],["M",2],["K",3]],
    "O":[["P",4],["G",8],["T",2],["M",3]],
    "P":[["N",1],["O",4],["U",2],["Q",4]],
    "Q":[["K",2],["R",3],["P",4],["V",2]],
    "R":[["Q",3],["F",5]],
    "S":[["G",2],["T",8],["W",6]],
    "T":[["O",2],["U",3],["S",8],["W",7],["X",5]],
    "U":[["T",3],["V",3],["P",2],["Y",3]],
    "V":[["Q",2],["U",3]],
    "W":[["T",7],["X",5],["S",6]],
    "X":[["T",5],["Y",6],["W",5],["X",5]],
    "Y":[["X",6],["U",3],["Z",6]],
    "Z":[["Y",6],["X",5]],


}




vertex = []

for key in stations:
    vertex.append(key)
edges = []

for key, value in stations.items():
     for i in range(len(value)):
        edges.append([key,value[i][0],value[i][1]])


cimek = ["A","C","D","G","H","Z","S"]

sources = ["D","B"]

Map = Graph (vertex,edges)
Map.dijkstra(10)

def feladat (source, cimek_in):
  traveled = 0
  ut = []
  cimek = cimek_in
  print("Innen indultal", source)
  #c??mek ??t??r??sa bet??b??l sz??mm??
  cimek = [(ord(i)-65) for i in cimek]
  #addig futtatjuk am??g van m??g pont ahova nem ment??nk m??g el
  while (len(cimek) > 0):
    #futtatunk egy dijsktrat a "source" pontb??l
    distance = Map.dijkstra((ord(source)-65))
    #kivesszuk azokat a pontokat amikbe sz??ll??tunk
    dist = [distance[i] for i in cimek]
    #meg??llap??tjuk a legk??zelebbit
    for i in cimek:
      if distance[i] == min(dist):
        next = i
    #hozz??adjuk a t??vols??got az ??sszes "??thoz"
    traveled += min(dist)
    ut.append(next)
    print("A k??vetkez?? c??med: ",chr(next+65))
    #kit??r??lj??k a pontot ??s ??t??ll??tjuk az ??jat a kezd??pontnak
    cimek.remove(next)
    source = chr(next+65)
  print("Ossz utazott km",traveled)
  print('\n')
  return ut, traveled

ut = []
hoszak = []

for i in range(len(sources)):
  uttmp,hoszaktmp= feladat(sources[i],cimek)
  ut.append(uttmp)
  hoszak.append(hoszaktmp)

for i in range(len(ut)):
  if hoszak[i] == min(hoszak):
    print(f"A legr??videbb ??t {hoszak[i]} hossz??")
    print(f"A(z) rakt??rb??l indul: {sources[i]}")
    print(f"??s az al??bbi ??ton halad: {ut[i]}")
    break
