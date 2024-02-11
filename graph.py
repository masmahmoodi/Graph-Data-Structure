class Graph:
    # Graph Constructor
    def __init__(self):
        self.adj_list = {}
        
    # adding vertex    
    def add_vertex(self,vertex):
       if vertex not in self.adj_list.keys(): 
           self.adj_list[vertex] = []
           return True
       return False

   
    # printing graph
    def print_graph(self):
        for keys,value in self.adj_list.items():
            print(f"{keys}: {value}")        


    # adding edges
    def add_edge(self,ver1,ver2):
        if ver1 in self.adj_list.keys() and ver2 in self.adj_list.keys():
            self.adj_list[ver1].append(ver2)
            self.adj_list[ver2].append(ver1)
            return True
        return False
    

    # Removing edges
    def remove_edge(self,ver1,ver2):
        if ver1 in self.adj_list.keys() and ver2 in self.adj_list.keys():
            try:
                self.adj_list[ver1].remove(ver2)
                self.adj_list[ver2].remove(ver1)
            except ValueError:
                # in here we are telling to python if the are is occur just ignore it
                pass    
            return True
        return True
        
    
    def remove_vertex(self,vertex):
        if vertex in self.adj_list.keys():
            for ver in self.adj_list[vertex]:
                self.adj_list[ver].remove(vertex)
            del self.adj_list[vertex]    
            
    


my_graph = Graph()
my_graph.add_vertex("A")   
my_graph.add_vertex("B")
my_graph.add_vertex("C")

my_graph.add_edge("A","B")
my_graph.add_edge("A","C")
my_graph.add_edge("C","B")

my_graph.print_graph()
print("------------")
# my_graph.remove_edge("A","B")
my_graph.remove_vertex("A")
my_graph.print_graph()        