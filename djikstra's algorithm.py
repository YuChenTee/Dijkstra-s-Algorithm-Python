graph = [[0,3,9,0,0,0],
         [3,0,0,2,1,0],
         [9,0,0,0,3,10],
         [0,2,0,0,6,3],
         [0,1,3,6,0,5],
         [0,0,10,3,5,0]]

def djikstra(graph,start):

    unvisited_vertex = []
    dist = []
    prev = []

    for i in range(len(graph)):
        unvisited_vertex.append(i)
        dist.append(0)
        prev.append(None)

    for i in range(len(graph)):
        dist[i] = float("inf")
        prev[i] = None

    dist[start] = 0
    u = None

    while len(unvisited_vertex) > 0:
        min_dist = float("inf")
        for i in range(len(graph)):
            if i in unvisited_vertex:
                if dist[i] < min_dist:
                    min_dist = dist[i]
                    u = i
        unvisited_vertex.remove(u)

        for i in range(len(graph)):
            if i in unvisited_vertex and graph[u][i] != 0 :
                if dist[u] + graph[u][i] < dist[i]:
                    dist[i] = graph[u][i] + dist[u]
                    prev[i] = u

    for i in range(len(graph)):
        print(dist[i], prev[i])


djikstra(graph,0)


