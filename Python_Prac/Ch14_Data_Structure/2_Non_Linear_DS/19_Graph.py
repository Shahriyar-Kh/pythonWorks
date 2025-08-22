#Example 1 We can present this graph in a python program as below
#Create the dictionary with graph element 
graph={
    "a":["b","c"],
    "b":["a","d"],
    "c":["a","d"],
    "d":["e"],
    "e":["d"]
}
print("\n\n********************* Create Graph from dict ****************")

#printthe graph
print(graph)
"""
******************* Display graph vertices *****************
['a', 'b', 'c', 'd', 'e']
"""
#Example 2 Display graph vertices
"""
To display the graph vertices we simple find the keys of the graph dictionary. We use the keys() method."""
print("\n\n******************* Display graph vertices *****************")
class graph:
    def __init__(self,gdict=None):
        if gdict is None:
            gdict=[]
        self.gdict=gdict
    #Get the keys of the dict
    def getVerticks(self):
        return list(self.gdict.keys())
    
#Create the dict with graph elements
graph_Dict= {
    "a":["b","c"],
    "b":["a","d"],
    "c":["a","d"],
    "d":["e"],
    "e":["d"]
}
#Create object and pass this dict
obj=graph(graph_Dict)
print(obj.getVerticks())
"""
******************* Display graph vertices *****************
['a', 'b', 'c', 'd', 'e']
"""

#Example 3 Display graph edges
"""
Finding the graph edges is little tricker than the vertices as we have to find each of the pairs of vertices which have an edge in between them. So we create an empty list of edges then iterate through the edge values associated with each of the vertices. A list is formed containing the distinct group of edges found from the vertices."""

print("\n\n**************************** Display graph edges ************************************ ")
class graph:
    def __init__(self,gdict=None):
        if gdict is None:
            gdict=[]
        self.gdict=gdict
    def edges(self):
        return self.findedges()
    #Find the distinct list of edges
    def findedges(self):
        edgename=[]
        for vrtx in self.gdict:
            for nextvrtx in self.gdict[vrtx]:
                if {nextvrtx,vrtx} not in edgename:
                    edgename.append({vrtx,nextvrtx})
        return edgename
    
#Create the dict with graph elements
graph_Dict= {
    "a":["b","c"],
    "b":["a","d"],
    "c":["a","d"],
    "d":["e"],
    "e":["d"]
}
#Create object and pass this dict
obj=graph(graph_Dict)
print(obj.edges())

#Example 4  Adding a vertex
"""
Adding a vertex is straight forward where we add another additional key to the graph dictionary."""

print("\n\n******************* Adding a vertex *****************")
class graph:
    def __init__(self,gdict=None):
        if gdict is None:
            gdict=[]
        self.gdict=gdict
    #Get the keys of the dict
    def getVerticks(self):
        return list(self.gdict.keys())
    
    #Add vertix
    def addVertex(self,vrtx):
        if vrtx not in self.gdict:
            self.gdict[vrtx]=[]

#Create the dict with graph elements
graph_Dict= {
    "a":["b","c"],
    "b":["a","d"],
    "c":["a","d"],
    "d":["e"],
    "e":["d"]
}
#Create object and pass this dict
obj=graph(graph_Dict)
obj.addVertex('f')
print(obj.getVerticks())

#Example 5 Adding an edge
"""
Adding an edge to an existing graph involves treating the new vertex as a tuple and validating if the edge is already present. 
If not then the edge is added."""

print("\n\n**************************** Add graph edges ************************************ ")
class graph:
    def __init__(self,gdict=None):
        if gdict is None:
            gdict=[]
        self.gdict=gdict
    def edges(self):
        return self.findedges()
    
    def addEdges(self,edge):
        edge=set(edge)
        (vrtx1,vrtx2)=tuple(edge)
        if vrtx1 in self.gdict:
            self.gdict[vrtx1].append(vrtx2)
        else:
            self.gdict[vrtx1]=[vrtx2]
    #Find the distinct list of edges
    def findedges(self):
        edgename=[]
        for vrtx in self.gdict:
            for nextvrtx in self.gdict[vrtx]:
                if {nextvrtx,vrtx} not in edgename:
                    edgename.append({vrtx,nextvrtx})
        return edgename
    
#Create the dict with graph elements
graph_Dict= {
    "a":["b","c"],
    "b":["a","d"],
    "c":["a","d"],
    "d":["e"],
    "e":["d"]
}
#Create object and pass this dict
obj=graph(graph_Dict)
obj.addEdges({'a','e'})
obj.addEdges({'a','c'})
print(obj.edges())