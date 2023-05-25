class Grpah:
    def __init__(self):
        self.graph = {}

    def AddVertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []
        else:
            print("Vertex Already Exist")

    def AddEdge(self, vertex1, vertex2):
        if vertex1 in self.graph and vertex2 in self.graph:
            self.graph[vertex1].append(vertex2)
            self.graph[vertex2].append(vertex1)
        else:
            print("Vertex Doesn't Exist")
    
    def GetNeighber(self, vertex):
        if vertex in self.graph:
            return self.graph[vertex]
        else:
            return []

    def Display(self):
        print(self.graph)

graph = Grpah()
graph.AddVertex("A")
graph.AddVertex("B")
graph.AddVertex("C")
graph.AddVertex("D")

graph.AddEdge("A", "B")
graph.AddEdge("B", "C")
graph.AddEdge("C", "D")
graph.AddEdge("D", "A")

print(graph.GetNeighber("A"))
print(graph.GetNeighber("B"))
graph.Display()