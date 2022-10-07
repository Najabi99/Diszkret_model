from optparse import Values
from tkinter import E


class Graph1: 
    def __init__(self, edges):
        self.edges = edges
        self.graph_dict = {}
        for start, end in self.edges:
            if start in self.graph_dict:
                self.graph_dict[start].append(end)
            else:
                self.graph_dict[start] = [end]

        print("Graph Dictionary",self.graph_dict)

    def get_paths(self, start, end, path =[]):

        path = path +[start]

        if start == end:
            return [path]
        if start not in self.graph_dict:
            return []

        paths =[]

        for node in self.graph_dict[start]:
            if node not in path:
                new_paths = self.get_paths(node, end, path)
                for p in new_paths:
                    paths.append(p)
        return paths

class Graph:
    def __init__(self, V, E):
        self.E = set(frozenset((u,v)) for u,v in E)
        self._nbrs = {}
        for v in V:
            self.addvertex(v)
        for u,v in self.E:
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
    "BUD": ["KOM","SZEK","PECS","KECS","MIS",],
    "GYOR": ["KOM","SZEK"],
    "KOM":["BUD","GYOR"],
    "SZEK":["SIO","BUD","GYOR"],
    "SIO":["SZEK","PECS"],
    "PECS":["SIO","BUD"],
    "KECS":["BUD","SZE","SZO"],
    "SZE":["KECS"],
    "SZO":["KECS","DEB"],
    "DEB":["SZO","MIS"],
    "MIS":["DEB","BUD"]
}
lines = {
    "GYOR-SZE": ["GYOR","KOM","BUD","KECS","SZE"],
    "PECS-GYOR": ["PECS","SIO","SZEK","GYOR"],
    "PECS-MIS":["PECS","BUD","MIS"],
    "MIS-SZE": ["MIS","DEB","SZO","KECS","SZE"],
    "BUD-DEB":["BUD","KECS","SZO","SZE"]
}

vertex = []

for key in stations:
    vertex.append(key)
edges = []

for key, value in stations.items():
    for i in range(len(value)):
        edges.append([key,value[i]])

Map = Graph (vertex,edges)
print(Map.__dict__)
print(Map.n)
print(Map.m)



#print(f"Paths between {start} and {end}: ", route_graph.get_paths(start, end))