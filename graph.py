class Graph:
    # Graph Constructor
    def __init__(self):
        self.adj_list = {}
        self.visited = set()
        self.stack = []
        
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
        
    # Remove vertex
    def remove_vertex(self,vertex):
        if vertex in self.adj_list.keys():
            for ver in self.adj_list[vertex]:
                self.adj_list[ver].remove(vertex)
            del self.adj_list[vertex]    
    
    
    # DFS method using iterative approach        
    def DFS(self,first_vertex):
        self.stack.append(first_vertex)
        while self.stack:
            current = self.stack.pop()
            if current not in self.visited:
                print(current)
                self.visited.add(current)
                for vertex in self.adj_list[current]:
                    self.stack.append(vertex)


    # DFS method using recursion approach  
    def DFS_recursion(self,first_vertex):
        self.stack.append(first_vertex)
        current = self.stack.pop()
        if current not in self.visited:
            print(current)
            self.visited.add(current)
            for vertex in self.adj_list[current]: 
                self.DFS_recursion(vertex)  

my_graph = Graph()

my_graph.add_vertex("A")
my_graph.add_vertex("B")
my_graph.add_vertex("C")
my_graph.add_vertex("D")
my_graph.add_vertex("E")

my_graph.add_edge("A","B")
my_graph.add_edge("A","C")
my_graph.add_edge("A","D")
my_graph.add_edge("B","D")
my_graph.add_edge("B","E")
my_graph.add_edge("E","D")
my_graph.add_edge("C","D")

# my_graph.DFS("A")
print("--------------")
my_graph.DFS("B")
print("----------")
my_graph.DFS_recursion("A")
# my_graph.DFS_recursion("A")