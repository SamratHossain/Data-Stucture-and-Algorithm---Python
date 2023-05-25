class Graph:
    def __init__(self, NumberOfVertices):
        self.NumberOfVertices = NumberOfVertices
        self.Matrix = [[0] * NumberOfVertices for _ in range(NumberOfVertices)]
    
    def AddEdge(self, Source, Destination):
        if 0 <= Source < self.NumberOfVertices and 0 <= Destination < self.NumberOfVertices:
            self.Matrix[Source][Destination] = 1
            self.Matrix[Destination][Source] = 1

    def IsEdge(self, Source, Destination):
        if 0 <= Source < self.NumberOfVertices and 0 <= Destination < self.NumberOfVertices:
            return self.Matrix[Source][Destination] == 1
        else:
            return False

    def Display(self):
        for matrix in self.Matrix:
            print(matrix)

graph = Graph(4)
graph.AddEdge(0, 1)
graph.AddEdge(0, 2)
graph.AddEdge(2, 1)
graph.AddEdge(2, 3)

print( graph.IsEdge(0, 1))
print( graph.IsEdge(0, 3))

graph.Display()