

class Graph:
    def __init__(self, V, E):
        self.E = list([u,v,weight] for u,v,weight in E)
        self._nbrs = {}
        self.V =V

        for v in V:
            self.addvertex(v)
        for u,v,weight in self.E:
            self.addedge(u,v)
    
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
    "L":[["",2]]
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
print(Map._nbrs)

#print(f"Paths between {start} and {end}: ", route_graph.get_paths(start, end))