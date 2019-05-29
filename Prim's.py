class Graph():
    def __init__(self, vertices): 
        self.V = vertices 
        self.graph = [[0 for column in range(vertices)]  
                    for row in range(vertices)] 
    def printMST(self, parent): 
        sum=0
        print("Edge \tWeight")
        for i in range(1,self.V): 
            print(parent[i],"-",i,"\t",self.graph[i][parent[i]])
            sum+=self.graph[i][parent[i]]
        print('Total min cost=',sum)
    def minKey(self, key, mstSet):  
        min = float('Inf') 
        for v in range(self.V): 
            if key[v] < min and mstSet[v] == False: 
                min = key[v] 
                min_index = v 
  
        return min_index 
    def primMST(self): 
        key = [float('Inf')] * self.V 
        parent = [None] * self.V 
        key[0] = 0 
        mstSet = [False] * self.V 
        parent[0] = -1 
        for cout in range(self.V): 
            u = self.minKey(key, mstSet) 
            mstSet[u] = True 
            for v in range(self.V):  
                if self.graph[u][v] > 0 and mstSet[v] == False and key[v] > self.graph[u][v]: 
                        key[v] = self.graph[u][v] 
                        parent[v] = u 
  
        self.printMST(parent) 
n=int(input('Enter the number of vertices\n')) 
v=int(input('Enter the number of edges\n'))
g = Graph(n) 
for i in range(v):
    u,v,cost=input('Enter edge(u,v) and cost:\n').split()
    u=int(u)
    v=int(v)
    cost=int(cost)
    g.graph[u][v]=cost
    g.graph[v][u]=cost
g.primMST(); 
