from pythonds.graphs import Graph
from pythonds.basic import Queue

class DFSGraph(Graph):
    def __init__(self):
        "init"
        super().__init__()
        self.time = 0

    def dfs(self):
        for aVertex in self:
            aVertex.setColor('white')
            aVertex.setPred(-1)

        for aVertex in self:
            if aVertex.getColor() == 'white' :
                self.dfsvisit(aVertex)

    def dfsvisit(self, startVertex):
        startVertex.setColor('gray')
        self.time += 1
        startVertex.setDiscovery(self.time)

        for nextVertex in startVertex.getConnections():
            if nextVertex.getColor() == 'white' :
                nextVertex.setPred(startVertex)
                self.dfsvisit(nextVertex)

        startVertex.setColor('black')
        self.time += 1
        startVertex.setFinish(self.time)

    def topologicalSorting(self):
        self.dfs()

        topList = []

        for key in self.vertices:
            topList.append(self.vertices[key])

        topList.sort(key = lambda x:x.fin)
        topList.reverse()

        return topList

    def transpose(self):
        for aVertex in self:
            aVertex.setColor('white')

        for key in self.vertices:
            start = self.vertices[key]
            break

        vertQueue = Queue()
        vertQueue.enqueue(start)

        while vertQueue.size() > 0:
            currentVert = vertQueue.dequeue()
            toDel = []

            for nbr in currentVert.getConnections():
                # here is the key
                if currentVert.connectedTo[nbr] != -1 :
                    nbr.connectedTo[currentVert] = -1
                    toDel.append(nbr)

                if nbr.getColor() == 'white' :
                    vertQueue.enqueue(nbr)

            for vertex in toDel:
                if currentVert.connectedTo[vertex] == 0 :
                    del currentVert.connectedTo[vertex]

            currentVert.setColor('black')

    def dfsScc(self):
        for aVertex in self:
            aVertex.setColor('white')

        alist = []
        for key in self.vertices:
            alist.append(self.vertices[key])

        alist.sort(key = lambda x : x.fin, reverse = True)

        components = []

        for aVertex in alist:
            if aVertex.getColor() == 'white' :
                component = []
                self.dfsvisitScc(aVertex, component)
                components.append(component)

        return components

    def dfsvisitScc(self, startVertex, component):
        component.append(startVertex.getId())
        startVertex.setColor('gray')

        for nextVertex in startVertex.getConnections():
            if nextVertex.getColor() == 'white' :
                self.dfsvisitScc(nextVertex, component)

        startVertex.setColor('black')

    def scc(self):
        self.dfs()
        self.transpose()
        return self.dfsScc()


if __name__ == "__main__" :
    print("scc: ")

    g = DFSGraph()
    g.addEdge("A", "B")
    g.addEdge("B", "C")
    g.addEdge("B", "E")
    g.addEdge("C", "F")
    g.addEdge("D", "B")
    g.addEdge("D", "G")
    g.addEdge("E", "A")
    g.addEdge("E", "D")
    g.addEdge("F", "H")
    g.addEdge("G", "E")
    g.addEdge("H", "I")
    g.addEdge("I", "F")

    # g.addEdge("A", "B")
    # g.addEdge("A", "C")
    # g.addEdge("B", "D")
    # g.addEdge("D", "A")

    print(g.scc())

print()

def knightGraph(bdSize):
    ktGraph = DFSGraph()

    for row in range(bdSize):
        for col in range(bdSize):
            nodeId = posToNodeId(row, col, bdSize)
            newPositions = genLegalMoves(row, col, bdSize)

            for e in newPositions:
                nid = posToNodeId(e[0], e[1], bdSize)
                ktGraph.addEdge(nodeId, nid)

    return ktGraph

def posToNodeId(row, column, board_size):
    return (row * board_size) + column

def genLegalMoves(x, y, bdSize):
    newMoves = []
    moveOffsets = [(-1,-2), (-1,2), (-2,-1), (-2,1),
                   ( 1,-2), ( 1,2), ( 2,-1), ( 2,1)]

    for i in moveOffsets:
        newX = x + i[0]
        newY = y + i[1]

        if legalCoord(newX, bdSize) and \
           legalCoord(newY, bdSize):
            newMoves.append((newX, newY))

    return newMoves

def legalCoord(x, bdSize):
    if x >= 0 and x < bdSize :
        return True
    else :
        return False

# if __name__ == "__main__" :
#     # dfs
#     kg = knightGraph(4)
#     kg.dfs()

#     for id in kg.getVertices():
#         print(id)

#     print()

#     # topological Sorting
#     kgTopo = knightGraph(4)

#     for v in kgTopo.topologicalSorting():
#         print(v.getId(), v.getFinish())
