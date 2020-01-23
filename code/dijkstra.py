from pythonds.graphs import PriorityQueue, Graph, Vertex

def dijkstra(aGraph, start):
    pq = PriorityQueue()
    start.setDistance(0)
    pq.buildHeap([(v.getDistance(), v) for v in aGraph])

    while not pq.isEmpty():
        currentVert = pq.delMin()

        for nextVert in currentVert.getConnections():
            newDist = currentVert.getDistance() \
                + currentVert.getWeight(nextVert)

            if newDist < nextVert.getDistance() :
                nextVert.setDistance(newDist)
                nextVert.setPred(currentVert)
                pq.decreaseKey(nextVert, newDist)

g = Graph()
g.addEdge(1, 2, 1)
g.addEdge(1, 5, 11)
g.addEdge(2, 3, 1)
g.addEdge(3, 4, 1)
g.addEdge(4, 5, 1)

startVertex = g.getVertex(1)

dijkstra(g, startVertex)

endVertex = g.getVertex(5)
predVertex = endVertex

# print(predVertex.getPred())

while predVertex is not None:
    print(predVertex.getId())
    predVertex = predVertex.getPred()
