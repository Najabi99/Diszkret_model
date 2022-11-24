

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

        self.printSolution(dist)

    @property
    def m(self):
        return len(self.E)
    
    @property
    def n(self):
        return len(self._nbrs)

stations = {
    "A":[["B",3],["I",7]],
    "B":[["A",3],["C",2],["J",6]],
    "C":[["J",5],["D",3],["B",2]],
    "D":[["J",4],["H",4],["E",1],["C",3]],
    "E":[["H",3],["D",1]],
    "F":[["L",6],["G",7],["H",3]],
    "G":[["M",9],["F",7]],
    "H":[["K",3],["D",4],["E",3],["F",5]],
    "I":[["J",5],["O",4],["R",7],["A",7]],
    "J":[["I",5],["B",6],["C",5],["D",4],["K",6]],
    "K":[["J",6],["H",3],["L",2],["O",5]],
    "L":[["K",2],["F",6],["M",3],["N",2],["P",4]],
    "M":[["L",3],["G",9],["Q",9],["P",4],["N",1]],
    "N":[["L",2],["M",1],["P",2]],
    "O":[["K",5],["I",4],["S",6],["P",1]],
    "P":[["O",1],["L",4],["N",2],["Q",3],["T",6],["M",4]],
    "Q":[["M",9],["P",3],["U",7]],
    "R":[["I",7],["V",3],["S",5]],
    "S":[["R",5],["O",5],["V",7],["W",2],["T",3]],
    "T":[["S",3],["P",6],["U",7],["W",8]],
    "U":[["Q",7],["T",7],["W",4]],
    "V":[["R",3],["S",7],["W",3],["X",9]],
    "W":[["V",3],["T",8],["U",4],["X",5],["Y",7]],
    "X":[["V",9],["W",5],["Y",1],["Z",5]],
    "Y":[["W",7],["X",1],["Z",6]],
    "Z":[["Y",6],["X",5]],


}




vertex = []

for key in stations:
    vertex.append(key)
edges = []

for key, value in stations.items():
     for i in range(len(value)):
        edges.append([key,value[i][0],value[i][1]])
# for key, value in stations.items():
#     print("key",key)
#     print("value",value)

Map = Graph (vertex,edges)
print(Map.__dict__)
print(Map.m)
print(Map.n)
print(Map.aMatrix)
Map.dijkstra(0)


#print(f"Paths between {start} and {end}: ", route.aMatrix.get_paths(start, end))