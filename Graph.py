

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
    "A": [["C",3]],
    "B": [["C",4]],
    "C":[["A",3],["B",4],["D",5],["E",4]],
    "D":[["G",3],["C",5]],
    "E":[["I",8],["C",4]],
    "F":[["G",5]],
    "G":[["D",3],["F",5],["H",4],["K",1]],
    "H":[["I",2],["G",4]],
    "I":[["E",8],["H",2],["J",6],["L",2]],
    "J":[["I",6]],
    "K":[["G",1]],
    "L":[["I",2]]
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