#adjacency list
class Graph:
    def __init__(self) -> None:
        #initialize with an empty dictionary
        self.adj_list = {}
    #method for printing out all vertices and edges
    def print_graph(self):
        for vertex in self.adj_list:
            print(vertex, ": ", self.adj_list[vertex])

    #adds a vertex with no edges to the graph
    def add_vertex(self, vertex):
        if vertex not in self.adj_list.keys():
            self.adj_list[vertex] = []
            return True
        return False
    
    #adds an edge between two vertices
    def add_edge(self, v1, v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            self.adj_list[v1].append(v2)
            self.adj_list[v2].append(v1)
            return True
        return False
    
    #removes an edge between 2 vertices
    def remove_edge(self, v1, v2):
        if v1 in self.adj_list.keys() and v2 in self.adj_list.keys():
            #try to remove the edge
            try:
                self.adj_list[v1].remove(v2)
                self.adj_list[v2].remove(v1)
            #if edge doesnt exist thats fine just pass and return true
            except ValueError:
                pass
            return True
        return False
    
    #remove a vertex
    def remove_vertex(self, vertex):
        if vertex in self.adj_list.keys():
            #loop through all edges in the vertex and delete them 
            # from the other verteces edge lists
            for v in self.adj_list[vertex]:
                self.adj_list[v].remove(vertex)
            del self.adj_list[vertex]
            return True
        return False
    
graph = Graph()
print('\n')
graph.add_vertex(1)
graph.add_vertex(2)
graph.add_edge(1, 2)
graph.print_graph()
print('\n')
graph.print_graph()
print('\n')