def greedyColoring(adj, V):
    
    color_names = ["green","red", "yellow", "blue",  "orange", "purple"]
    
    result = [-1] * V
    result[0] = "green"  
   
    available = [False] * V

    for u in range(1, V):
       
        for i in adj[u]:
            if result[i] != -1:
                available[color_names.index(result[i])] = True

        cr = 0
        while cr < V:
            if not available[cr]:
                break
            cr += 1
  
        result[u] = color_names[cr]

        for i in adj[u]:
            if result[i] != -1:
                available[color_names.index(result[i])] = False

    for u in range(V):
        print("Vertex", u, " --->  Color", result[u])


def read_graph_from_file(filename):
    with open(filename, 'r') as file:
        V = int(file.readline())  
        adj = [[] for _ in range(V)]  

        for u in range(V):
            adj[u] = list(map(int, file.readline().strip().split()))
    
    return adj, V

filename = input("Enter the filename : ")
adj, V = read_graph_from_file(filename)
print("Coloring of the graph:")
greedyColoring(adj, V)


