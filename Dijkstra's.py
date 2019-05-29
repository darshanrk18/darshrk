def minimum_dist(dist,queue):
    minimum=float('Inf')
    min_index=-1
    for i in range(len(dist)):
        if dist[i]<minimum and i in queue:
            minimum=dist[i]
            min_index=i
    return min_index
def printpath(parent,j):
    if parent[j]==-1:
        print(j,end='')
        return
    printpath(parent,parent[j])
    print(j,end='')
def printsolution(dist,parent,s):
    src=s
    print('Vertex\tDistance from source\tPath')
    for i in range(len(dist)):
        if i!=src:
            print('%d-->%d\t\t%d\t\t\t\t\t'%(src,i,dist[i]),end='')
            printpath(parent,i)
            print()
def dijkstra(graph,src):
    n=len(graph)
    parent=[-1]*n
    dist=[float('Inf')]*n
    dist[src]=0
    queue=[]
    for i in range(n):
        queue.append(i)
    while queue:
        u=minimum_dist(dist,queue)
        queue.remove(u)
        for i in range(n):
            if graph[u][i] and i in queue and dist[u]+graph[u][i]<dist[i]:
                dist[i]=dist[u]+graph[u][i]
                parent[i]=u
    printsolution(dist,parent,src)
n=int(input('Enter no of vertices: '))
e=int(input('Enter no of edges: '))
g=[[0 for x in range(n)] for y in range(n)]
for i in range(e):
    u,v,cost=input('Enter an edge(u,v) and its cost(eg, u v cost): ').split()
    u=int(u)
    v=int(v)
    cost=int(cost)
    g[u][v]=cost
    g[v][u]=cost
s=int(input('Enter the source vertex: '))
dijkstra(g,s)
