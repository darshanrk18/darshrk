def bellman_ford(edges,src):
    dist = {}
    path = {}
    for i in edges:
        if i[0] == src:
            dist[i[0]] = 0
            path[i[0]] = [i[0]]
        else:
            dist[i[0]] = 1000
            path[i[0]] = []
        if i[1] == src:
            dist[i[1]] = 0
            path[i[1]] = [i[1]]
        else:
            dist[i[1]] = 1000
            path[i[1]] = []
    for i in range(1,len(dist.keys())):
        for j in edges:
            if dist[j[1]] > dist[j[0]] + j[2]:
                dist[j[1]] = dist[j[0]] + j[2]
                path[j[1]] = path[j[0]] + [j[1]]
    for i in dist:
        if i != src:
            print("Distance from source to", i, "is", dist[i], "and path is", path[i])



graph = {}
no_of_edges = int(input("Enter number of edges : "))
edges = []
for i in range(no_of_edges):
    start,end,weight = input("Enter start node, end node and weight : ").split()
    weight = int(weight)
    edges.append((start,end,weight))
src = input("Enter source node : ")
bellman_ford(edges,src)
